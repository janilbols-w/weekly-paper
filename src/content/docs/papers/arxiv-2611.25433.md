---
title: "RoCoKV: Accelerating LLM Inference Serving through Uncertainty and Redundancy Aware KV Cache Compression"
description: "KV cache compression is critical for large reasoning models, where most of the cost comes from long generated reasoning traces rather than the input prompt."
---

**评分：55/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2611.25433v1) · [PDF](https://arxiv.org/pdf/2611.25433v1)

## 一句话摘要

KV cache compression is critical for large reasoning models, where most of the cost comes from long generated reasoning traces rather than the input prompt.

## 为什么值得关注

待编辑增强。

## 摘要原文

KV cache compression is critical for large reasoning models, where most of the cost comes from long generated reasoning traces rather than the input prompt. These traces often contain redundant and low-utility tokens due to looping, self-verification, and corrections. However, such tokens may still receive high attention scores, making it difficult to remove them without harming the reasoning process. We propose RoCoKV, a KV cache compression method designed for large reasoning models. RoCoKV introduces two key components. First, uncertainty-guided adaptive pruning adjusts the compression strength based on the model's confidence, allocating more memory during uncertain phases and applying stronger pruning when the model is confident. Second, redundancy-aware token selection reduces the impact of tokens that are highly similar to recent reasoning content, encouraging the model to retain more informative and diverse tokens. Beyond the algorithm, we co-design RoCoKV with the serving stack: we develop fused three-phase CUDA decode kernels and integrate them into vLLM as a drop-in plugin that preserves its paged KV layout and CUDA graph capture, turning algorithmic savings into real end-to-end speedups. Extensive experiments across three reasoning benchmarks and two reasoning models demonstrate that RoCoKV consistently improves reasoning accuracy under constrained KV cache budgets, achieving higher accuracy compared to state-of-the-art KV cache compression methods. For DeepSeek-R1-Distill-Llama-8B in vLLM, RoCoKV achieves a 1.27X speedup and 38% higher throughput on AIME25, the most challenging evaluated reasoning benchmark, and a 1.43X speedup and 45% higher throughput on the long synthetic benchmark, compared with Full-KV.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Payman Behnam, Elaheh Sobhani, Saad Amin, Yahya Hassan, Daniyal Khan, Biswadeep Chakraborty, Tanish Patwa, Souvik Kundu, Alexey Tumanov
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
