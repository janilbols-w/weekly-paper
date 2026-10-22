---
title: "Distilling Multi-Teacher Scoring Principles for Unsupervised Time Series Anomaly Detection"
description: "Time series anomalies take diverse forms, and individual detectors encode different anomaly scoring principles that rarely cover all anomaly types."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.29063) · [PDF](https://arxiv.org/pdf/2610.29063)

## 一句话摘要

Time series anomalies take diverse forms, and individual detectors encode different anomaly scoring principles that rarely cover all anomaly types.

## 为什么值得关注

待编辑增强。

## 摘要原文

Time series anomalies take diverse forms, and individual detectors encode different anomaly scoring principles that rarely cover all anomaly types. Recent unsupervised time-series anomaly detectors provide complementary scoring signals, yet deploying them as an ensemble preserves the inference and maintenance cost of every individual detector. We study whether heterogeneous teacher detectors can be distilled into a single lightweight detector in the unsupervised setting, where no anomaly labels are available to define a shared target. AnoMix addresses this by extracting weak pairwise supervision from the training-set anomaly scores of frozen teachers. It normalizes each teacher score sequence independently and trains the student with CoRank, a multi-teacher ranking-distillation objective that converts teacher score gaps into pairwise supervision through teacher consensus. Across seven benchmark datasets, AnoMix successfully integrates complementary teacher scoring principles into a single deployable model, improving over individual detectors and static score ensembles while using a compact student with under 80k parameters on the benchmark settings. A zero-shot variant further shows that the distilled ranking signal transfers to unseen datasets and can outperform large pretrained time-series foundation models for anomaly detection.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dongchan Cho, Jiho Han, Juwon Hwang, Changhee Min, Minsang Kim, Namsoon Jung
- 发布：2026-10-22；更新：2026-10-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
