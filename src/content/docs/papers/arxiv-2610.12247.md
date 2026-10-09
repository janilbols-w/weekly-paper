---
title: "Batch Before You Lift: Scalable Topological Deep Learning on Large Graphs"
description: "Topological Deep Learning extends graph-based learning to higher-order domains, such as hypergraphs, cellular, and simplicial complexes."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.12247) · [PDF](https://arxiv.org/pdf/2610.12247)

## 一句话摘要

Topological Deep Learning extends graph-based learning to higher-order domains, such as hypergraphs, cellular, and simplicial complexes.

## 为什么值得关注

待编辑增强。

## 摘要原文

Topological Deep Learning extends graph-based learning to higher-order domains, such as hypergraphs, cellular, and simplicial complexes. These domains are typically constructed from patterns in an input graph through a process of graph lifting. Full-domain training constructs and stores the complete lifted representation before model execution. On large and dense datasets like Reddit (233k nodes and 57.3M edges), this global materialization becomes a severe computational bottleneck, often rendering training infeasible. To address this limitation, we introduce Cluster-TNN, a domain-agnostic framework that avoids this bottleneck by lifting locally instead. After partitioning the input graph during preprocessing, at runtime Cluster-TNN dynamically samples groups of node clusters, reconstructs their induced subgraphs to form mini-batches, and applies the chosen lifting within each mini-batch. Retaining all edges among sampled nodes preserves the connectivity needed to construct higher-order structures across clusters, producing topological mini-batches that existing Topological Neural Networks can process directly. Across 21 matched comparisons with full-graph execution, Cluster-TNN reduces peak GPU memory in every configuration, by 83.2% on average while maintaining competitive predictive performance. Notably, such a reduction enables, to our knowledge, the first training of multiple different higher-order Topological Neural Networks on large datasets such as Reddit and OGBN Products. These results establish Cluster-TNN as a general strategy for scaling Topological Deep Learning beyond the limitations of global domain construction.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：David Leko, Luka Beni\'c, Guillermo Bern\'ardez, Nina Miolane, Olga Fink, Lev Telyatnikov
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
