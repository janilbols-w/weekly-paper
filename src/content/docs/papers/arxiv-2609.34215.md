---
title: "Same Winners, Different Success Rates: Evaluating How LLM Agents Recover from Failures"
description: "Evaluating how LLM agents recover from mid-task failures is central to deploying reliable agentic systems."
---

**评分：42/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.34215) · [PDF](https://arxiv.org/pdf/2609.34215)

## 一句话摘要

Evaluating how LLM agents recover from mid-task failures is central to deploying reliable agentic systems.

## 为什么值得关注

待编辑增强。

## 摘要原文

Evaluating how LLM agents recover from mid-task failures is central to deploying reliable agentic systems. Existing checkpoint-based benchmarks measure recovery by comparing which action is selected as best across independent runs, a quantity known as set agreement. However, set agreement is a purely ordinal measure that records which action wins without reflecting the absolute level of performance. When all actions fail, they tie at zero reward, and independent runs produce the same tied set with high probability, creating an illusion of stability that masks near-zero recovery success. We formalize this limitation through a set-path symmetry result, proving that for equal-cost Bernoulli actions the success probabilities (0.9, 0.8) and (0.2, 0.1) yield identical best-action-set distributions at every sample size. No procedure based solely on which action wins can distinguish these two regimes. We further prove that certifying exact population ties is impossible in finite time, and that the assignment of outcomes to checkpoints carries information beyond marginal outcome distributions. The pooled success probability is the missing scalar that resolves the ordinal ambiguity. Experiments on 864 frozen RecoveryBench episodes and two planning cohorts totaling 3,456 responses confirm the theoretical predictions. Agreement and held-out quality can move in opposite directions, and permuting checkpoint-to-action bindings changes 8 to 13 percent of cell-level conclusions. Based on these findings, we propose reporting four diagnostic quantities (agreement, all-zero fraction, held-out success, and pooled success) that expose this failure mode with no additional data collection.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Dong Xu, Zhangfan Yang, Jiantao Wu, Shipeng Zhang, Zexuan Zhu, Jiangqiang Li, Jun Zhang, Junkai Ji
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
