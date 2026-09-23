---
title: "PRISM: Probabilistic Runtime Insights and Scalable Performance Modeling for Large-Scale Distributed Training"
description: "Large model training beyond tens of thousands of GPUs is an uncharted territory."
---

**评分：42/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2510.15596) · [PDF](https://arxiv.org/pdf/2510.15596)

## 一句话摘要

Large model training beyond tens of thousands of GPUs is an uncharted territory.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large model training beyond tens of thousands of GPUs is an uncharted territory. At such scales, disruptions to the training process are not a matter of if, but a matter of when -- a stochastic process degrading training productivity. Dynamic runtime variation will become increasingly more frequent as training scales and GPUs are operated in increasingly power-limited and thermally-stressed environments. At the 64,000+ GPU scale, we already observe 12% variability for frontier foundation model training. Motivated by our analysis and the large design space around performance variability, we present PRISM -- a performance modeling framework that captures the stochastic nature of large-scale distributed training. The core of PRISM is a statistical model that composes operator-level latency distributions through workload dependencies. Across 14 diverse training configurations spanning hundreds to 64K+ GPUs, PRISM estimates p95 execution time within 5.4% error. Using PRISM, we explore the design and optimization space of distributed training, enabling principled, variability-aware recommendations that can improve performance and system efficiency at scale.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distributed training, large model training
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Alicia Golden, Michael Kuchnik, Samuel Hsia, Zachary DeVito, Gu-Yeon Wei, David Brooks, Carole-Jean Wu
- 发布：2026-09-23；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
