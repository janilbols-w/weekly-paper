---
title: "DepTGL: A Parallel Framework for Memory-based TGNN Training with Adaptive Temporal Data Dependency Management"
description: "Memory-based Temporal Graph Neural Networks (M-TGNNs) maintain recursively updated node states to capture fine-grained temporal interactions."
---

**评分：45/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2608.16305) · [PDF](https://arxiv.org/pdf/2608.16305)

## 一句话摘要

Memory-based Temporal Graph Neural Networks (M-TGNNs) maintain recursively updated node states to capture fine-grained temporal interactions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Memory-based Temporal Graph Neural Networks (M-TGNNs) maintain recursively updated node states to capture fine-grained temporal interactions. However, existing distributed frameworks lack effective mechanisms for managing the temporal data dependencies inherent in these models. As a result, they must enforce strict chronological updates, incur substantial remote synchronization overhead, and experience severe load imbalance when temporal event streams are skewed. We propose DepTGL, a scalable distributed training framework that restructures temporal-dependency management for M-TGNNs from a data-centric perspective. First, DepTGL introduces a hybrid temporal-dependency management scheme that explicitly balances communication and caching overhead via temporal-event caching, supplemented by selective dependency-driven communication. Next, DepTGL incorporates a gradient-aware cache-synchronization policy that adaptively suppresses boundary updates as model optimization stabilizes, thereby reducing redundant synchronization. Finally, DepTGL integrates a load-aware temporal-pruning strategy that eliminates auxiliary replay events under skew-induced load spikes, reducing redundant data processing and mitigating straggler effects. Experiments on six real-world temporal graphs show that DepTGL achieves an average speedup of 4.99x over state-of-the-art baselines, while maintaining comparable accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distributed training
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Linfang Chen, Zhen Song, Lei Liu, Yu Gu, Yushuai Li, Yanfeng Zhang, Lizhen Cui, Ge Yu, Tianyi Li
- 发布：2026-08-17；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
