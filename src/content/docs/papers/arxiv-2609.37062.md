---
title: "vSkipper: Translating Dynamic Layer Skipping into LLM Serving Gains"
description: "Dynamic layer skipping reduces LLM computation by allowing each token to execute only a subset of the model's layers."
---

**评分：50/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.37062) · [PDF](https://arxiv.org/pdf/2609.37062)

## 一句话摘要

Dynamic layer skipping reduces LLM computation by allowing each token to execute only a subset of the model's layers.

## 为什么值得关注

待编辑增强。

## 摘要原文

Dynamic layer skipping reduces LLM computation by allowing each token to execute only a subset of the model's layers. However, existing skippers rely on specialized generation loops and do not integrate with modern serving engines. As a result, fewer executed layers do not necessarily translate into lower serving latency: FlexiDepth skips 8 of Llama-3-8B's 32 layers on average, yet its standard generation loop decodes 14.6--21.0% more slowly than the base model. We present vSkipper, a virtualization layer that makes dynamic layer skippers pluggable in serving engines while preserving continuous batching, fixed-shape batches, paged KV caching, and captured decode graphs. At each routed layer, vSkipper groups tokens by the skipper's decision and uses routed execution only when predicted to be profitable. We implement vSkipper in SGLang and evaluate the released FlexiDepth checkpoint against upstream SGLang under identical prompts, arrivals, output lengths, and launch settings. At the knee of upstream's load curve, vSkipper reduces mean end-to-end latency by 36.8% on GSM8K and 13.6% on BBH. Under saturation, it increases request throughput by 11.3% and 7.4%. Serving adds no statistically resolved quality loss beyond the checkpoint's own. Across synthetic skip policies, two Qwen3 skippers, and three GPUs, we demonstrate reuse without workload-specific tuning. To our knowledge, vSkipper is the first system to realize serving-efficiency gains from per-token interior layer skipping within a modern LLM serving engine. The code is open-sourced as an SGLang fork at https://github.com/AKafakA/sglang-vskipper/tree/vskipper-ref

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Wei Da, Yavuz Ferhatosmanoglu, Evangelia Kalyvianaki
- 发布：2026-09-29；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/AKafakA/sglang-vskipper/tree/vskipper-ref](https://github.com/AKafakA/sglang-vskipper/tree/vskipper-ref)
- 阅读深度：metadata
