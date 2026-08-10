---
title: "Every Cache Entry Earns Its Place: Global Allocation of Resolution and Coverage for KV Cache Compression"
description: "As large language models (LLMs) process increasingly long contexts, KV cache storage and repeated access have become a major bottleneck."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.07001) · [PDF](https://arxiv.org/pdf/2608.07001)

## 一句话摘要

As large language models (LLMs) process increasingly long contexts, KV cache storage and repeated access have become a major bottleneck.

## 为什么值得关注

待编辑增强。

## 摘要原文

As large language models (LLMs) process increasingly long contexts, KV cache storage and repeated access have become a major bottleneck. Existing KV cache compression methods rely on predefined, fixed compression rules and are typically developed around either token eviction or merging. As a result, cache resources can neither flow freely across layers, heads, and context slots, nor be jointly allocated to balance local resolution and information coverage. Therefore, we propose GraceKV, a global approach for the allocation of resolution and coverage in KV cache compression, and formulate the compression process as a global resource allocation problem under a fixed cache budget. GraceKV treats each layer-KV head-slot combination as an atomic unit and builds a prototype tree. Leaf nodes correspond to token-level KV entries, while each internal node uses a single prototype to compress the KV space covered by its children. A set of non-overlapping nodes in the tree forms the representation of an atomic unit. Adding the root of a new tree expands information coverage, whereas splitting a selected node improves local resolution. All candidate actions compete globally for a shared cache budget. Finally, the nodes retained across all trees form the compressed KV cache. This process adaptively determines the allocation of cache resources among atomic units globally and the balance between resolution and coverage. GraceKV requires no additional training, and the entire compression and inference process is performed on the GPU. Systematic experiments across diverse long-context tasks and compression ratios show that GraceKV ranks first in 24 of 32 settings and remains robust up to 128-fold compression. These results validate the effectiveness of global budget allocation in coordinating information coverage and local resolution.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haolin Tian, Yuzhe Liu, Tonghan Wang
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
