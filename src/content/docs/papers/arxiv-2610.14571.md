---
title: "Dissecting the Carbon-SLO Tension in Geo-Distributed LLM Serving"
description: "Large Language Model (LLM) inference is driving a growing share of datacenter carbon emissions."
---

**评分：45/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](http://arxiv.org/abs/2610.14571v1) · [PDF](https://arxiv.org/pdf/2610.14571v1)

## 一句话摘要

Large Language Model (LLM) inference is driving a growing share of datacenter carbon emissions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Model (LLM) inference is driving a growing share of datacenter carbon emissions. Although carbon-aware scheduling can reduce these emissions in geo-distributed datacenters by exploiting the spatiotemporal variations in grid carbon intensity, the latency-sensitive nature of LLM serving constrains this design space. While prior studies investigate the carbon savings achievable through spatial scheduling, they oversimplify the dynamics of modern inference engines, such as queueing and continuous batching, which strongly shape inference latency. We address this issue by designing and evaluating a latency-centric, geo-distributed inference simulator, calibrated with hardware-grounded latency and power measurements, that reproduces these dynamics and enables the study of carbon savings under strict service-level objectives (SLOs). We then formulate a series of SLO- and carbon-aware schedulers of increasing sophistication, from per-request heuristics to batch-level optimization: (i) a greedy heuristic, (ii) an integer linear programming (ILP)-based scheduler jointly assigning batches of requests, (iii) an iterative ILP-based solution projecting its own assignments back into the load estimates to capture load coupling, and (iv) a facility mixed-integer linear programming (MILP) scheduler pricing the energy of batched requests collectively rather than in isolation. Across three LLMs under MLPerf SLOs and varying system loads, the MILP-based option offers the best carbon-SLO balance, reducing carbon emissions by up to 60% relative to the round-robin policy, with an average SLO violation of 3%. Our characterization further shows that savings grow with the spread of carbon intensity across datacenters and shrink as system load increases, while SLO attainment depends on how frequently schedulers receive datacenters' load updates.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: slo
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Burak Topcu, Musa Cim, Zuhal Ozturk, Mahmut Taylan Kandemir
- 发布：2026-10-10；更新：2026-10-10
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/topcuburak/carbon-slo-at-geoscale](https://github.com/topcuburak/carbon-slo-at-geoscale)
- 阅读深度：metadata
