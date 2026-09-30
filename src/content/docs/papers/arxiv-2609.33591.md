---
title: "Pretraining Transformers with Quantized Softmax in Attention"
description: "Low-precision Transformer systems increasingly quantize attention matrix multiplications, while softmax often remains at higher precision."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.33591) · [PDF](https://arxiv.org/pdf/2609.33591)

## 一句话摘要

Low-precision Transformer systems increasingly quantize attention matrix multiplications, while softmax often remains at higher precision.

## 为什么值得关注

待编辑增强。

## 摘要原文

Low-precision Transformer systems increasingly quantize attention matrix multiplications, while softmax often remains at higher precision. During pretraining, an approximate softmax changes the gradients that train the model as well as its forward computation. We study this interaction with K-interval attention, which approximates the exponential using K+1 grid values. We vary per-row grid calibration, interpolation versus hard rounding, and the placement of a straight-through surrogate relative to normalization. We derive the corresponding backward rules, including calibration derivatives, and compare these choices in pretraining experiments matched on model, data, and optimizer. Detaching the row extrema leaves the forward computation unchanged but produces a delayed increase in validation loss. With hard rounding at K=4, min-max calibration and a pre-normalization surrogate incur a large loss gap; changing either choice substantially reduces it. At 124M parameters and 2.5B training tokens, fixed-window calibration with a post-normalization surrogate yields a validation loss gap of +0.019 nats relative to softmax at K=4, and with a pre-normalization surrogate yields +0.004 nats at K=16.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shangzhen Zhu, Muyan Hu, Tomasz Kozlowski
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
