---
title: "TriAxialKV: Toward Extreme Low-Precision KV-Cache Quantization for Agentic Inference Tasks"
description: "Agentic workloads have emerged as a major workload for LLM inference."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2605.17170) · [PDF](https://arxiv.org/pdf/2605.17170)

## 一句话摘要

Agentic workloads have emerged as a major workload for LLM inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Agentic workloads have emerged as a major workload for LLM inference. They differ significantly from chat-only workloads, requiring long-context processing, the ability to handle multimodal inputs, and structured multi-turn interactions with tool calling capabilities. As a result, their context exhibits structure that can carry different importance along three key axes: temporal recency to the current turn, modality such as text or image tokens, and semantic role such as user queries, tool calls, observations, or reasoning. These axes capture distinct token behaviors and lead to different sensitivities to KV-cache compression. However, existing KV-cache quantization methods are typically homogeneous or exploit only heterogeneity on a single dimension, such as temporal proximity or modality, overlooking the interactions among them. To this end, we introduce TriAxialKV, a novel mixed-precision KV-cache quantization scheme that assigns each token a triaxial tag, calibrates per-tag sensitivity, and allocates INT2/INT4 bit-widths under a fixed memory budget. We implement TriAxialKV as an end-to-end serving system, comprising calibration, mixed-precision quantization and memory management, and custom fused Triton decode kernels. When using Qwen3-VL-32B-Thinking as a computer-use agent operating the OSWorld, TriAxialKV matches the accuracy of SGLang with BF16 KV cache while supporting 4.5$\times$ KV cache capacity and achieving 30% higher end-to-end throughput, when running on real GPU systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hanzhang Shen, Haoran Wu, Yiren Zhao, Robert Mullins
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
