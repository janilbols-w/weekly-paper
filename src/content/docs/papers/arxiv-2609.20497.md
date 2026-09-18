---
title: "A Kubernetes-Native Request Router for Quality-Aware Inference Serving in the Computing Continuum"
description: "We introduce Adaptive Score-based Routing Balancer (ASRB), a dynamic, score-based request routing mechanism for Kubernetes-based service deployments over the computing continuum."
---

**评分：41/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2609.20497) · [PDF](https://arxiv.org/pdf/2609.20497)

## 一句话摘要

We introduce Adaptive Score-based Routing Balancer (ASRB), a dynamic, score-based request routing mechanism for Kubernetes-based service deployments over the computing continuum.

## 为什么值得关注

待编辑增强。

## 摘要原文

We introduce Adaptive Score-based Routing Balancer (ASRB), a dynamic, score-based request routing mechanism for Kubernetes-based service deployments over the computing continuum. ASRB jointly considers infrastructure-level information, response time measurements, and application-level quality indicators, with a particular focus on serving Machine Learning (ML) workloads. For these workloads, ASRB balances requests over service instances deployed in the continuum, following service provider-defined policies encoded as weighted combinations of QoS criteria to flexibly address latency-accuracy trade-offs. To drive routing decisions and swiftly adapt to changes in the operating environment, ASRB monitors a range of runtime metrics across multiple system layers. To deal with the associated monitoring overhead, particularly important for large-scale deployments, it selectively and adaptively controls monitoring intensity without sacrificing on routing quality. ASRB is implemented without requiring any modifications to Kubernetes, making it straightforward to deploy and operate in existing cluster environments. Our testbed experiments demonstrate the versatility of ASRB: When tuned for latency reduction, it achieves at least 10 ms lower mean response time compared with latency-oriented state-of-the-art routing mechanisms, while it achieves higher accuracy when this is prioritized through specific configurations, thus enabling flexible and operator-controllable trade-offs. At the same time, it attains reduced failure rates, higher responsiveness to changes in the operating environment, and up to ~70% less monitoring cost than relevant state-of-the-art solutions, at the potential expense of only a modest latency penalty in some configurations.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: request routing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ignjat Karanovic, Pantelis A. Frangoudis, Ivan Čilić, Ivana Podnar Žarko, Schahram Dustdar
- 发布：2026-09-17；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
