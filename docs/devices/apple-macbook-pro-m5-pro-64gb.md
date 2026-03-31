---
id: "apple-macbook-pro-m5-pro-64gb"
name: "Apple MacBook Pro M5 Pro 64GB"
vendor: "Apple"
device_type: "Mini PC"
chip: "Apple M5 Pro (18-core CPU, 20-core GPU)"

memory_capacity_gb: 64
memory_bandwidth_gbs: 307
memory_type: "LPDDR5X"

price_usd: 3080
power_watts: 70

interface: "Onboard"

benchmarks:
  - model: "Qwen3.5-9B"
    quant: "Q4"
    framework: "MLX"
    decode_tps: 39.4
    estimated: true
    estimated_from: "M5 Max 9B 78.7 tps × BW ratio 307/614 = 0.5"
  - model: "Qwen3.5-27B"
    quant: "Q4"
    framework: "MLX"
    decode_tps: 11.8
    estimated: true
    estimated_from: "M5 Max 27B Q6 23.6 tps × BW ratio 307/614 = 0.5"
  - model: "Qwen3.5-35B-A3B"
    quant: "Q4"
    framework: "MLX"
    decode_tps: 33.0
    estimated: true
    estimated_from: "M5 Max 35B-A3B 65.9 tps × BW ratio 307/614 = 0.5"

submitted_by: "community"
date: "2026-03-31"
---

# Apple MacBook Pro M5 Pro 64GB — Benchmark Report

## Test Environment

- **Device**: MacBook Pro (M5 Pro, 64GB unified memory)
- **CPU**: 18-core (6 Super + 12 Performance)
- **GPU**: 20-core with Neural Accelerators
- **Memory**: 64GB LPDDR5X, 307 GB/s bandwidth
- **Framework**: MLX (estimated)
- **Process**: TSMC 3nm Fusion Architecture

## Sources

- Estimated from [M5 Max benchmarks (Hardware Corner)](https://www.hardware-corner.net/m5-max-local-llm-benchmarks-20261233/) scaled by bandwidth ratio (307/614 = 0.5)

## Notes

- The M5 Pro has half the GPU cores and half the memory bandwidth of the M5 Max (307 vs 614 GB/s).
- All estimates are derived from M5 Max measured data scaled by the bandwidth ratio, since decode speed is memory-bandwidth-bound.
- 64GB unified memory can run 27B dense and 35B MoE models at Q4, but not 70B+ models.
- At $3,080, positioned between the M4 Max and M5 Max in both price and performance.
