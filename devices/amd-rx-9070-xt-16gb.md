---
id: "amd-rx-9070-xt-16gb"
name: "AMD Radeon RX 9070 XT 16GB"
vendor: "AMD"
device_type: "GPU"
chip: "Navi 48 (RDNA 4)"

memory_capacity_gb: 16
memory_bandwidth_gbs: 624
memory_type: "GDDR6"
memory_bus_width: "256bit"

price_usd: 550
power_watts: 300

interface: "PCIe 5.0 x16"

benchmarks:
  - model: "Llama 2 7B"
    quant: "Q4_0"
    framework: "llama.cpp ROCm"
    decode_tps: 108.0
    prefill_tps: 4914.0
    note: "measured, llama.cpp GitHub #15021, tg128, FA=1"
  - model: "Qwen3.5-9B"
    quant: "Q4"
    framework: "llama.cpp ROCm"
    decode_tps: 86.4
    estimated: true
    estimated_from: "Llama 2 7B 108.0 tps (7B -> 9B, x0.78, Dense->Dense, Qwen3.5 ~24% slower on GPU adjusted to x0.80)"

submitted_by: "community"
date: "2026-04-03"
---

# AMD Radeon RX 9070 XT 16GB — Benchmark Report

## Test Environment

- **GPU**: AMD Radeon RX 9070 XT (Navi 48, RDNA 4, TSMC 4nm)
- **VRAM**: 16GB GDDR6, 256-bit, 624 GB/s
- **Framework**: llama.cpp (ROCm HIP backend)
- **Quantization**: Q4_0
- **Context**: 128 tokens (tg128)

## Sources

- [llama.cpp ROCm Performance Discussion #15021](https://github.com/ggml-org/llama.cpp/discussions/15021)

## Notes

- First RDNA 4 generation GPU, major improvements in AI/LLM inference over RDNA 3.
- 624 GB/s bandwidth at $550 is excellent value — higher bandwidth than RTX 5070 Ti at a lower price.
- Llama 2 7B Q4 at 108 tps is strong, though Qwen3.5 models run slower on AMD due to less optimized ROCm support.
- 16GB VRAM can run 14B models at Q4, but 27B+ models do not fit.
- ROCm software stack continues to improve but still lags CUDA in optimization maturity.
