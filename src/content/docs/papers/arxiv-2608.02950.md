---
title: "Schedule-Informed Temporal Fusion Forecasting of Hourly Airport Security-Checkpoint Throughput"
description: "Checkpoint staffing requires accurate forecasts of when screening demand will occur, yet flight schedules record departure times rather than passenger arrival times at security checkpoints."
---

**评分：42/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2608.02950) · [PDF](https://arxiv.org/pdf/2608.02950)

## 一句话摘要

Checkpoint staffing requires accurate forecasts of when screening demand will occur, yet flight schedules record departure times rather than passenger arrival times at security checkpoints.

## 为什么值得关注

待编辑增强。

## 摘要原文

Checkpoint staffing requires accurate forecasts of when screening demand will occur, yet flight schedules record departure times rather than passenger arrival times at security checkpoints. This study develops a framework that converts known flight schedules into temporally aligned signals for forecasting hourly checkpoint throughput. Using 2023-2024 Transportation Security Administration throughput data and Cirium Diio flight schedules for Hartsfield-Jackson Atlanta International Airport, domestic and international seat capacity was distributed across pre-departure hours using truncated Poisson kernels. A Temporal Fusion Transformer then combined these schedule-derived arrival-intensity signals with historical throughput, scheduled activity, and temporal variables. Models were trained chronologically, with July-December 2024 reserved for testing, and evaluated against recurrent neural network and long short-term memory models across five random seeds. For direct six-hour forecasts, the proposed model achieved a weighted mean absolute percentage error of 9.33%, compared with 12.16% for the recurrent neural network and 11.37% for long short-term memory, while also producing the lowest errors during peak periods. With six-hour recursive updates, errors remained between 10.60% and 11.04% across 24-96 hour horizons, although longer horizons contained fewer valid forecast origins. By transforming scheduled departures into interpretable pre-departure screening-load signals without requiring passenger-flight matching, the framework supports advance staffing, lane-opening, and multiday checkpoint planning. Because observed throughput reflects realized processing rather than unconstrained arrivals, the forecasts should be interpreted together with local staffing, capacity, queue, and wait-time information.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yinxiao Zhang, Sen Wang, Yi Gao
- 发布：2026-08-05；更新：2026-08-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
