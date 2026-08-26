---
title: "Quantization Effects on Bangla Language Understanding in Large Language Models: A Systematic Evaluation"
description: "Post-training quantization lowers the memory footprint of Large Language Models (LLMs) and speeds up inference, which is why it is now common for on-device deployment."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.24615) · [PDF](https://arxiv.org/pdf/2608.24615)

## 一句话摘要

Post-training quantization lowers the memory footprint of Large Language Models (LLMs) and speeds up inference, which is why it is now common for on-device deployment.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training quantization lowers the memory footprint of Large Language Models (LLMs) and speeds up inference, which is why it is now common for on-device deployment. Most of what we know about its effects, however, comes from English benchmarks. It is not clear whether the same holds for morphologically complex, low-resource languages such as Bangla, and this gap is what we address here. We evaluate three model families---Qwen-2.5-7B, LLaMA-3.1-8B, and GPT-OSS-20B---in full precision and in three quantized formats (GPTQ-Int8, GPTQ-Q8, GGUF-W8A16) across five Bangla natural language understanding benchmarks (Bangla MMLU, CommonsenseQA-BN, OpenBookQA-BN, PIQA-BN, and BoolQ-BN), using zero-shot evaluation through lm-evaluation-harness. To our knowledge this is the first controlled comparison of quantization formats on Bangla NLU. The three families do not respond the same way: GPT-OSS loses up to 57.35% accuracy on reasoning-heavy tasks under GGUF-W8A16, while Qwen and LLaMA hold steady under GPTQ, and in a few cases the quantized version edges out the full-precision one. BoolQ-BN, a comprehension task, stays stable across all three families regardless of format. Taken together, these results suggest quantization can work well for Bangla deployment, but the choice of architecture and quantization method matters more than the bit width alone. We discuss what this means for practitioners choosing a model to run on constrained hardware.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ismail Hossain, Nafi Ullah Shafin, Mohammad Abdullah Al Mumin
- 发布：2026-08-26；更新：2026-08-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
