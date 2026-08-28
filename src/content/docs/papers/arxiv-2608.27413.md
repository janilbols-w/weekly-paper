---
title: "Scaling Graph Neural Networks for Friend Recommendation: Multi-Hash User Embeddings and Temporal Neighbor Sampling"
description: "Friend recommendation is inherently graph-structured: the relevance of a potential connection depends on multi-hop social context rather than user attributes alone."
---

**评分：46/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2608.27413) · [PDF](https://arxiv.org/pdf/2608.27413)

## 一句话摘要

Friend recommendation is inherently graph-structured: the relevance of a potential connection depends on multi-hop social context rather than user attributes alone.

## 为什么值得关注

待编辑增强。

## 摘要原文

Friend recommendation is inherently graph-structured: the relevance of a potential connection depends on multi-hop social context rather than user attributes alone. However, deploying message-passing GNNs on a production-scale social graph with hundreds of millions of users and tens of billions of edges requires addressing numerous modeling and systems challenges. We present a scalable end-to-end GNN ranking system for production social graphs, focusing on two design choices that are critical in this setting: multi-hash ID embeddings and temporal neighbor sampling. Multi-hash embeddings are common for high-cardinality features, but industrial GNN systems typically either ignore trainable IDs or accept full embedding tables, exceeding 200 GB for our graph. We integrate multi-hash as the primary node representation, reducing the ID-embedding table size by more than 98 percent while preserving ranking quality. Temporal neighbor sampling is well understood in principle, but existing implementations scan full adjacency lists, which is a non-starter for users with tens of thousands of friends. We implement timestamp-sorted CSR storage with binary search, reducing the per-node temporal sampling cost from $O(deg(v) + k)$ to $O(\log(deg(v)) + k)$. Beyond these components, we show that this combination scales and yields measurable production impact. On a graph with 194M users and 28B edges, offline ablations isolate each design choice's contribution. In an online A/B test, our system increases friend additions from recommendations by 16 percent and unique friend adders by 11.5 percent over a strong production baseline. We release our framework for distributed training and inference on large temporal graphs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distributed training
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Maksim Utushkin, Andrei Ovsiannikov, Alexander D'yakonov
- 发布：2026-08-27；更新：2026-08-28
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/makut/VK-GNN](https://github.com/makut/VK-GNN)
- 阅读深度：metadata
