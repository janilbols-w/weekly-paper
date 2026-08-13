---
title: "SoftWater: Class-Aware Rate Allocation for Softmax Quantization"
description: "Post-training quantization pipelines routinely leave the softmax output layer in high precision."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.12026) · [PDF](https://arxiv.org/pdf/2608.12026)

## 一句话摘要

Post-training quantization pipelines routinely leave the softmax output layer in high precision.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training quantization pipelines routinely leave the softmax output layer in high precision. Yet in small LLMs with modern vocabularies, the head holds 15--30\% of all parameters, so a nominal ``2-bit'' model with an fp16 head can store several times as many bits per weight. We pose softmax-layer quantization as a rate-distortion problem under the KL divergence between the original and quantized output distributions. A second-order analysis reveals a class-aware geometry: quantization error is weighted jointly by feature covariance and class-specific softmax curvature. A separability approximation replaces the $Kn\times Kn$ Cholesky with one $n\times n$ factorization rescaled per class, making the lattice encodable by successive interference cancellation, with both statistics from a single forward pass. The resulting method, SoftWater, gives fine grids to frequent, low-variance classes and coarse grids to rare ones, a large gap under Zipfian token distributions. Across five models from 1B to 32B, SoftWater outperforms the released WaterSIC quantizer (near-optimal under linear-layer WMSE but not output KL) at matched head rates on 59 of 60 test points, using none of that pipeline's refinements and cutting head-induced KL by $6.5\times$--$8.3\times$ at 2 bits. On Llama-3.2-1B-Instruct with quantized bodies, a 2-bit head removes 45--60\% of stored bytes for a $2.9$--$3.7\%$ perplexity increase. Because the class-side statistic comes from calibration data, matching calibration to the deployment domain gives the lowest KL on that domain throughout. On a tied model, a 4-bit head is near-lossless and a 2-bit head costs under 4\% perplexity, making head quantization of such models practical.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Joao V. Cavalcanti, Ashia C. Wilson
- 发布：2026-08-13；更新：2026-08-13
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
