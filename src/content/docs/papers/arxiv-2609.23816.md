---
title: "SPLASH: Co-Designing Sparse Attention with High-Bandwidth Flash for Efficient Long-Context Inference"
description: "The key-value (KV) cache has become the dominant consumer of memory in large language model (LLM) serving systems as context lengths, concurrency, and request lifetimes grow."
---

**评分：47/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.23816) · [PDF](https://arxiv.org/pdf/2609.23816)

## 一句话摘要

The key-value (KV) cache has become the dominant consumer of memory in large language model (LLM) serving systems as context lengths, concurrency, and request lifetimes grow.

## 为什么值得关注

待编辑增强。

## 摘要原文

The key-value (KV) cache has become the dominant consumer of memory in large language model (LLM) serving systems as context lengths, concurrency, and request lifetimes grow. High-bandwidth memory (HBM) provides the bandwidth attention decode needs but limited capacity, while off-package memory and storage add capacity but lack the bandwidth to sustain attention decode. High-Bandwidth Flash (HBF) is a promising substrate that combines terabyte-scale capacity with near-HBM read bandwidth. Limited write endurance makes read-only model weights its natural use, but we argue that HBF paired with HBM as a hierarchy can also hold the KV cache. Unlike prior hierarchies, whose secondary tiers are bandwidth bottlenecked, the comparable bandwidths let the two act as one logical memory for the long-context KV cache. HBF capacity enables long-context serving, and sparse attention makes it efficient by limiting KV-cache reads during memory-bound decode. Since HBF reads full flash pages and aggregates bandwidth by accessing thousands of parallel flash planes, sparse attention must be co-designed with these physical properties. We present SPLASH, an algorithm and architecture co-design that virtualizes the KV cache across HBM and HBF and adapts sparse attention to HBF's page granularity and plane-level parallelism. Across models and context lengths, SPLASH improves decode throughput per GPU by 3.5x-11.4x over the evaluated baselines under a 100 ms per-token latency objective, while keeping accuracy within 4% of dense attention across long-context suites.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Aditya Anirudh Jonnalagadda, Agasthi Haputhanthri, Pranav Dangi, Rohan Juneja, Wenshuo Yue, Aritra Bagchi, Bin Gao, Tulika Mitra
- 发布：2026-09-20；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
