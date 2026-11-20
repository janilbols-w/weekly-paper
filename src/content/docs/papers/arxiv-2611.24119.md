---
title: "eFAIR: Fair LLM Serving under Hourly Electricity Commitments"
description: "Datacenters can procure electricity in day-ahead markets by committing to energy purchases for individual hours."
---

**评分：44/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.24119) · [PDF](https://arxiv.org/pdf/2611.24119)

## 一句话摘要

Datacenters can procure electricity in day-ahead markets by committing to energy purchases for individual hours.

## 为什么值得关注

待编辑增强。

## 摘要原文

Datacenters can procure electricity in day-ahead markets by committing to energy purchases for individual hours. For LLM services operating within these hourly budgets, maximizing aggregate throughput alone may still leave individual requests waiting or receiving much slower service than desired. Fair serving therefore requires improving service for poorly served requests while reserving electricity for later arrivals whose timing and demand are unknown. To compare service across requests, we define normalized throughput as each request's actual output rate divided by the product of its standalone throughput and its service entitlement, a positive weight representing its desired service level. Using this measure, we formulate fair serving as leximin optimization under an hourly electricity constraint, prioritizing requests with the lowest normalized throughput. To address this problem, we present eFAIR, an online scheduler that coordinates request dispatching, electricity budget allocation, and GPU frequency selection through a common normalized-throughput target. Specifically, request dispatching prioritizes requests by desired service level and progress; electricity budget allocation reserves electricity for current and expected future work; and frequency selection uses electricity savings to raise GPU frequencies for requests with higher desired service levels. Evaluations on H20 and H200 configurations, each with 32 replicas, show that eFAIR improves the tenth percentile of normalized throughput by 28.0%-31.0% over the best budget-feasible baseline, while keeping absolute deviations from the hourly electricity commitment below 0.26%. eFAIR also improves throughput balance among concurrent requests and aligns electricity allocation more closely with service demand over time. Together, these results demonstrate how eFAIR improves request-level fairness within an hourly commitment.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：You Peng, Youhe Jiang, Chen Wang, Binhang Yuan
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
