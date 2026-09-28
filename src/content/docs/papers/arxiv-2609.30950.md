---
title: "Low-Bit Recurrent States in Hybrid Language Models"
description: "Hybrid language models maintain fixed-size recurrent states, but existing quantizers typically use eight bits or more."
---

**评分：38/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2609.30950) · [PDF](https://arxiv.org/pdf/2609.30950)

## 一句话摘要

Hybrid language models maintain fixed-size recurrent states, but existing quantizers typically use eight bits or more.

## 为什么值得关注

待编辑增强。

## 摘要原文

Hybrid language models maintain fixed-size recurrent states, but existing quantizers typically use eight bits or more. Quantization errors persist according to channel decay rates. We derive distortion weights from the observability Gramian and combine them with normalized state ranges for mixed-precision bit allocation, without calibration data, rotation, or training. We also quantize decay rates logarithmically. With per-token state quantization, a four-bit mean payload reduces excess negative log-likelihood by factors of 3.3--27.9 relative to the best of seven baselines across three hybrid models; metadata costs vary. At six bits, negative log-likelihood differs from the FP32-state baseline by less than 0.005 nats. Ablations separate gains from variable bit widths, decay weighting, and range normalization. With less frequent write-backs, gains diminish and depend on the model and budget.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: observability
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hongren Chen, Jiayang He
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
