---
title: "CoordRoute: Coordinated Multi-Model Routing for Maximum Compute-Budget Utility"
description: "Model routing sends each request to one of several large language models (LLMs) of different sizes."
---

**评分：38/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2611.34161) · [PDF](https://arxiv.org/pdf/2611.34161)

## 一句话摘要

Model routing sends each request to one of several large language models (LLMs) of different sizes.

## 为什么值得关注

待编辑增强。

## 摘要原文

Model routing sends each request to one of several large language models (LLMs) of different sizes. In practice, requests share a fixed compute budget: a spending cap on rented model APIs or the capacity of a private GPU cluster. Most existing routers do not account for the total budget: each decides a request on its own, so per-request optima are not optimal overall. We advocate coordinated routing, which allocates the budget across requests to maximize its utility, their total satisfaction, along a predict-plan-rectify route: predict what each model would give and cost, plan the choice against later requests, and rectify it during generation. Each step faces a challenge: a request's gain from each model is uncertain before generation, later arrivals are unknown when a request must start, and observing answers during generation consumes the budget itself. CoordRoute addresses them with relative demand prediction, which compares candidate models through past requests that lead to the same routing choices; a lookahead solver, which charges each choice for what its compute could earn for later requests; and budget-aware runtime correction, which drops or upgrades in-flight requests at the same price, inspecting answers only when it pays off. On Azure Conversation and BurstGPT traces, CoordRoute improves total satisfaction by 18.72% over the strongest existing router.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: model routing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Boning Huangfu, Boxiao Du, Chen Chen
- 发布：2026-11-25；更新：2026-11-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
