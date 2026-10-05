---
title: "Page-EntroKV: Hardware-Aligned, Entropy-Weighted KV-Cache Eviction under Grouped-Query Attention"
description: "Serving long-context autoregressive language models is constrained by the key-value (KV) cache."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.03135) · [PDF](https://arxiv.org/pdf/2610.03135)

## 一句话摘要

Serving long-context autoregressive language models is constrained by the key-value (KV) cache.

## 为什么值得关注

待编辑增强。

## 摘要原文

Serving long-context autoregressive language models is constrained by the key-value (KV) cache. Most dynamic eviction methods score token importance per query head and choose tokens independently. This fits poorly with grouped-query attention (GQA), where several query heads share one physical KV buffer: divergent per-head selections force the serving engine to retain the union of their choices - inflating the cache by up to the group ratio r - while arithmetic mean pooling dilutes the specialized retrieval heads that carry factual recall. We introduce Page-EntroKV, a formal framework for KV-cache eviction operating at the granularity GQA serving actually allocates. Heads within each physical group are pooled by weights derived from sink-isolated collision (Renyi-2) entropy - one inner product per head, computed once at prefill with no calibration - so sink heads cannot masquerade as retrieval heads. Pooled scores are projected onto PagedAttention page frames, and eviction executes at the hardware tuple (layer, group, page). We formalize the union overhead ratio (UOR) and intra-group disagreement, prove an exact identity linking them for two-head groups alongside two-sided bounds at every group ratio, prove strict budget preservation and a finite-context needle-retention bound that arithmetic mean pooling provably violates, and give exact per-layer page accounting. On a pilot architecture (Qwen2.5-1.5B-Instruct, r=6), head-independent replay over 2,240 group measurements yields union overhead up to 4.75x at a 2% budget, while Page-EntroKV holds UOR exactly 1.000; sink isolation removes a 13x sink masquerade; needle recall is 100% versus 0% for mean pooling at a 20% budget; retained cardinality is exact for every page size; and QA and code tasks remain solvable at 20% retention.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Inbasekaran S
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
