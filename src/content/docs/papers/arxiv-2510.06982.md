---
title: "Robust and Efficient Finetuning of Vision Foundation Models via Implicit Ensembling"
description: "Robust finetuning of foundation models seeks to improve out-of-distribution (OOD) generalization during in-distribution (ID) adaptation."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2510.06982) · [PDF](https://arxiv.org/pdf/2510.06982)

## 一句话摘要

Robust finetuning of foundation models seeks to improve out-of-distribution (OOD) generalization during in-distribution (ID) adaptation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Robust finetuning of foundation models seeks to improve out-of-distribution (OOD) generalization during in-distribution (ID) adaptation. We revisit Mixout, a stochastic regularizer that intermittently replaces finetuned parameters with a reference anchor, and study its effectiveness for robust finetuning of vision foundation models. We reinterpret Mixout as a single-run, weight-sharing implicit ensemble and analyze its expected OOD error through a bias-variance-covariance-locality (BVCL) lens. This perspective reveals three key factors that govern the ID-OOD trade-off: the choice of masking anchor, the mask resampling frequency, and mask sparsity. Guided by this analysis, we propose GMixout, which generalizes Mixout in three ways. First, it explicitly controls the masking period through a resampling-frequency hyperparameter. Second, it replaces the fixed pretrained anchor with an exponential moving average snapshot that adapts throughout training. Third, it uses sparse kernels to update only a small subset of parameters at each iteration, introducing no inference-time overhead and enabling large-model finetuning on consumer-grade GPUs. Experiments across five vision benchmarks show that GMixout consistently outperforms Mixout, Model Soups, and strong parameter-efficient finetuning baselines under both covariate shift and class imbalance.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Masih Aminbeidokhti, Heitor Rapela Medeiros, Eric Granger, Marco Pedersoli
- 发布：2026-10-20；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
