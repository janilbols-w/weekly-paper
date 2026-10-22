---
title: "Extreme Low-State Quantized Transformer for Electricity-Load Forecasting"
description: "Aggressive low-state weight quantization can substantially reduce neural-network representational flexibility, making predictive performance difficult to preserve when only a few discrete weight states are available."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.28784) · [PDF](https://arxiv.org/pdf/2610.28784)

## 一句话摘要

Aggressive low-state weight quantization can substantially reduce neural-network representational flexibility, making predictive performance difficult to preserve when only a few discrete weight states are available.

## 为什么值得关注

待编辑增强。

## 摘要原文

Aggressive low-state weight quantization can substantially reduce neural-network representational flexibility, making predictive performance difficult to preserve when only a few discrete weight states are available. We investigate this regime for Transformer-based electricity-load forecasting using 3-, 5-, 7-, and 16-state weight quantization across feed-forward-only and attention-plus-feed-forward quantization. Two tasks predict either the next hour or the next 24 hours from the preceding 48 hours across two co-primary electricity-consumption datasets. Direct post-training quantization (PTQ) increased mean normalized root-mean-square error (NRMSE) relative to full precision by 6.25 and 7.04 percentage points in Datasets A and B, whereas quantization-aware fine-tuning (QAT-FT) recovered approximately 90.2% and 94.5% of these penalties. Quantization-aware training from random initialization (Scratch-QAT) also produced competitive low-state solutions, with particularly favorable behavior at three states. We further introduce accumulated-update thresholding, which accumulates optimizer-proposed weight changes before commitment. Relative to paired Scratch-QAT controls, this reduced committed shadow-weight updates by approximately 99.7% and discrete state transitions by approximately 77--80%, while mean NRMSE changed by only +0.042 and +0.197 percentage points. These results show that useful Transformer forecasting can be retained under highly discrete weight representations while strongly suppressing target-state activity, supporting a prospective route toward compact, low-activity edge forecasting using multilevel synaptic devices.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Muhammad Sabbir Alam, Harindra Sandun Mavikumbure, Victor Cobilean, Milos Manic, Jayasimha Atulasimha
- 发布：2026-10-22；更新：2026-10-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
