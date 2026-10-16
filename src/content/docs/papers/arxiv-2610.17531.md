---
title: "Towards Green AI: Evaluating Energy Efficiency for Quantized LLM Inference"
description: "While it is known that quantization of large language models (LLMs) reduces memory usage via lower-bit weights, studies quantifying the resulting impact on energy usage and carbon intensity are scarce."
---

**评分：61/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2610.17531v1) · [PDF](https://arxiv.org/pdf/2610.17531v1)

## 一句话摘要

While it is known that quantization of large language models (LLMs) reduces memory usage via lower-bit weights, studies quantifying the resulting impact on energy usage and carbon intensity are scarce.

## 为什么值得关注

待编辑增强。

## 摘要原文

While it is known that quantization of large language models (LLMs) reduces memory usage via lower-bit weights, studies quantifying the resulting impact on energy usage and carbon intensity are scarce. We present the first unified evaluation of weight-only quantization strategies for LLM inference across varying input/output lengths and GPUs, highlighting differences in energy efficiency in addition to accuracy degradation and runtime. We study quantized inference on Llama 2 7B, Phi 3.5 Mini Instruct, OLMo 1B, Qwen 2.5 7B, and Qwen 2.5 14B across GLUE MNLI, MMLU, HumanEval, and GSM8K datasets, evaluating 10 post-training quantization (PTQ) strategies on NVIDIA H100, A6000, A100, and L4 GPUs. We identify a novel trend showing that quantization techniques tend to exhibit peak energy efficiency relative to full-precision baselines when inputs are sufficiently long and outputs are short. Furthermore, we show that quantization strategies become marginally more energy-efficient relative to full-precision models as batch sizes increase, though gains are modest. Notably, fused-kernel implementations such as EETQ int8 and Bitsandbytes int8 offer the highest energy savings, up to 4x compared to FP32 on short text generation, with negligible accuracy loss. Finally, we observe that energy usage closely tracks runtime on our evaluated benchmarks, indicating that, in practice, latency optimization can serve as a reliable proxy for reducing the environmental footprint of LLM services. We conclude with suggested directions for strategically selecting low-carbon quantization strategies based on specific inference requirements.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 7 |
| rigor | 15 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, quantization, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Petar Basta
- 发布：2026-10-13；更新：2026-10-13
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
