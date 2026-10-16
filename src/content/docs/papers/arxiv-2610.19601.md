---
title: "PA1-OPD: One-Step Prefix-Augmented On-Policy Distillation for Language Model Pretraining"
description: "Knowledge distillation (KD) improves language-model pretraining by matching teacher distributions at corpus prefixes, but provides no direct supervision at contexts induced by student predictions."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.19601) · [PDF](https://arxiv.org/pdf/2610.19601)

## 一句话摘要

Knowledge distillation (KD) improves language-model pretraining by matching teacher distributions at corpus prefixes, but provides no direct supervision at contexts induced by student predictions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Knowledge distillation (KD) improves language-model pretraining by matching teacher distributions at corpus prefixes, but provides no direct supervision at contexts induced by student predictions. We introduce PA1-OPD, which augments corpus-path distillation with teacher feedback after one student-sampled transition per selected prefix. This expands the supervised states while retaining next-token prediction and corpus-path KD. Data-anchored roots support parallel sampling, and differentiable tree attention shares prefix computation without changing inference. In two continued-pretraining settings, full coverage improves held-out cross-entropy over KD across C4, PG-19, and Pile at every evaluated checkpoint. In Stage2, selecting the 10% of roots with highest student surprisal adds 48.85% to KD's Macro cross-entropy gain over next-token training. Gains remain when branch supervision excludes successor states already on the corpus path, supporting the value of feedback beyond observed contexts. Additional depth or breadth improves aggregate results at unchanged per-term supervision weight, with benefits varying by corpus. These findings support local student-induced supervision as a complement to pretraining distillation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhenhe Wu, Jian Yang, Yaping Jin, Xinlai Kang, Jie Hu, Hanting Chen
- 发布：2026-10-14；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
