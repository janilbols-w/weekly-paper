---
title: "One Patch, Three Roles: What Is Actually Coupled in Autoregressive Time-Series Forecasting?"
description: "Patch-based autoregressive time-series forecasting often ties input representation, learned transitions, and recursive execution to one patch length."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.23686) · [PDF](https://arxiv.org/pdf/2609.23686)

## 一句话摘要

Patch-based autoregressive time-series forecasting often ties input representation, learned transitions, and recursive execution to one patch length.

## 为什么值得关注

待编辑增强。

## 摘要原文

Patch-based autoregressive time-series forecasting often ties input representation, learned transitions, and recursive execution to one patch length. We ask which of these roles can be adjusted separately. A supporting atomic-encoding study finds greater sensitivity to model width than to atom grouping on the evaluated grid. Our main finding is that a frozen parent's recursive trajectory is easier to fit than the observed future with lightweight parallel exits. Autoregressive Trajectory Distillation (ATD) turns this into selectable ATD-1/2/4/8 execution, with ATD-1 exactly recovering the parent. On a paired four-data-set comparison, ATD-8 reaches $5.54\times$ end-to-end speedup with stable quality across widths. Fewer calls do not automatically remove the parent's existing forecast error: ATD improves trajectory fidelity in all 21 seed runs but forecast accuracy in only 15 against matched clean-future supervision. We further find a correctable residual projection along a train-selected periodic history direction. Spectrum Tangent applies this correction without adding neural parameters or Transformer calls. At horizon 720, it reduces mean squared error (MSE) and mean absolute error (MAE) by 2.54% and 2.33% over seven data sets and two output widths, while remaining $3.24\times$ faster than recursive inference. Level and shape projections sometimes disagree. Trajectory compressibility, the fidelity-accuracy mismatch, and the correction recur across three public AR parents. Together these results separate representation, transition, and execution as AR design axes. Code is available at https://github.com/RowanFFF/ATD-Spectrum-Tangent.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Ziang Li, Yue Huang, Guoxu Zhou, Na Han, Jie Wen, Lunke Fei, Xiaozhao Fang
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/RowanFFF/ATD-Spectrum-Tangent](https://github.com/RowanFFF/ATD-Spectrum-Tangent)
- 阅读深度：metadata
