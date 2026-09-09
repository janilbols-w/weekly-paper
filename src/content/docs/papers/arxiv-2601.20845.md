---
title: "PatchFormer: A Patch-Based Time Series Foundation Model with Hierarchical Masked Reconstruction and Cross-Domain Transfer Learning for Zero-Shot Multi-Horizon Forecasting"
description: "Time series forecasting is a fundamental problem with applications in climate, energy, healthcare, and finance."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2601.20845) · [PDF](https://arxiv.org/pdf/2601.20845)

## 一句话摘要

Time series forecasting is a fundamental problem with applications in climate, energy, healthcare, and finance.

## 为什么值得关注

待编辑增强。

## 摘要原文

Time series forecasting is a fundamental problem with applications in climate, energy, healthcare, and finance. Many existing approaches require domain-specific feature engineering and substantial labeled data for each task. We introduce PatchFormer, a patch-based time series foundation model that uses hierarchical masked reconstruction for self-supervised pretraining and lightweight adapters for efficient transfer. PatchFormer segments time series into patches and learns multiscale temporal representations with learnable aggregation across temporal scales. Pretraining uses masked patch reconstruction with dynamic masking and objectives that encourage both local accuracy and global consistency, followed by cross-domain knowledge distillation. Experiments on 24 benchmark datasets spanning weather, energy, traffic, finance, and healthcare demonstrate state-of-the-art zero-shot multi-horizon forecasting, reducing mean squared error by 27.3 percent relative to strong baselines while requiring 94 percent less task-specific training data. The model exhibits near log-linear scaling with more pretraining data up to 100 billion points and processes length-512 sequences 3.8x faster than full-sequence transformers.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Olaf Yunus Laitinen Imanov, Derya Umut Kulali, Taner Yilmaz
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
