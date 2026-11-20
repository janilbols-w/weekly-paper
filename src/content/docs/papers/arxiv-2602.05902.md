---
title: "CoreQ: Mismatch-Corrected Successive Rounding for LLM Quantization"
description: "Post-training quantization (PTQ) enables efficient deployment of large language models by mapping pretrained weights to low-bit formats without retraining, typically using a small calibration set to minimize a layer-wise calibration objective."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2602.05902) · [PDF](https://arxiv.org/pdf/2602.05902)

## 一句话摘要

Post-training quantization (PTQ) enables efficient deployment of large language models by mapping pretrained weights to low-bit formats without retraining, typically using a small calibration set to minimize a layer-wise calibration objective.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training quantization (PTQ) enables efficient deployment of large language models by mapping pretrained weights to low-bit formats without retraining, typically using a small calibration set to minimize a layer-wise calibration objective. However, this sequential procedure induces a mismatch: errors from earlier quantized layers alter the inputs received by later layers, causing the activations to deviate from those of the full-precision model. Recent approaches introduce mismatch-aware calibration objectives to compensate for this effect, but leave open how much of the observed mismatch should shift each layer's calibration target. We show that fully applying the empirical mismatch correction can overfit finite calibration data, while using a fixed correction coefficient ignores variation in mismatch estimates across layers. To address these limitations, we propose CoreQ, a learning-free PTQ framework that uses a geometric decomposition of the mismatch to compute a closed-form, layer-adaptive correction coefficient. This coefficient controls how much of the observed mismatch enters each layer's calibration target, reducing overfitting to limited calibration data without coefficient tuning. CoreQ then applies efficient greedy successive rounding to the resulting triangular least-squares objective. Its bounded beam-search extension, K-CoreQ, trades modest additional compute for improved performance. Across multiple LLM families, scales, bit-widths, and quantization settings, CoreQ and K-CoreQ achieve lower perplexity and higher downstream accuracy than strong PTQ baselines. Code is available at GitHub.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Seohyeon Cha, Huancheng Chen, Dongjun Kim, Haoran Zhang, Kevin Chan, Gustavo de Veciana, Haris Vikalo
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
