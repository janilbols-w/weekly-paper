---
title: "SpraySense: Sensing Gray Failures through Packet Spraying Discrepancies"
description: "Distributed machine learning (ML) training has become a dominant workload in modern data center networks, operating at massive scale with clusters comprising tens to hundreds of thousands of GPUs."
---

**评分：38/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2605.03702) · [PDF](https://arxiv.org/pdf/2605.03702)

## 一句话摘要

Distributed machine learning (ML) training has become a dominant workload in modern data center networks, operating at massive scale with clusters comprising tens to hundreds of thousands of GPUs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Distributed machine learning (ML) training has become a dominant workload in modern data center networks, operating at massive scale with clusters comprising tens to hundreds of thousands of GPUs. The scale of these networks makes failures, and particularly gray failures, inevitable. Gray failures can significantly degrade both network and application performance, yet they are notoriously difficult to detect, localize, and debug. To meet the performance demands of ML workloads, adaptive routing is widely deployed to maximize network utilization by dynamically spreading traffic across many paths. While adaptive routing increases network utilization, it also greatly intensifies the effect of gray failures. Prior work has either dismissed gray failures as negligible or proposed detection mechanisms that fail to scale, rendering these approaches increasingly impractical for large-scale clusters. We present SpraySense, a passive gray failure detection system that leverages the statistical properties of adaptive routing and network load balancing. By combining these properties with flow-level information, SpraySense can identify failures before they significantly impact application performance, enabling preemptive rerouting and improving overall performance. Importantly, this is achieved through passive observation of traffic spraying, without introducing additional load on the network. We evaluate SpraySense and show that it can detect and localize a single-link packet-drop-rate $1.5\%$ within a single iteration and as little as $0.5\%$ within 5 training iterations of Llama-3 70B in a 64 spine topology.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: load balancing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jakob Krebs, Daniel Amir, Shir Landau Feibish, Mark Silberstein
- 发布：2026-10-23；更新：2026-10-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
