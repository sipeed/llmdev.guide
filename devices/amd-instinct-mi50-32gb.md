---
id: "amd-instinct-mi50-32gb"
name: "AMD Instinct MI50 32GB"
vendor: "AMD"
device_type: "GPU"
chip: "Vega 20 (GCN 5.1)"

memory_capacity_gb: 32
memory_bandwidth_gbs: 1024
memory_type: "HBM2"
memory_bus_width: "4096bit"

tops_int8: 53
tops_note: "FP16 26.5 TFLOPS, no dedicated tensor cores"

price_usd: 600
power_watts: 300

interface: "PCIe x16"

benchmarks:
  - model: "Llama 3.1 8B"
    quant: "Q4_K_M"
    framework: "llama.cpp ROCm"
    decode_tps: 71.1
    note: "measured, llama-bench tg128, ahelpme.com"
  - model: "Qwen3-30B-A3B"
    quant: "Q4_K_M"
    framework: "llama.cpp ROCm"
    decode_tps: 73.1
    note: "measured, Qwen3-Coder-30B-A3B llama-bench tg128, ahelpme.com"
  - model: "Gemma3 27B"
    quant: "Q4_K_M"
    framework: "Ollama"
    decode_tps: 19.8
    note: "measured, tinyredinc/paperhub GitHub"
  - model: "Qwen3.5-9B"
    quant: "Q4_K_M"
    framework: "llama.cpp ROCm"
    decode_tps: 63.2
    estimated: true
    estimated_from: "Llama 3.1 8B 71.1 tps (8B -> 9B, x0.89, Dense->Dense)"
  - model: "Qwen3.5-27B"
    quant: "Q4_K_M"
    framework: "Ollama"
    decode_tps: 19.8
    estimated: true
    estimated_from: "Gemma3 27B 19.8 tps (27B -> 27B, x1.00, Dense->Dense)"
  - model: "Qwen3.5-35B-A3B"
    quant: "Q4_K_M"
    framework: "llama.cpp ROCm"
    decode_tps: 73.1
    estimated: true
    estimated_from: "Qwen3-30B-A3B 73.1 tps (3B -> 3B active, x1.00, MoE->MoE)"

submitted_by: "community"
date: "2026-03-31"
---

# AMD Instinct MI50 32GB — Benchmark Report

## Test Environment

- **GPU**: AMD Radeon Instinct MI50 32GB (Vega 20, 7nm)
- **Memory**: 32GB HBM2, 4096-bit, 1.0 TB/s bandwidth
- **Framework**: llama.cpp (ROCm backend) / Ollama
- **Quantization**: Q4_K_M

## Sources

- [llama-bench Llama 3.1 8B on MI50](https://ahelpme.com/ai/llamacpp-ai/llama-bench-the-llama-3-1-8b-and-amd-radeon-instinct-mi50-32gb/)
- [llama-bench Qwen3-Coder-30B-A3B on MI50](https://ahelpme.com/ai/llamacpp-ai/llama-bench-the-qwen3-coder-30b-a3b-and-amd-radeon-instinct-mi50-32gb/)
- [MI50 LLM Performance (tinyredinc/paperhub)](https://github.com/tinyredinc/paperhub/blob/master/mi50-llm-performance/mi50_llm_performance.md)

## Notes

- The MI50 is a datacenter GPU from 2018, the 32GB version available used on eBay for ~$600. At this price point, 32GB HBM2 with 1 TB/s bandwidth is exceptional value.
- ROCm support for MI50 (gfx906) is deprecated — current versions still work but no new optimizations are coming.
- 32GB HBM2 can comfortably run 27B dense and 35B MoE models at Q4.
- Qwen3-30B-A3B at 73 tps is faster than Llama 3.1 8B (71 tps) thanks to only 3B active parameters in the MoE architecture.
- 300W TDP and no display output (1x mini-DP 1.4a) — this is a server card requiring adequate cooling and PSU.
- Multi-GPU scaling for decode is poor (adding a second MI50 gives <3% improvement when VRAM is sufficient).
