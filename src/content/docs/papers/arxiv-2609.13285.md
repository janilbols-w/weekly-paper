---
title: "Grouped Value Attention: Efficient KV Caching via On-Demand Key Reconstruction"
description: "The KV cache is a primary bottleneck for Transformer decoding: its memory footprint and cache-read traffic grow with sequence length."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.13285) · [PDF](https://arxiv.org/pdf/2609.13285)

## 一句话摘要

The KV cache is a primary bottleneck for Transformer decoding: its memory footprint and cache-read traffic grow with sequence length.

## 为什么值得关注

待编辑增强。

## 摘要原文

The KV cache is a primary bottleneck for Transformer decoding: its memory footprint and cache-read traffic grow with sequence length. Grouped-query attention (GQA) reduces this cost by sharing key-value heads, but still stores both a key and a value at every step. We introduce Grouped Value Attention (GVA), which stores grouped values and reconstructs content keys with a learned linear map. At inference, the map can be absorbed into the query, eliminating the need to materialize content keys in the intended decode path. A small shared decoupled RoPE channel retains positional information through a separately cached positional key. For the configurations studied, this representation reduces persistent cache scalars by approximately 45-47% relative to matched GQA. At the 350M-parameter scale with 30B FineWeb-Edu tokens, the 16-dimensional positional variant reaches 44.18 average accuracy across five tasks, compared with 44.36 for GQA and 43.88 for MLA. These results demonstrate near-GQA benchmark accuracy with a more compact cache representation. To translate this compact representation into faster autoregressive inference, we have developed custom decoding kernels and are currently evaluating their end-to-end inference performance with an open-source release planned soon.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Vishesh Tripathi, Abhay Kumar, Ramsha Khan
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
