---
title: "The Operable Pareto Front: Distilling Offline Search into Run-Time Control for Multi-Objective UAV Edge-Computing Scheduling"
description: "A UAV mobile edge computing (MEC) fleet trades energy against delay, and its schedules form a Pareto front; we call a scheduler operable when the fleet can be asked for any point on that front at run time."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2609.17992) · [PDF](https://arxiv.org/pdf/2609.17992)

## 一句话摘要

A UAV mobile edge computing (MEC) fleet trades energy against delay, and its schedules form a Pareto front; we call a scheduler operable when the fleet can be asked for any point on that front at run time.

## 为什么值得关注

待编辑增强。

## 摘要原文

A UAV mobile edge computing (MEC) fleet trades energy against delay, and its schedules form a Pareto front; we call a scheduler operable when the fleet can be asked for any point on that front at run time. We propose PrefDT, to the best of our knowledge the first preference-conditioned Decision Transformer for the problem of joint trajectory, association and offloading scheduling. Its idea comes from language modeling: we hand the model the desired trade-off as an input, such that a single model only needs to be trained once offline to return any desired point on the curve in one rollout. The fleet's state is summarized by attention pooling with a per-user bypass, so the scheduler keeps working when user reports are lost. The energy target is a running budget decremented by what the fleet actually spends. As a result, when wind or load pushes consumption off the plan, the policy can track the difference and hold its budget. Because no corpus of preference-labeled flights exists, we design a distillation pipeline and build the corpus by ourselves. In simulation against 26 method variants, PrefDT produces the best trade-off curve of any learned method and holds its energy budget to within 0.6% when propulsion cost rises by half in mid-flight.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qiao Liao, Zhiyong Feng, Bin Wu, Guodong Fan
- 发布：2026-09-17；更新：2026-09-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
