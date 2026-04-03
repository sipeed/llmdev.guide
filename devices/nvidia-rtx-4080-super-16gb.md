---
id: "nvidia-rtx-4080-super-16gb"
name: "NVIDIA GeForce RTX 4080 SUPER 16GB"
vendor: "NVIDIA"
device_type: "GPU"
chip: "AD103 (Ada Lovelace)"

memory_capacity_gb: 16
memory_bandwidth_gbs: 736
memory_type: "GDDR6X"

price_usd: 1000
power_watts: 320

interface: "PCIe x16"

benchmarks:
  - model: "Qwen3 8B"
    quant: "Q4_K"
    framework: "llama.cpp"
    decode_tps: 104.2
    prefill_tps: 6137.0
    note: "measured, Hardware Corner GPU ranking, 4K context"
  - model: "Qwen3 14B"
    quant: "Q4_K"
    framework: "llama.cpp"
    decode_tps: 64.2
    prefill_tps: 3745.0
    note: "measured, Hardware Corner GPU ranking, 4K context"
  - model: "Qwen3.5-9B"
    quant: "Q4_K"
    framework: "llama.cpp"
    decode_tps: 92.7
    estimated: true
    estimated_from: "Qwen3 8B 104.2 tps (8B -> 9B, x0.89, Dense->Dense)"

submitted_by: "community"
date: "2026-04-03"
---

# NVIDIA GeForce RTX 4080 SUPER 16GB — Benchmark Report

## Test Environment

- **GPU**: NVIDIA GeForce RTX 4080 SUPER (AD103, Ada Lovelace)
- **VRAM**: 16GB GDDR6X, 736 GB/s
- **Framework**: llama.cpp (CUDA backend)
- **Quantization**: Q4_K
- **Context**: 4K tokens

## Sources

- [Hardware Corner — RTX 4080 SUPER LLM Benchmarks](https://www.hardware-corner.net/gpu-llm-benchmarks/rtx-4080-super/)

## Notes

- 736 GB/s bandwidth is higher than RTX 5070 Ti (504 GB/s), resulting in strong decode performance despite older architecture.
- 16GB VRAM can run 14B models at Q4, but 27B+ models do not fit.
- At ~$1000 (street price), fills the gap between RTX 4060 Ti 16GB and RTX 4090 in price and performance.
- Prefill speed (6137 tps on Qwen3 8B) benefits from Ada Lovelace's mature tensor core implementation.
