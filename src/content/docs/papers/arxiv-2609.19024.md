---
title: "OAK: Restart- and Age-Aware Scheduling for Distributed Machine Learning on Shared GPU Clusters"
description: "Distributed machine learning increasingly runs on shared multi-tenant GPU clusters where contention and failures are routine."
---

**评分：45/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.19024) · [PDF](https://arxiv.org/pdf/2609.19024)

## 一句话摘要

Distributed machine learning increasingly runs on shared multi-tenant GPU clusters where contention and failures are routine.

## 为什么值得关注

待编辑增强。

## 摘要原文

Distributed machine learning increasingly runs on shared multi-tenant GPU clusters where contention and failures are routine. Goodput-driven schedulers maximise instantaneous throughput but treat accumulated waiting time and restart cost as second-class signals: long-waiting jobs are repeatedly deferred, and the minutes of checkpoint loading paid after each interruption are not folded back into allocation decisions. We present OAK, a per-round mixed-integer linear scheduler whose composite utility adds two first-class terms to goodput: an age key that elevates jobs with high cumulative waiting time, and a decomposed restart factor that tracks productive training time and checkpoint overhead as separately measured quantities rather than a single aggregate ratio. We evaluate OAK against four representative goodput- and fairness-driven baselines in a trace-driven simulator on a 12-GPU cluster across four data-parallel workloads with controlled Poisson failure injection, and reproduce the failure-mode improvement on a 4-V100 real-hardware cluster. Under failure-free conditions OAK matches the strongest goodput-driven baseline within 4%. Under failures at rate $\lambda = 0.1$ it reduces mean job completion time (JCT) by 33.9-58.3% and worst-case JCT by 58-76% over its goodput-driven foundation; the decomposed restart factor alone accounts for a 40-57% mean and 52-76% tail JCT improvement against an aggregate restart estimator used in prior goodput-driven schedulers. Per-round decision latency is 7.65 ms, three orders of magnitude faster than evolutionary-search alternatives at default settings.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Khaled Aljbab, Amine Barrak
- 发布：2026-09-17；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
