---
title: "Softmax Reparameterization for Output-Head Quantization"
description: "Large vocabularies make output heads a substantial inference cost in small language models."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.31291) · [PDF](https://arxiv.org/pdf/2609.31291)

## 一句话摘要

Large vocabularies make output heads a substantial inference cost in small language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large vocabularies make output heads a substantial inference cost in small language models. We propose softmax reparameterization, a post-training method that selects a functionally equivalent output head before quantization. The method subtracts a scalar multiple of the vocabulary-row mean from every output row and selects the coefficient by validation KL separately for RTN, activation-weighted MSE, and full-Hessian GPTQ. This one-dimensional search includes the original head and fixed mean-centering, preserves the full-precision softmax distribution, and leaves the trained decoder unchanged; a rank-one correction handles nonlinear logit paths such as soft-capping. Across seven heads, W4 gains concentrate where baseline quantization substantially distorts predictions: on Phi-4-mini, AW-MSE KL falls from 0.936 to 0.256. The gains survive stronger GPTQ calibration and remain complementary to exact per-channel scaling and affine quantization. Across four heads and three W4 quantizers, frozen WikiText-selected coefficients also transfer to C4 and OpenWebMath, outperforming mean-centering in all 18 comparisons where the frozen coefficient differs from $1$ and matching it in the remaining six. At W2, used as a compression stress test, benefits broaden across nearly the full model--quantizer matrix. Matched residual analysis shows that improved fidelity can accompany greater logit reconstruction error while reducing the residual's Fisher-weighted cost. For shift-compatible heads, reparameterization adds no inference operation and preserves packed W4 execution: with the decoder held in BF16, quantizing the Phi output head reduces batch-one generation latency by 10.8% relative to the BF16-head baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Asim Kadav, Christian Flores, Chirag Arora, Varun Kotte, Hongbo Zheng, Lan Yan, Priya Shanmugasundaram, Tracy Holloway King
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
