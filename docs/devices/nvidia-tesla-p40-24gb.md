---
id: "nvidia-tesla-p40-24gb"
name: "NVIDIA Tesla P40 24GB"
vendor: "NVIDIA"
device_type: "GPU"
chip: "GP102 (Pascal)"

memory_capacity_gb: 24
memory_bandwidth_gbs: 346
memory_type: "GDDR5X"
memory_bus_width: "384bit"

price_usd: 150
power_watts: 250

interface: "PCIe 3.0 x16"

benchmarks:
  - model: "Llama 2 7B"
    quant: "Q4_0"
    framework: "llama.cpp"
    decode_tps: 40.9
    note: "measured, localscore.ai"
  - model: "Qwen2.5 14B"
    quant: "Q4_K_M"
    framework: "llama.cpp"
    decode_tps: 13.6
    note: "measured, localscore.ai"
  - model: "Qwen3-30B-A3B"
    quant: "Q4_K_M"
    framework: "llama.cpp"
    decode_tps: 29.3
    note: "measured, localscore.ai"
  - model: "Qwen3.5-9B"
    quant: "Q4"
    framework: "llama.cpp"
    decode_tps: 32.7
    estimated: true
    estimated_from: "Llama 2 7B 40.9 tps (7B -> 9B, x0.78, Dense->Dense, Qwen3.5 ~24% slower adjusted to x0.80)"
  - model: "Qwen3.5-27B"
    quant: "Q4"
    framework: "llama.cpp"
    decode_tps: 13.6
    estimated: true
    estimated_from: "Qwen2.5 14B 13.6 tps (14B -> 27B, bandwidth-bound: 346*0.9/15.5=20.1 ceiling, actual ~68% efficiency)"
  - model: "Qwen3.5-35B-A3B"
    quant: "Q4"
    framework: "llama.cpp"
    decode_tps: 29.3
    estimated: true
    estimated_from: "Qwen3-30B-A3B 29.3 tps (3B -> 3B active, x1.00, MoE->MoE)"

submitted_by: "community"
date: "2026-04-03"
---

# NVIDIA Tesla P40 24GB — Benchmark Report

## Test Environment

- **GPU**: NVIDIA Tesla P40 (GP102, Pascal, 16nm)
- **VRAM**: 24GB GDDR5X, 384-bit, 346 GB/s
- **Framework**: llama.cpp (CUDA backend)
- **Quantization**: Q4_K_M / Q4_0

## Sources

- [LocalScore.ai — Tesla P40](https://www.localscore.ai/accelerator/1729)
- [Tesla P40 Local LLM Guide](https://like2byte.com/tesla-p40-local-llm-guide/)

## Notes

- The Tesla P40 is a datacenter GPU from 2016, available used for ~$150. At this price, 24GB VRAM is unmatched value.
- No tensor cores (Pascal architecture) — all inference runs on CUDA cores, significantly slower per-bandwidth than modern GPUs.
- 24GB VRAM can run 27B dense models at Q4 and 35B MoE models, making it useful for larger model experimentation on a budget.
- Passive cooling design — requires server chassis or aftermarket cooler for desktop use.
- No display output — this is a compute-only card.
- PCIe 3.0 only, but this does not bottleneck LLM inference (weights stay in VRAM).
