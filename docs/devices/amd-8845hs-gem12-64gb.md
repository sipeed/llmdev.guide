---
id: "amd-8845hs-gem12-64gb"
name: "AMD Ryzen 7 8845HS Mini PC (GEM12) 64GB"
vendor: "AMD"
device_type: "Mini PC"
chip: "AMD Ryzen 7 8845HS"

memory_capacity_gb: 64
memory_bandwidth_gbs: 89.6
memory_type: "DDR5"
memory_speed: "5600MT/s"
memory_bus_width: "dual-channel"

price_usd: 500
power_watts: 45

interface: "Onboard"

benchmarks:
  - model: "Qwen3.5-9B"
    quant: "Q4_K_M"
    framework: "LM Studio"
    decode_tps: 13.57
    note: "measured"
  - model: "Qwen3.5-35B-A3B"
    quant: "Q4_K_M"
    framework: "LM Studio"
    decode_tps: 25.95
    note: "measured"
  - model: "Qwen3.5-27B"
    quant: "Q4_K_M"
    framework: "LM Studio"
    decode_tps: 4.32
    note: "measured"

submitted_by: "zp"
date: "2026-03-29"
---

# AMD Ryzen 7 8845HS Mini PC (GEM12) 64GB — Benchmark Report

## Test Environment

- **Device**: GEM12 Mini PC
- **CPU**: AMD Ryzen 7 8845HS (8-core Zen 4, 16 TOPS NPU)
- **Memory**: 64GB DDR5-5600 dual-channel (~89.6 GB/s)
- **Framework**: LM Studio (llama.cpp backend)
- **Quantization**: Q4_K_M for all models

## Evidence

### Qwen3.5-9B — 13.57 tps

![Qwen3.5-9B benchmark](assets/amd-8845hs-gem12-64gb/8845_9b.jpg)

### Qwen3.5-27B — 4.32 tps

![Qwen3.5-27B benchmark](assets/amd-8845hs-gem12-64gb/8845_27b.jpg)

### Qwen3.5-35B-A3B — 25.95 tps

![Qwen3.5-35B-A3B benchmark](assets/amd-8845hs-gem12-64gb/8845_35b_a3b.jpg)

## Notes

- CPU-only inference on Zen 4 cores. The 16 TOPS XDNA NPU is not used by LM Studio.
- 64GB DDR5 dual-channel provides ~89.6 GB/s bandwidth, sufficient to run 27B dense models.
- 9B at 13.57 tps is usable for interactive chat. 35B-A3B MoE at 25.95 tps is very responsive thanks to only 3B active parameters.
- 27B dense at 4.32 tps is slow but functional for non-interactive tasks.
- At ~$500 this is one of the most affordable platforms that can run 27B+ models locally.
