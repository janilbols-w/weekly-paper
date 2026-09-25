---
title: "Speculative Evaluation of Stochastic LLMs"
description: "Evaluating a stochastic large language model is costly: benchmark scores estimate expected performance from randomized rollouts, yet uniform repetition ignores sharp differences in task-level rollout variance."
---

**评分：44/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.28560) · [PDF](https://arxiv.org/pdf/2609.28560)

## 一句话摘要

Evaluating a stochastic large language model is costly: benchmark scores estimate expected performance from randomized rollouts, yet uniform repetition ignores sharp differences in task-level rollout variance.

## 为什么值得关注

待编辑增强。

## 摘要原文

Evaluating a stochastic large language model is costly: benchmark scores estimate expected performance from randomized rollouts, yet uniform repetition ignores sharp differences in task-level rollout variance. We ask how to minimize the variance of a fixed-benchmark mean under an exact rollout budget. We develop Speculative Evaluation with a Hierarchical Bayesian Neyman (HBN) policy with pilot size and stage weight jointly chosen ex ante. It runs a short uniform pilot, pools per-task success counts with a hierarchical Bayesian model, and uses posterior expectations of task-level sampling variances for exact positive-integer Neyman allocation. To mitigate the pilot synchronization barrier, HBN-async speculatively executes continuations from partial pilot feedback and retains those selected by the final allocation. Across six checkpoints and 18 benchmark groups, we evaluate 107 nondegenerate benchmark-checkpoint profiles. For rollout budgets of 8-64 per task, Speculative Evaluation reduces variance relative to Uniform by 12.8%-33.6% on average across profiles, outperforming hindsight-tuned empirical and independent Bayesian baselines. Real-generation experiments that account for the pilot synchronization barrier show that HBN-async mitigates its overhead, helping translate statistical efficiency into practical evaluation benefits.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 15 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qianli Shen, Xiang Li, Ruomeng Ding, Yanxi Chen, Daoyuan Chen, Yaliang Li
- 发布：2026-09-23；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
