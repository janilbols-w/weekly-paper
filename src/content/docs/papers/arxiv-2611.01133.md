---
title: "Rethinking LLM Pruning via Test-Time Scaling"
description: "Structured pruning reduces the size of large language models, often at the cost of lower accuracy."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.01133) · [PDF](https://arxiv.org/pdf/2611.01133)

## 一句话摘要

Structured pruning reduces the size of large language models, often at the cost of lower accuracy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Structured pruning reduces the size of large language models, often at the cost of lower accuracy. Whether this decline reflects diminished reasoning capacity or greater difficulty in sampling correct solutions is less clear. We examine this question across expert, FFN and layer pruning on four mathematical and coding benchmarks, comparing original and pruned models through pass@k at matched sampling budgets. Even after substantial pruning, some models match or exceed the original model's reasoning coverage despite lower pass@1, and solve problems left unsolved in the original samples. Retaining broad coverage, however, does not mean that correct solutions remain easy to obtain. Under severe pruning, diverse generated chain-of-thought (CoT) traces can coexist with increased repetition and less reliable generation. As correct answers become harder to sample, the additional attempts can sharply increase total token use even when individual responses become shorter. This separation between coverage and sampling efficiency also clarifies expert-selection gains, as methods with markedly different pass@1 can solve the same problems at large budgets yet require different numbers of attempts to reach a common coverage target. Pruning should therefore be assessed by both the range of problems a model can still solve and the sampling cost of obtaining correct solutions.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mingyang Song, Mao Zheng
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
