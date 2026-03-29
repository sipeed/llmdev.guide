#!/usr/bin/env python3
"""
解析 devices/*.md 的 YAML frontmatter，生成 docs/data/devices.json
"""

import json
import re
import shutil
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("错误: 需要安装 PyYAML: pip install pyyaml")
    sys.exit(1)

DEVICES_DIR = Path(__file__).parent.parent / "devices"
OUTPUT_FILE = Path(__file__).parent.parent / "docs" / "data" / "devices.json"
DOCS_DEVICES_DIR = Path(__file__).parent.parent / "docs" / "devices"

REQUIRED_FIELDS = [
    "id", "name", "vendor", "device_type",
    "memory_capacity_gb", "memory_bandwidth_gbs",
    "price_usd", "power_watts",
    "benchmarks", "submitted_by", "date",
]

BENCHMARK_REQUIRED = ["model", "quant", "framework", "decode_tps"]

# Known model active parameters (in billions)
MODEL_ACTIVE_PARAMS = {
    "Qwen3.5-9B": 9, "Qwen3.5-27B": 27,
    "Qwen3.5-35B-A3B": 3, "Qwen3.5-122B-A10B": 10, "Qwen3.5-397B-A17B": 17,
    "Qwen3 8B": 8, "Qwen3 14B": 14, "Qwen3 32B": 32, "Qwen3 30B-A3B": 3,
    "Qwen3-30B-A3B": 3, "8B Dense": 8,
    "Qwen2 7B": 7, "Qwen2.5 7B": 7, "Qwen2-1.5B": 1.5,
    "Llama 7B": 7, "Llama 2 7B": 7, "Llama2-7B": 7,
    "Llama 3.1 8B": 8, "Llama 3.2 3B": 3, "Llama 3.3 70B": 70,
    "Mistral 7B": 7, "Mixtral 8x7B": 12.9, "Mixtral 8x22B": 44,
    "DeepSeek-R1-Distill 8B": 8, "DeepSeek-R1-Distill 7B": 7,
    "DeepSeek-R1-Distill 70B": 70, "DeepSeek R1 671B": 37,
    "GPT-OSS-20B": 3.6, "GPT-OSS-120B": 5.1,
    "TinyLlama 1.1B": 1.1, "Gemma 2 9B": 9,
}

# Quant string -> bits per weight
QUANT_BITS = {
    "int4": 4, "fp4": 4, "q4": 4, "q4_0": 4, "q4_k_m": 4, "q4_k_xl": 4,
    "w4a8": 4, "w4a16": 4, "mxfp4": 4,
    "int8": 8, "fp8": 8, "q8_0": 8, "w8a8": 8,
    "bf16": 16, "fp16": 16, "f16": 16, "f32": 32,
}

BW_EFFICIENCY = 0.9  # 90% bandwidth utilization ceiling


def parse_frontmatter(filepath: Path) -> dict | None:
    text = filepath.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    return yaml.safe_load(parts[1])


def get_quant_bits(quant_str: str) -> float | None:
    if not quant_str:
        return None
    q = quant_str.lower().strip()
    if q in QUANT_BITS:
        return QUANT_BITS[q]
    # Try partial match
    for key, bits in QUANT_BITS.items():
        if key in q:
            return bits
    return None


def get_active_params(model_name: str, bench: dict) -> float | None:
    if model_name in MODEL_ACTIVE_PARAMS:
        return MODEL_ACTIVE_PARAMS[model_name]
    # Try to parse from model_note
    note = bench.get("model_note", "")
    m = re.search(r"([\d.]+)B active", note)
    if m:
        return float(m.group(1))
    return None


def check_bandwidth_ceiling(data: dict, filepath: Path) -> list[str]:
    """Check if reported decode_tps exceeds theoretical bandwidth ceiling.
    Also marks suspicious benchmarks with _suspicious=True in-place."""
    warnings = []
    bw = data.get("memory_bandwidth_gbs")
    if not bw or not data.get("benchmarks"):
        return warnings

    for i, bench in enumerate(data["benchmarks"]):
        decode_tps = bench.get("decode_tps")
        if not decode_tps or not isinstance(decode_tps, (int, float)):
            continue

        model = bench.get("model", "")
        active_b = get_active_params(model, bench)
        quant_bits = get_quant_bits(bench.get("quant", ""))

        if not active_b or not quant_bits:
            continue

        bytes_per_param = quant_bits / 8
        weight_gb = active_b * bytes_per_param
        ceiling_tps = bw * BW_EFFICIENCY / weight_gb

        if decode_tps > ceiling_tps:
            bench["_suspicious"] = True
            warnings.append(
                f"  ⚠ {model} {bench.get('quant','?')}: "
                f"decode {decode_tps} tps > ceiling {ceiling_tps:.1f} tps "
                f"(BW={bw} GB/s × {BW_EFFICIENCY} / {weight_gb:.1f} GB)"
            )

    return warnings


def validate_device(data: dict, filepath: Path) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in data or data[field] is None:
            errors.append(f"缺少必填字段: {field}")

    if "benchmarks" in data and data["benchmarks"]:
        for i, bench in enumerate(data["benchmarks"]):
            if not isinstance(bench, dict):
                errors.append(f"benchmarks[{i}] 格式错误")
                continue
            for field in BENCHMARK_REQUIRED:
                if field not in bench or bench[field] is None:
                    errors.append(f"benchmarks[{i}] 缺少字段: {field}")

    num_checks = {
        "memory_capacity_gb": (0.5, 10000),
        "memory_bandwidth_gbs": (1, 100000),
        "price_usd": (1, 1000000),
        "power_watts": (0.5, 10000),
    }
    for field, (lo, hi) in num_checks.items():
        val = data.get(field)
        if val is not None:
            try:
                val = float(val)
                if not lo <= val <= hi:
                    errors.append(f"{field}={val} 超出合理范围 [{lo}, {hi}]")
            except (TypeError, ValueError):
                errors.append(f"{field} 不是有效数值: {val}")

    return errors


def build():
    devices = []
    has_errors = False
    has_warnings = False

    md_files = sorted(DEVICES_DIR.glob("*.md"))
    md_files = [f for f in md_files if f.name != "_template.md"]

    if not md_files:
        print("警告: devices/ 目录下没有设备文件")

    for filepath in md_files:
        print(f"处理: {filepath.name}")
        data = parse_frontmatter(filepath)
        if data is None:
            print(f"  跳过: 无法解析 frontmatter")
            continue

        errors = validate_device(data, filepath)
        if errors:
            has_errors = True
            for err in errors:
                print(f"  错误: {err}")
            data["_has_errors"] = True
        else:
            data["_has_errors"] = False

        # Bandwidth ceiling check
        warnings = check_bandwidth_ceiling(data, filepath)
        if warnings:
            has_warnings = True
            for w in warnings:
                print(w)

        data["_source_file"] = filepath.name
        devices.append(data)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(devices, f, ensure_ascii=False, indent=2)

    # Copy device markdown files to docs/devices/ for the detail page
    if DOCS_DEVICES_DIR.exists():
        shutil.rmtree(DOCS_DEVICES_DIR)
    DOCS_DEVICES_DIR.mkdir(parents=True, exist_ok=True)
    for filepath in md_files:
        shutil.copy2(filepath, DOCS_DEVICES_DIR / filepath.name)

    print(f"\n生成: {OUTPUT_FILE}")
    print(f"共 {len(devices)} 个设备")

    if has_warnings:
        print("\n⚠ 部分设备数据超过带宽理论上限，请检查上方警告")
    if has_errors:
        print("✗ 部分设备数据存在错误，请检查上方输出")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(build())
