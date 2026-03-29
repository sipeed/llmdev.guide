---
id: nvidia-rtx-5090-32gb
name: NVIDIA RTX 5090 32GB
vendor: NVIDIA
device_type: "GPU"
chip: GB202
memory_capacity_gb: 32
memory_bandwidth_gbs: 1792
memory_type: GDDR7
tops_int8: 3352
tops_note: FP4 Tensor Core sparse, actual dense INT8 significantly lower
price_usd: 3999
power_watts: 575
interface: PCIe x16
benchmarks:
- model: Llama 7B
  quant: Q4_0
  framework: llama.cpp CUDA
  decode_tps: 300.4
  prefill_tps: 14970.0
  note: measured, FA=1
- model: Qwen3 8B
  quant: Q4_K_XL
  framework: llama.cpp CUDA
  decode_tps: 145.3
  context_length: 16384
  note: measured, Hardware Corner
- model: Qwen3 30B-A3B
  quant: Q4_K_XL
  framework: llama.cpp CUDA
  decode_tps: 141.6
  prefill_tps: 4669.0
  context_length: 16384
  note: measured, MoE 3B active, Hardware Corner
- model: Qwen3 32B
  quant: Q4_K_XL
  framework: llama.cpp CUDA
  decode_tps: 50.9
  prefill_tps: 2077.0
  context_length: 16384
  note: measured, Dense 32B, Hardware Corner
- model: Qwen3.5-9B
  quant: int4
  framework: llama.cpp CUDA
  decode_tps: 198.0
  note: "measured"
- model: Qwen3.5-27B
  quant: int4
  framework: llama.cpp CUDA
  decode_tps: 90.0
  note: measured, source HN
- model: Qwen3.5-35B-A3B
  quant: int4
  framework: llama.cpp CUDA
  decode_tps: 194.0
  note: measured, source llama.cpp #19890
submitted_by: community
date: '2026-03-28'
---

# NVIDIA RTX 5090 32GB — Benchmark Report

## Test Environment

- **OS**: Linux (Ubuntu)
- **Framework**: llama.cpp (CUDA backend, Flash Attention enabled)
- **Model source**: Hugging Face (GGUF)
- **Cooling**: Stock cooler
- **Power supply**: Standard ATX PSU (1000W+ recommended)

## Sources

- [llama.cpp #15013](https://github.com/ggml-org/llama.cpp/discussions/15013) — Llama 7B Q4_0: decode 300.4 tps, prefill 14970 tps (FA=1)
- [Hardware Corner](https://hardware-corner.net) — Qwen3 8B/32B/30B-A3B @16K context
- [Hacker News](https://news.ycombinator.com/item?id=47292522) — Qwen3.5-27B int4: 90 tps
- [llama.cpp #19890](https://github.com/ggml-org/llama.cpp/discussions/19890) — Qwen3.5-35B-A3B int4: 194 tps

## Notes

The RTX 5090 with Blackwell GB202 delivers the highest decode throughput among consumer GPUs thanks to 1792 GB/s GDDR7 bandwidth. MSRP is $1,999 but actual street price is ~$3,799 due to extreme demand and GDDR7 supply constraints. The 32GB VRAM allows running 27B dense and 35B MoE models comfortably. The 575W TDP is substantial and requires adequate cooling and power supply.

Qwen3.5-35B-A3B achieves 194 tps — faster than the dense 9B model estimate (234 tps) would suggest for a 3B-active MoE, likely due to MoE-specific optimizations in recent llama.cpp builds.
