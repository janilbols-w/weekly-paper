---
title: "Two-Layer Evolutionary Scheduling for Machine Learning Jobs in Multi-Cluster Environments"
description: "The rapid growth of large-scale machine learning (ML) workloads has led to unprecedented demands on GPU cluster scheduling systems."
---

**评分：43/100** · AI 基础设施 > 集群与资源系统 > GPU 调度与虚拟化

[论文原文](https://arxiv.org/abs/2611.09093) · [PDF](https://arxiv.org/pdf/2611.09093)

## 一句话摘要

The rapid growth of large-scale machine learning (ML) workloads has led to unprecedented demands on GPU cluster scheduling systems.

## 为什么值得关注

待编辑增强。

## 摘要原文

The rapid growth of large-scale machine learning (ML) workloads has led to unprecedented demands on GPU cluster scheduling systems. However, existing heuristic schedulers struggle to handle the complexity and dynamics of multi-cluster GPU environments, often leading to load imbalance, long queuing delays, and poor alignment to business objectives. This paper formulates the ML scheduling problem in multi-cluster GPU environments as online multi-objective optimization that minimizes the average and maximum weighted queuing times while maximizing GPU time utilization. To solve this optimization problem, we propose EVO-GP, a two-layer evolutionary online scheduling method that decouples global job-to-cluster allocation from intra-cluster GPU resource allocation. At the job-to-cluster allocation layer, an evolutionary algorithm assigns arriving jobs to feasible clusters to promote load balance across clusters. At the resource allocation layer, a priority function automatically learned offline via genetic programming is used to rank jobs and guide GPU allocation within each cluster. Extensive experiments on both real-world data and simulated workloads demonstrate that the proposed EVO-GP method consistently outperforms state-of-the-art baselines, while maintaining superior adaptability and scalability.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: cluster scheduling
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jingyuan Xu, Changwu Huang, Lemeng Pan, Ke Tang, Xin Yao
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
