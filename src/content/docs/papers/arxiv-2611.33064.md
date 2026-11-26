---
title: "U-Statistics-Powered LLM Reasoning"
description: "Since its introduction by DeepSeek, group relative policy optimization (GRPO) has been widely adopted for training large reasoning models and agents, spurring a proliferation of its variants."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2611.33064) · [PDF](https://arxiv.org/pdf/2611.33064)

## 一句话摘要

Since its introduction by DeepSeek, group relative policy optimization (GRPO) has been widely adopted for training large reasoning models and agents, spurring a proliferation of its variants.

## 为什么值得关注

待编辑增强。

## 摘要原文

Since its introduction by DeepSeek, group relative policy optimization (GRPO) has been widely adopted for training large reasoning models and agents, spurring a proliferation of its variants. Yet the group size, a crucial hyperparameter in these GRPO-type algorithms, remains largely chosen by trial and error. Exploiting the U-statistic structure of GRPO's policy gradient, we recast the selection of the group size as a classical statistical problem of variance ratio estimation. This problem is particularly challenging when the denominator of the ratio is small, rendering naive plug-in estimators unstable. To address this challenge, we propose a pessimistic ratio estimator that accounts for the denominator's estimation uncertainty. We characterise the statistical properties of this estimator across three sample-size regimes. Empirically, using %a jackknife-based pessimistic rule on synthetic tasks from Reasoning Gym and real-world benchmarks covering both mathematical reasoning and code generation, we show that our adaptive group size selection reduces the mean squared error of the resulting policy gradient and improves policy optimisation over fixed-group-size baselines, with modest additional computational cost.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shijin Gong, Kai Ye, Victor Chernozhukov, Xinyu Zhang, Chengchun Shi
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
