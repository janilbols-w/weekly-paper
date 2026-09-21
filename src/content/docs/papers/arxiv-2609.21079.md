---
title: "DLB: Distributed Load Balancing at Scale for Generative AI Inference"
description: "The reliance on scarce and expensive accelerators such as GPUs and TPUs in modern datacenters places unprecedented demands on backend infrastructure."
---

**评分：47/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2609.21079) · [PDF](https://arxiv.org/pdf/2609.21079)

## 一句话摘要

The reliance on scarce and expensive accelerators such as GPUs and TPUs in modern datacenters places unprecedented demands on backend infrastructure.

## 为什么值得关注

待编辑增强。

## 摘要原文

The reliance on scarce and expensive accelerators such as GPUs and TPUs in modern datacenters places unprecedented demands on backend infrastructure. For workloads characterized by heterogeneous service times and complex multi-stage processing, such as Generative AI, conventional load balancing techniques are often inadequate, relying heavily on costly overprovisioning to maintain service level objectives. This paper introduces DLB, the Distributed Load Balancer, a novel system designed to minimize end-to-end user latency for large-scale, heterogeneous workloads. DLB employs a scalable, distributed design with peer-to-peer probing to maintain real-time visibility into server capacity across large-scale, geographically distributed infrastructure. The system continuously learns latency models to estimate the latency impact of routing decisions, allowing it to effectively manage heterogeneous hardware and diverse model architectures. We provide a novel theoretical analysis of our routing algorithms that establishes their stability and global performance guarantees over time. We also evaluate DLB through extensive simulations, which show substantial gains compared to state-of-the-art load balancing algorithms. Finally, following a 22-month deployment of DLB at Google, where it facilitates large-scale Generative AI inference for thousands of different machine learning models and millions of requests per second, we detail the design choices and practical experiences gained from the system in production. Analysis of production migrations demonstrates that DLB yields statistically significant latency reductions compared to the legacy baseline, including a 17\% decrease in median latency and a 13\% decrease at the p95 tail.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: load balancing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Santiago R. Balseiro, Bartek Wydrowski, Sameer Agarwal, David Applegate, Aaron Archer, Soheil Hassas Yeganeh, Alex Iriza, Bobby Kleinberg, Balasubramanian Sivan, Pranav Vaish, Oscar Zegarra, Wenxin Zhang, Vahab Mirrokni, Amin Vahdat
- 发布：2026-09-21；更新：2026-09-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
