---
title: "Every Coin Has Two Sides: On the Dual Nature of Generalization in On-Policy Distillation of Large Language Models"
description: "On-policy distillation (OPD) transfers teacher capabilities by supervising trajectories sampled from the student's own policy, yet its generalization behavior remains poorly understood, as most studies evaluate OPD on a single domain and on benchmarks close to the training data."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](http://arxiv.org/abs/2608.16647v1) · [PDF](https://arxiv.org/pdf/2608.16647v1)

## 一句话摘要

On-policy distillation (OPD) transfers teacher capabilities by supervising trajectories sampled from the student's own policy, yet its generalization behavior remains poorly understood, as most studies evaluate OPD on a single domain and on benchmarks close to the training data.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) transfers teacher capabilities by supervising trajectories sampled from the student's own policy, yet its generalization behavior remains poorly understood, as most studies evaluate OPD on a single domain and on benchmarks close to the training data. We present a controlled study that varies one generalization factor at a time, from in-domain distribution shifts to cross-domain transfer and the multi-teacher setting. We find that OPD transfers a teacher's reasoning behavior rather than its answers to particular problems: training difficulty barely matters, and even problems the teacher never solves are useful. Transfer depends strongly on the origin relationship between teacher and student: same-origin pairs bring the student close to the teacher across languages, reasoning horizons, and even other domains, whereas cross-origin pairs mostly fit the trained distribution. This broad reach is a double-edged sword: since routing prompts to domain experts cannot confine each teacher's influence, combining them yields a mixture-dependent seesaw among their capabilities. These results clarify when OPD generalizes and offer a useful perspective for diagnosing multi-teacher OPD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhaoyi Li, Deyang Kong, Yuan Wei, Evan Yang, Ranran Shen, Mahardika Krisna Ihsani, Ming Yang, Wei Zhang, Chuan Hao, Jian Yang, Ran Tao, Bryan Dai, Shikun Zhang, Wei Ye, Ying Wei, Defu Lian
- 发布：2026-08-17；更新：2026-08-17
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
