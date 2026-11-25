---
title: "RefineKV: Query-Adaptive KV Cache Compression via Attention-Error Bounds"
description: "Repeatedly accessing the full key--value (KV) cache is a major bottleneck in long-context language model decoding."
---

**评分：48/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.28171) · [PDF](https://arxiv.org/pdf/2611.28171)

## 一句话摘要

Repeatedly accessing the full key--value (KV) cache is a major bottleneck in long-context language model decoding.

## 为什么值得关注

待编辑增强。

## 摘要原文

Repeatedly accessing the full key--value (KV) cache is a major bottleneck in long-context language model decoding. We find that small query-specific subsets can accurately approximate full attention, yet their union covers nearly the entire cache, motivating query-adaptive access for the KV cache. A natural approach is to split the KV cache into clusters, using compact representatives for clusters that incur negligible error while expanding the rest to their original KV entries. We derive a selection criterion from an upper bound on attention-output error, which reveals two complementary factors governing the error: importance measures the impact of a cluster, while distortion measures how faithfully the cluster can be represented. Based on this criterion, we propose RefineKV, a decoding-time query-adaptive KV compression method. Experiments on two models and three benchmarks demonstrate that RefineKV retains near-full-attention quality while achieving up to 7.6x speedup in the attention phase and 1.66x faster decoding, establishing a new quality-latency Pareto frontier.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Kewei Lian, Jiayi Zhai, Anji Liu
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
