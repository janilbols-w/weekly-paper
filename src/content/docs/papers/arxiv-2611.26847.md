---
title: "A Sparsity Analysis of Traffic Forecasting Architectures: How Much Missing Data is Too Much?"
description: "Traffic forecasting models are typically evaluated under ideal conditions with complete data."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.26847) · [PDF](https://arxiv.org/pdf/2611.26847)

## 一句话摘要

Traffic forecasting models are typically evaluated under ideal conditions with complete data.

## 为什么值得关注

待编辑增强。

## 摘要原文

Traffic forecasting models are typically evaluated under ideal conditions with complete data. This evaluation does not reflect the frequent sensor failures and communication outages common in real-world deployments. This paper presents a comprehensive analysis of multivariate traffic prediction models to evaluate their performance under varying levels of sensor data loss during inference. We benchmark several architectural paradigms, including graph neural networks, attention-based Transformers, and selective state-space models, across sparsity levels ranging from zero to complete sensor loss, using two widely used multi-channel traffic benchmarks. To ensure consistent comparison across traffic variables, we use normalized metrics and define a usability threshold to identify when predictions become unreliable. Our results show a clear trade-off between baseline accuracy and robustness: models with the highest accuracy under full-data conditions often degrade most sharply as data becomes sparse, while less accurate models maintain more stable performance. These findings show that model selection should be based on the expected reliability of the sensor network rather than peak accuracy alone. This work provides a practical framework for assessing traffic forecasting models and highlights the importance of robustness in real-world applications.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mohamed Hamad, Bilal Mutahir, Mohamed Mabrok, Nizar Zorba, Hamid Saeedi, Halim Yanikomeroglu
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
