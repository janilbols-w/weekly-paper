---
title: "Aurora-X: Built for Extreme Time Series Forecasting"
description: "Time series foundation models (TSFMs) enable cross-domain forecasting, but their development as general-purpose forecasters remains constrained by underexplored training potential and limited architectural versatility."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.31038) · [PDF](https://arxiv.org/pdf/2609.31038)

## 一句话摘要

Time series foundation models (TSFMs) enable cross-domain forecasting, but their development as general-purpose forecasters remains constrained by underexplored training potential and limited architectural versatility.

## 为什么值得关注

待编辑增强。

## 摘要原文

Time series foundation models (TSFMs) enable cross-domain forecasting, but their development as general-purpose forecasters remains constrained by underexplored training potential and limited architectural versatility. To address these challenges, we introduce Aurora-X, a billion-scale TSFM with a progressive curriculum and a unified architecture. We first use channel-independent pretraining to learn temporal patterns, then introduce cross-variable dependencies, varied context and horizon lengths, and future covariates if available during midtraining. Variable-resolution post-training further enables an adjustable temporal span per token at inference. With fixed model weights, this supports longer histories under a fixed token budget or fewer tokens for the same history, enabling test-time scaling. With a versatile architecture, Aurora-X supports cross-variable modeling, covariate conditioning, and parallel decoding of future patches for probabilistic forecasting. These are supported by a novel pattern-guided mixture-of-experts that expands model capacity through sparse activation and uses shallow patch similarities to constrain deep-layer routing, guiding expert specialization across heterogeneous time series. Furthermore, we propose an implicit quantile network head that predicts arbitrary quantiles to characterize predictive distributions, enhancing probabilistic forecasting flexibility. Comprehensive experiments on GIFT-Eval, TIME, FEV-Bench, TFB, and DAG-Bench demonstrate state-of-the-art forecasting performance against pretrained TSFMs and task-specific supervised models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 9 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: parallel decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xingjian Wu, Chenjuan Guo, Xiangfei Qiu, Zhigang Hu, Hanyin Cheng, Peng Chen, Yang Shu, Jilin Hu, Bin Yang
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
