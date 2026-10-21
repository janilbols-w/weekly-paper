---
title: "SAGE-HAP: Sustainability-Certified Agentic Communication and Computing at a Solar-Powered High-Altitude Platform"
description: "The solar-powered High-Altitude Platforms (HAP) can provide persistent communication and computing services beyond terrestrial coverage."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2610.27513) · [PDF](https://arxiv.org/pdf/2610.27513)

## 一句话摘要

The solar-powered High-Altitude Platforms (HAP) can provide persistent communication and computing services beyond terrestrial coverage.

## 为什么值得关注

待编辑增强。

## 摘要原文

The solar-powered High-Altitude Platforms (HAP) can provide persistent communication and computing services beyond terrestrial coverage. However, changing mission priorities, coupled resource demands, and uncertain solar supply complicate sustainable scheduling, while large language model proposals require independent feasibility checks. This paper proposes SAGE, a Sustainability-certified Agentic Ground-service Engine for a HAP. We formulate an energy-causal stochastic optimization problem incorporating semantic modes, multi-user interference, channel aging, essential platform loads, and battery stress. An agent translates operator intent into typed admission, mode, and grouping candidates, while deterministic convex refinement and an action shield verify resource and reserve feasibility using calibrated solar lower bounds before execution. Agent proposals and deterministic fallbacks share the same certification path. Residual-based forecasting and memory-assisted replanning close the control loop. We establish fixed-candidate convexity, reserve safety under calibrated solar coverage and bounded actuation error, and an online utility bound accounting for candidate-generation error. At nominal load, simulations show 2.38 percentage points higher completion and 5.27% greater useful-workload energy efficiency than energy-harvesting Lyapunov control. Under stressed load and solar uncertainty, reserve violations occur in 1/50 runs, versus 47/50 without energy certification. A 600-record calibrated inference replay further shows 23.5--36.5% utility gains over deterministic-only candidates under compound stress.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haoxiang Luo, Bang Huang, Mohamed-Slim Alouini
- 发布：2026-10-21；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
