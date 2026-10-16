---
title: "Truthful and Expected-Payment-Optimal Model Routing in Graph-Based Agentic Workflows"
description: "Assigning routine tasks to cheaper large language model (LLM) providers can reduce generation cost, but switching providers may require processing accumulated context again."
---

**评分：42/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2610.19316) · [PDF](https://arxiv.org/pdf/2610.19316)

## 一句话摘要

Assigning routine tasks to cheaper large language model (LLM) providers can reduce generation cost, but switching providers may require processing accumulated context again.

## 为什么值得关注

待编辑增强。

## 摘要原文

Assigning routine tasks to cheaper large language model (LLM) providers can reduce generation cost, but switching providers may require processing accumulated context again. Keeping dependent tasks with the same provider can instead reuse eligible context. Graph-based workflows therefore couple routing decisions across tasks. Independent providers may also privately know their real-time unit costs and strategically misreport them. We formulate this routing problem as a single-parameter procurement auction and propose STAR (Strategy-proof Topology-aware Agent Routing), which minimizes virtual-cost-weighted graph workloads. Its allocation rule and payments, computed by integrating workload over possible cost reports, make truthful reporting utility-maximizing regardless of other providers' reports and cover each truthful provider's execution cost. With independent cost distributions and non-decreasing virtual costs, STAR additionally minimizes the user's expected total payment to providers. Controlled synthetic experiments separate the execution-cost benefit of topology awareness from the payment benefit of virtual-cost optimization: the former grows with fan-out and transferred payload, while the latter increases gradually along the tested prior-shape heterogeneity path. A paired sensitivity study quantifies how payment savings vary with prior misspecification while strategy-proofness is preserved.

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

- taxonomy keywords: model routing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiayuan Liu, Mingyu Guo, Jiarui Gan, Vincent Conitzer
- 发布：2026-10-13；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
