---
id: "nvidia-rtx-5060-ti-16gb"
name: "NVIDIA GeForce RTX 5060 Ti 16GB"
vendor: "NVIDIA"
device_type: "GPU"
chip: "GB206 (Blackwell)"

memory_capacity_gb: 16
memory_bandwidth_gbs: 448
memory_type: "GDDR7"
memory_bus_width: "128bit"

price_usd: 429
power_watts: 180

interface: "PCIe x16"

benchmarks:
  - model: "Qwen3 8B"
    quant: "Q4_K"
    framework: "llama.cpp"
    decode_tps: 69.2
    prefill_tps: 2965.0
    note: "measured, Hardware Corner GPU ranking, 4K context"
  - model: "Qwen3 14B"
    quant: "Q4_K"
    framework: "llama.cpp"
    decode_tps: 41.1
    prefill_tps: 1743.0
    note: "measured, Hardware Corner GPU ranking, 4K context"
  - model: "Qwen3.5-9B"
    quant: "Q4_K"
    framework: "llama.cpp"
    decode_tps: 61.6
    estimated: true
    estimated_from: "Qwen3 8B 69.2 tps (8B -> 9B, x0.89, Dense->Dense)"

submitted_by: "community"
date: "2026-04-03"
---

# NVIDIA GeForce RTX 5060 Ti 16GB — Benchmark Report

## Test Environment

- **GPU**: NVIDIA GeForce RTX 5060 Ti (GB206, Blackwell)
- **VRAM**: 16GB GDDR7, 448 GB/s
- **Framework**: llama.cpp (CUDA backend)
- **Quantization**: Q4_K
- **Context**: 4K tokens

## Sources

- [Hardware Corner — RTX 5060 Ti LLM Benchmarks](https://www.hardware-corner.net/gpu-llm-benchmarks/rtx-5060-ti-16gb/)

## Notes

- At $429, the best budget Blackwell option with 16GB VRAM.
- 16GB VRAM can run 14B models at Q4, but 27B+ models do not fit.
- 180W TDP makes it efficient — Qwen3 8B at 69 tps with only 180W is strong power efficiency.
- Qwen3 8B decode drops from 69 tps (4K) to 51 tps (16K) to 28 tps (64K) as context grows.
