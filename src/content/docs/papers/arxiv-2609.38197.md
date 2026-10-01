---
title: "DualCast: A Dual-Path Language Model for Bimodal Financial Time-Series Forecasting"
description: "Financial time-series forecasting must capture price dynamics across heterogeneous assets while incorporating news available at prediction time."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.38197) · [PDF](https://arxiv.org/pdf/2609.38197)

## 一句话摘要

Financial time-series forecasting must capture price dynamics across heterogeneous assets while incorporating news available at prediction time.

## 为什么值得关注

待编辑增强。

## 摘要原文

Financial time-series forecasting must capture price dynamics across heterogeneous assets while incorporating news available at prediction time. We introduce DualCast, a dual-path framework that extends a frozen language model with a discrete financial vocabulary. Each log-return patch is represented by a learned summary token and three residual shape tokens, preserving local drift and volatility while allowing shape patterns to be shared across assets. To improve codebook utilization, we develop adaptive frequency-equalizing residual vector quantization, which rebalances overloaded codewords without compromising reconstruction accuracy. The fast path trains only the new financial-token embeddings and output heads on a frozen Qwen3-8B backbone. A toggleable LoRA adapter enables a slow path that conditions on the fast forecast and news available at the forecast origin to produce a revised prediction. The reviser is initialized by supervised fine-tuning and further optimized with a return-space group relative policy optimization objective that rewards improvements over the fast forecast. In zero-shot evaluations covering equities and energy prices at five-minute, daily, and weekly resolutions, the slow path achieves the lowest mean absolute percentage error among the compared methods in 8 of 12 dataset-horizon settings, including every longest-horizon setting. News ablations indicate additional gains in most tested settings, although their magnitude varies across markets. DualCast thus combines a fast numerical forecaster with an optional text-conditioned revision mechanism.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Wentao Zhao, Hongqiang Wu, Shanghang Liu, Zhaochen Zan, Yu Zhang, Biqing Huang
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
