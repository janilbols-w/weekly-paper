---
title: "TierKV: Long-Context On-Device LLMs via Predictive Multi-Tier KV Caching"
description: "Large language models (LLMs) are moving onto mobile devices for increasingly diverse workloads over text, images, video, and audio."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.21172) · [PDF](https://arxiv.org/pdf/2609.21172)

## 一句话摘要

Large language models (LLMs) are moving onto mobile devices for increasingly diverse workloads over text, images, video, and audio.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) are moving onto mobile devices for increasingly diverse workloads over text, images, video, and audio. These applications often require long contexts, making the Key-Value (KV) cache a dominant memory bottleneck because it grows linearly with sequence length and is accessed at every decoding step. Prior work reduces KV-cache footprint through low-rank compression, token eviction, or flash offloading, but the resulting reconstruction overhead, irreversible token loss, or I/O stalls can offset the benefit of saving memory. We present TierKV, a mobile LLM inference framework built on Predictive Multi-Tier Cache Optimization (PMCO). Before decoding starts, PMCO predicts future cache demand from prefill hidden states and jointly assigns tokens to exact, low-rank, and flash-offloaded tiers under the device memory and accuracy budgets. This formulation retains access to the full context, removes the circular dependency of reactive eviction, and admits a closed-form solver that selects tier boundaries and per-layer ranks at runtime. Across eight text, vision, and audio models on three mobile SoCs, TierKV improves prefill throughput by up to 17.6x over existing mobile LLM frameworks, reduces RAM-resident KV cache by 12.5-34%, thereby enabling substantially longer contexts under the same memory budget, while incurring only minor accuracy degradation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zhihao Shu, Md Musfiqur Rahman Sanim, Jie Hu, Kun Yuan, Minghai Qin, Gagan Agrawal, Wei Niu
- 发布：2026-09-21；更新：2026-09-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
