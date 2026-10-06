---
title: "LLM-enhanced spatio-temporal learning for grid-level docked bike sharing demand prediction"
description: "Short-term bike-sharing demand forecasting is complicated by spatial-temporal non-stationarity and the practical difficulty of incorporating unstructured external text into numerical pipelines."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.03834) · [PDF](https://arxiv.org/pdf/2610.03834)

## 一句话摘要

Short-term bike-sharing demand forecasting is complicated by spatial-temporal non-stationarity and the practical difficulty of incorporating unstructured external text into numerical pipelines.

## 为什么值得关注

待编辑增强。

## 摘要原文

Short-term bike-sharing demand forecasting is complicated by spatial-temporal non-stationarity and the practical difficulty of incorporating unstructured external text into numerical pipelines. Conventional approaches rely on historical flow sequences and fixed graph structures, thereby constraining their accuracy when anomalous social events perturb normal travel patterns. We propose a forecasting framework in which a Large Language Model (LLM) drives a semantic shockwave mechanism that converts free-form urban text, such as municipal event schedules, local news, and transit bulletins, into quantified spatial-temporal perturbation fields. The LLM extracts three physically interpretable parameters per event (intensity, spatial reach, and temporal lag), from which Gaussian decay fields are constructed and injected into a Zero-Inflated Adaptive Spatio-Temporal Graph Convolutional Network (ZI-ASTGCN). To handle the pronounced sparsity of grid-level measurements, the model couples a dual-branch output head with a multi-task zero-inflated loss that jointly trains a gating probability and a conditional flow intensity. Experiments on the operational Barcelona Bicing dataset show that ZI-ASTGCN outperforms established neural baselines, with particularly strong gains during high-demand periods, validating the utility of physics-grounded semantic signals in spatial-temporal mobility forecasting.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xuxilu Zhang, Francesc Soriguera
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
