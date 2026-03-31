---
id: "apple-macbook-pro-m5-max-128gb"
name: "Apple MacBook Pro M5 Max 128GB (40-core GPU)"
vendor: "Apple"
device_type: "Mini PC"
chip: "Apple M5 Max (18-core CPU, 40-core GPU)"

memory_capacity_gb: 128
memory_bandwidth_gbs: 614
memory_type: "LPDDR5X"

price_usd: 4999
power_watts: 100

interface: "Onboard"

benchmarks:
  - model: "Qwen3.5-122B-A10B"
    quant: "Q4"
    framework: "MLX"
    decode_tps: 65.9
    prefill_tps: 881.0
    note: "measured, Hardware Corner, 4K context"
  - model: "Qwen3.5-27B"
    quant: "Q6"
    framework: "MLX"
    decode_tps: 23.6
    prefill_tps: 811.0
    note: "measured, Hardware Corner, 4K context"
  - model: "Llama 3.3 70B"
    quant: "Q4_K_M"
    framework: "MLX"
    decode_tps: 9.95
    note: "measured, Hardware Corner"
  - model: "Qwen3.5-9B"
    quant: "Q4"
    framework: "MLX"
    decode_tps: 78.7
    estimated: true
    estimated_from: "Qwen3.5-27B Q6 23.6 tps, bandwidth model: 614*0.9/4.5=122.8 ceiling, scaled from 27B Q6 actual/ceiling ratio"
  - model: "Qwen3.5-35B-A3B"
    quant: "Q4"
    framework: "MLX"
    decode_tps: 65.9
    estimated: true
    estimated_from: "Qwen3.5-122B-A10B 65.9 tps (10B -> 3B active, MoE->MoE, conservative same speed)"

submitted_by: "community"
date: "2026-03-31"
---

# Apple MacBook Pro M5 Max 128GB (40-core GPU) — Benchmark Report

## Test Environment

- **Device**: MacBook Pro 16-inch (M5 Max, 128GB unified memory)
- **CPU**: 18-core (6 Super + 12 Performance)
- **GPU**: 40-core with Neural Accelerators
- **Memory**: 128GB LPDDR5X, 614 GB/s bandwidth
- **Framework**: MLX
- **Process**: TSMC 3nm Fusion Architecture

## Sources

- [Hardware Corner — M5 Max LLM Benchmarks](https://www.hardware-corner.net/m5-max-local-llm-benchmarks-20261233/)

## Notes

- The M5 Max 40-core GPU delivers 614 GB/s bandwidth, a ~50% increase over M4 Max (410 GB/s).
- Prefill speed sees the biggest improvement (~3-4x over M4) thanks to Neural Accelerators in every GPU core.
- Decode speed improvement is more modest (~12-19%) since it remains memory-bandwidth-bound.
- 128GB unified memory can comfortably run 122B MoE models and 70B dense models at Q4.
- MLX is recommended over llama.cpp for best Apple Silicon performance (~20-30% faster).
