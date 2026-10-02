---
title: "Dr. OPD: Learning What to Follow for Optimal On-Policy Distillation of Large Language Models"
description: "On-policy distillation (OPD) trains a student on its own generated responses using dense, token-level supervision from a stronger teacher."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.38025) · [PDF](https://arxiv.org/pdf/2609.38025)

## 一句话摘要

On-policy distillation (OPD) trains a student on its own generated responses using dense, token-level supervision from a stronger teacher.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) trains a student on its own generated responses using dense, token-level supervision from a stronger teacher. Vanilla OPD treats all teacher signals equally, assuming that the teacher's supervision is equally important for every token. However, teacher signals at different tokens may have very different effects on the student's performance: some correct important reasoning errors, while others have little effect on the final answer. Motivated by this observation, we introduce Dr. OPD (OPD Done Right), which defines the optimal weighted OPD to maximize the student's performance. We formulate Dr. OPD as a bilevel optimization problem in which the student learns from weighted teacher supervision, while the weights are selected to maximize the expected reward of the resulting student. To solve Dr. OPD, we develop an efficient iterative solver that updates the token weights and student policy alternatively. At each round, it updates weights in closed form and then takes one gradient step on the resulting weighted OPD objective. Under regularity conditions, we show that this weighted update achieves a higher expected reward than a vanilla OPD update. Empirically, across strong-to-weak and same-size distillation on math and code, Dr. OPD consistently outperforms all evaluated baselines. In particular, in the strong-to-weak distillation setting, Dr. OPD improves average math performance by $9.7$ points over vanilla OPD, and enables the smaller student to surpass its larger teacher.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhenyu Wang, Tianze Wang, Linjun Zhang, Yifan Hu
- 发布：2026-09-29；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
