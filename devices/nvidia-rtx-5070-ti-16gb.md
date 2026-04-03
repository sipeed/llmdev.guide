---
id: "nvidia-rtx-5070-ti-16gb"
name: "NVIDIA GeForce RTX 5070 Ti 16GB"
vendor: "NVIDIA"
device_type: "GPU"
chip: "GB203 (Blackwell)"

memory_capacity_gb: 16
memory_bandwidth_gbs: 896
memory_type: "GDDR7"
memory_bus_width: "256bit"

price_usd: 749
power_watts: 300

interface: "PCIe x16"

benchmarks:
  - model: "Qwen3 8B"
    quant: "Q4_K"
    framework: "llama.cpp"
    decode_tps: 120.5
    prefill_tps: 5557.0
    note: "measured, Hardware Corner GPU ranking, 4K context"
  - model: "Qwen3 14B"
    quant: "Q4_K"
    framework: "llama.cpp"
    decode_tps: 74.3
    prefill_tps: 3265.0
    note: "measured, Hardware Corner GPU ranking, 4K context"
  - model: "Qwen3.5-9B"
    quant: "Q4_K"
    framework: "llama.cpp"
    decode_tps: 107.2
    estimated: true
    estimated_from: "Qwen3 8B 120.5 tps (8B -> 9B, x0.89, Dense->Dense)"

submitted_by: "community"
date: "2026-04-03"
---

# NVIDIA GeForce RTX 5070 Ti 16GB — Benchmark Report

## Test Environment

- **GPU**: NVIDIA GeForce RTX 5070 Ti (GB203, Blackwell)
- **VRAM**: 16GB GDDR7, 896 GB/s
- **Framework**: llama.cpp (CUDA backend)
- **Quantization**: Q4_K
- **Context**: 4K tokens

## Sources

- [Hardware Corner — GPU LLM Ranking](https://www.hardware-corner.net/gpu-ranking-local-llm/)

## Notes

- 16GB VRAM can run 14B models at Q4 comfortably, but 27B+ models do not fit.
- At $749, sits between RTX 5070 ($669) and RTX 5080 ($1499) — very close to 5070 in price but significantly faster.
- Qwen3 8B at 120.5 tps is excellent for interactive use.
- 896 GB/s bandwidth (same as RTX 5080) thanks to 256-bit GDDR7 bus — the main difference from 5080 is fewer CUDA cores.
