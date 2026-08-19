---
title: "A Data-Efficient Analytical Prior Machine Learning Framework for Sound Reduction Frequency Prediction in Helmholtz Resonators"
description: "High-fidelity finite-element simulations can provide accurate numerical predictions for side-branch resonators, but large simulation datasets are expensive to generate and purely data-driven surrogates may become unreliable when simulation-labelled data are scarce."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.16873) · [PDF](https://arxiv.org/pdf/2608.16873)

## 一句话摘要

High-fidelity finite-element simulations can provide accurate numerical predictions for side-branch resonators, but large simulation datasets are expensive to generate and purely data-driven surrogates may become unreliable when simulation-labelled data are scarce.

## 为什么值得关注

待编辑增强。

## 摘要原文

High-fidelity finite-element simulations can provide accurate numerical predictions for side-branch resonators, but large simulation datasets are expensive to generate and purely data-driven surrogates may become unreliable when simulation-labelled data are scarce. This study develops an analytical-prior learning framework that reuses a low-cost analytical model to improve data efficiency under limited high-fidelity simulation budgets. Two complementary routes are considered. When the analytical model remains available at inference, it is retained as an explicit baseline and the simulation data are used to learn only the analytical-to-simulation discrepancy. When a self-contained predictor is required, the analytical mapping is first distilled from abundant low-cost evaluations into a learned prior and then calibrated with the limited simulation data. The framework is evaluated on rectangular side-branch Helmholtz resonators using 86 simulation-labelled geometries and 8,998 non-overlapping analytical-only geometries. The analytical model achieved a mean absolute error (MAE) of 1.333 Hz. Direct support vector regression (SVR) achieved 3.375 Hz, while residual SVR reduced the MAE to 0.426 Hz. A direct multilayer perceptron (MLP) achieved 1.109 Hz, whereas analytical-prior pretraining reduced the error to 0.556 Hz with frozen-prior residual adaptation and 0.371 Hz with full-model fine-tuning. Across training budgets of 20 to 70 simulation-labelled cases, both analytical correction and analytical-prior pretraining consistently improved data efficiency relative to direct learning. These results show that analytical prior information can substantially improve high-fidelity prediction when simulation data are scarce, with explicit correction and prior distillation serving complementary deployment needs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiaming Li
- 发布：2026-08-19；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
