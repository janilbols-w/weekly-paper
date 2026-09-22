---
title: "Time Series Foundation Models for Process Model Forecasting"
description: "Process Model Forecasting (PMF) aims to predict how the control-flow structure of a process evolves over time by modeling the temporal dynamics of directly-follows (DF) relations, complementing predictive process monitoring that focuses on single-case prefixes."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2512.07624) · [PDF](https://arxiv.org/pdf/2512.07624)

## 一句话摘要

Process Model Forecasting (PMF) aims to predict how the control-flow structure of a process evolves over time by modeling the temporal dynamics of directly-follows (DF) relations, complementing predictive process monitoring that focuses on single-case prefixes.

## 为什么值得关注

待编辑增强。

## 摘要原文

Process Model Forecasting (PMF) aims to predict how the control-flow structure of a process evolves over time by modeling the temporal dynamics of directly-follows (DF) relations, complementing predictive process monitoring that focuses on single-case prefixes. Prior benchmarks show that machine learning and deep learning models provide only modest gains over statistical baselines, mainly due to the sparsity and heterogeneity of the DF time series. We investigate Time Series Foundation Models (TSFMs), large pre-trained models for generic time series, as an alternative for PMF. Using DF time series derived from real-life event logs, we compare zero-shot use of TSFMs, without additional training, with fine-tuned variants adapted on PMF-specific data. TSFMs generally achieve lower forecasting errors (MAE and RMSE) than traditional and specialized models trained from scratch on the same logs, indicating effective transfer of temporal structure from non-process domains. While fine-tuning can further improve accuracy, the gains are often small and may disappear on smaller or more complex datasets, so zero-shot use remains a strong default. Our study highlights the generalization capability and data efficiency of TSFMs for process-related time series and, to the best of our knowledge, provides the first systematic evaluation of temporal foundation models for PMF.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yongbo Yu, Jari Peeperkorn, Johannes De Smedt, Jochen De Weerdt
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
