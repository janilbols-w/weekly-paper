---
title: "ValueDiff: Value-Geometric KV Cache Eviction for Sink-Suppressed LLMs"
description: "Modern LLMs with QK-normalization, gated attention, learned attention sinks, or logit softcapping exhibit weaker persistent attention sinks, on which existing KV cache eviction methods primarily rely."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.23314) · [PDF](https://arxiv.org/pdf/2609.23314)

## 一句话摘要

Modern LLMs with QK-normalization, gated attention, learned attention sinks, or logit softcapping exhibit weaker persistent attention sinks, on which existing KV cache eviction methods primarily rely.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern LLMs with QK-normalization, gated attention, learned attention sinks, or logit softcapping exhibit weaker persistent attention sinks, on which existing KV cache eviction methods primarily rely. We observe that across these models, weaker sinks co-occur with greater value-vector dispersion relative to key-vector dispersion. Motivated by this value-side dispersion, we present ValueDiff, a value-geometric eviction that ranks tokens by the L2 deviation of their value vectors from the cache mean. The same score arises as the minimal-disturbance eviction under a max-entropy assumption about future attention. We evaluate under fixed cache budgets, with eviction at every block boundary during prefill and at every decoding step during generation. On RULER at a tight 2k token budget, ValueDiff retains 88--99\% of dense across seven sink-suppressed models (best on 6 out of 7). On LongBench at the 4k budget, ValueDiff averages 92\% retention across sink-suppressed models versus 83\% for the strongest prior baseline. On MATH-500, ValueDiff is the strongest non-dense method on every sink-suppressed model tested at the 25\% cache budget, outperforming prior methods by up to $\sim$20 points on gated-attention models. Across all three benchmarks, value geometry emerges as the more reliable query-invariant eviction signal for sink-suppressed models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Junyoung Park, Jungwook Choi, Mingu Lee
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
