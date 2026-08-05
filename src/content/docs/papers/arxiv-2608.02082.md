---
title: "Energy-Latency Trade-offs in O-RAN with Distributed Baseband Processing and AI Inference"
description: "The Open Radio Access Network (O-RAN) architecture introduces flexible functional splits and open interfaces that enable distributed and centralized deployment of baseband processing."
---

**评分：44/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2608.02082) · [PDF](https://arxiv.org/pdf/2608.02082)

## 一句话摘要

The Open Radio Access Network (O-RAN) architecture introduces flexible functional splits and open interfaces that enable distributed and centralized deployment of baseband processing.

## 为什么值得关注

待编辑增强。

## 摘要原文

The Open Radio Access Network (O-RAN) architecture introduces flexible functional splits and open interfaces that enable distributed and centralized deployment of baseband processing. While this flexibility offers opportunities for improved resource utilization, it also introduces fundamental trade-offs between energy efficiency and latency. In this paper, we develop a throughput-based end-to-end energy consumption model for O-RAN and extend it by incorporating detailed latency modeling and application-specific Artificial Intelligence/Machine Learning inference costs. The proposed end-to-end modeling framework provides a general representation of processing, transport, and inference-related energy and delay across the access, metro, and long-haul network segments. Building on this general model, we formulate an optimization problem that selects the placement of baseband processing and AI inference tasks across candidate O-RAN configurations to analyze energy-latency tradeoffs under network load, server frequency, and energy-budget constraints. Using representative hardware platforms and realistic traffic assumptions, we evaluate multiple baseband processing placements corresponding to different O-RAN functional configurations. Our results reveal how user quality of service requirements and network load conditions jointly determine the optimal placement of baseband processing and AI inference tasks, highlighting the inherent trade-off between energy efficiency and latency. The analysis provides practical insights for latency-aware and energy-efficient O-RAN deployments supporting emerging AI-driven services.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 15 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Urooj Tariq, Rishu Raj, Shashi Raj Pandey, Merim Dzaferagic, Petar Popovski, Dan Kilper
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
