---
title: "User-Assisted Collaborative Distributed Inference for Efficient QoS-Aware Autoscaling"
description: "Growing demand for artificial intelligence (AI) inference services requires scalable infrastructure, yet centralized serving costs rise with demand."
---

**评分：45/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2608.11840) · [PDF](https://arxiv.org/pdf/2608.11840)

## 一句话摘要

Growing demand for artificial intelligence (AI) inference services requires scalable infrastructure, yet centralized serving costs rise with demand.

## 为什么值得关注

待编辑增强。

## 摘要原文

Growing demand for artificial intelligence (AI) inference services requires scalable infrastructure, yet centralized serving costs rise with demand. We propose a collaborative distributed inference system combining dedicated infrastructure with resources contributed by service users. Dedicated resources provide baseline capacity for maintaining quality of service (QoS), while volunteered resources absorb increasing demand without proportional growth in centralized infrastructure. To capture stochastic and dynamic interactions among users, resources, tasks, and policies, we develop a high-dimensional generative Markov model with structured temporal factorization. The model supports simulation and provides a foundation for task scheduling and QoS-aware resource allocation optimization. We evaluate the system across user populations, resource capacities, and centralized and distributed scheduling policies. Simulations show that distributed scheduling becomes increasingly advantageous as the user population grows, improving request completion and P99 latency while substantially reducing dedicated resource consumption. These results demonstrate the feasibility of user-assisted collaborative inference for infrastructure-efficient autoscaling.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: autoscaling
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Alfreds Lapkovskis, Ali Beikmohammadi, Sindri Magnússon, Praveen Kumar Donta
- 发布：2026-08-12；更新：2026-08-13
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
