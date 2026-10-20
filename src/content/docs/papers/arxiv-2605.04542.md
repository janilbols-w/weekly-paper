---
title: "Power Distribution Bridges Sampling, Self-Reward RL, and Self-Distillation"
description: "Recent analyses question whether reinforcement learning (RL) is responsible for strong reasoning in large language models (LLMs)."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.04542) · [PDF](https://arxiv.org/pdf/2605.04542)

## 一句话摘要

Recent analyses question whether reinforcement learning (RL) is responsible for strong reasoning in large language models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent analyses question whether reinforcement learning (RL) is responsible for strong reasoning in large language models (LLMs). At the same time, distillation and inference-time sampling, including power sampling, have emerged as effective ways to improve LLM performance. However, the relationship among RL, distillation, and sampling remains unclear. In this study, we focus on the power distribution, the target distribution of power sampling, and show that the power distribution bridges sampling, self-reward KL-regularized RL, and self-distillation. From the sampling perspective, we show that inexpensive local approximations cannot reproduce sequence-level power without information about possible suffixes. From the RL perspective, the power distribution is the closed-form optimizer of KL-regularized RL when the model's sequence-level log-probabilities are used as the reward. This identification leads to power self-distillation, an offline distillation surrogate that shares the same target distribution and amortizes the cost of power sampling into supervised training on teacher samples. We further show that power self-distillation can achieve self-reward sharpening, that downstream true-reward gains are governed by the covariance between true reward and self-reward under the power distribution, and that this ideal power-teacher gain transfers to a distilled student when the student is close to the power teacher. Experiments on reasoning tasks support our analysis: power sampling raises self-reward, true-reward gains depend on alignment with self-reward, and power self-distillation can match or exceed the performance of power sampling at much lower inference cost. The code is available at https://github.com/tom4649/power-self-distillation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Akiyoshi Tomihari, Issei Sato
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/tom4649/power-self-distillation](https://github.com/tom4649/power-self-distillation)
- 阅读深度：metadata
