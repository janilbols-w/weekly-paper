---
title: "Scalable Placement for Disaggregated LLM Serving on Heterogeneous Edge Fleets"
description: "Serving large language models (LLMs) at the edge is increasingly desirable for privacy-sensitive applications and scenarios that require data to remain on local devices."
---

**评分：42/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.32881) · [PDF](https://arxiv.org/pdf/2611.32881)

## 一句话摘要

Serving large language models (LLMs) at the edge is increasingly desirable for privacy-sensitive applications and scenarios that require data to remain on local devices.

## 为什么值得关注

待编辑增强。

## 摘要原文

Serving large language models (LLMs) at the edge is increasingly desirable for privacy-sensitive applications and scenarios that require data to remain on local devices. However, edge environments are constrained by limited computational resources and exhibit substantial device heterogeneity, making efficient LLM serving challenging. These limitations become particularly pronounced under bursty demand, where congestion and queue buildup can significantly increase response latency. Replicating the model into multiple pipeline instances can improve serving capacity and reduce congestion. Yet, deciding how devices should be grouped into replicas, assigning replicas to prefill or decode functions, and partitioning model layers across heterogeneous devices jointly creates a large combinatorial optimization problem. We present Spade, a scalable and runtime-efficient placement planner for disaggregated LLM serving with pipeline replication across heterogeneous edge clusters. Spade introduces a dominance-based pruning technique that discards inferior replica candidates and recursively eliminates larger candidates that contain them, dramatically shrinking the search space. It further combines a water-filling approach for layer partitioning with a bounded multidimensional knapsack formulation that optimizes placement under a congestion-aware objective. On a synthetic fleet of 30 devices spanning five hardware classes, Spade finds the optimal placement in 441ms. In contrast, a genetic-search baseline augmented with dynamic-programming partitioning requires approximately two hours and still produces solutions with a 19.7% worse congestion objective. When evaluated on fleets containing ten device types, Spade's pruning strategy eliminates 99.6% of candidate placements while yielding the same surviving candidate set as exhaustive enumeration.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Truong-Thanh Le, Hoang-Loc La, Amir Taherkordi, Frank Eliassen, Phuong Hoai Ha
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
