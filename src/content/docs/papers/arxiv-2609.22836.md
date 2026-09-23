---
title: "A Hybrid Attention Model Learning Unified Time-aware Patch Representation for Irregular Multivariate Time Series Forecasting"
description: "Time series foundation models (TSFMs) have recently delivered impressive zero-shot performance across diverse forecasting tasks."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.22836) · [PDF](https://arxiv.org/pdf/2609.22836)

## 一句话摘要

Time series foundation models (TSFMs) have recently delivered impressive zero-shot performance across diverse forecasting tasks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Time series foundation models (TSFMs) have recently delivered impressive zero-shot performance across diverse forecasting tasks. However, real-world decision-making frequently relies on \emph{irregular multivariate time series} (IMTS), where inconsistent inter-observation intervals and asynchronous sampling across variables coexist with informative missingness. Existing TSFMs handle such inputs either through imputation that injects spurious values or through index-based positional encodings that ignore continuous time. There is still a gap in the foundation model that follows the original IMTS patterns. In this paper, we propose a hybrid attention model that learns a unified time-aware patch representation for IMTS forecasting. We first design a \emph{time-aware patch encoding} that maps a variable number of intra-patch timestamps into a fixed-size embedding, producing a uniform format for irregular patches without resorting to imputation. We then introduce a \emph{time bias attention} mechanism that calibrates inter-patch temporal misalignment and asynchronous cross-channel dependencies as auxiliary attention offset. Finally, on top of a decoder-only Transformer backbone, we adopt a \emph{hybrid causal mask} that preserves a bidirectional full view over the historical context while keeping the forecast horizon strictly autoregressive. To support large-scale pretraining under irregular settings, we also curate VersaTSA, an archive of $30$B observations that retains the native sampling sparsity of its sources. Experiments on three IMTS benchmarks and a standard regular-MTS benchmark show that our model achieves state-of-the-art zero-shot performance on IMTS and remains competitive when transferred to regular forecasting.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhihao Lin, Li Lin, Qi Zhang, Kaiwen Xia, Shuai Wang, Jialin Qiao
- 发布：2026-09-22；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
