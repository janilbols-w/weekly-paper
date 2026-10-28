---
title: "Efficient Quantization Training with Stochastic Rounding via Structured Subspace Randomness"
description: "Low-precision training often relies on stochastic rounding (SR) to keep quantized gradients unbiased and prevent small updates from rounding to zero."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.36587) · [PDF](https://arxiv.org/pdf/2610.36587)

## 一句话摘要

Low-precision training often relies on stochastic rounding (SR) to keep quantized gradients unbiased and prevent small updates from rounding to zero.

## 为什么值得关注

待编辑增强。

## 摘要原文

Low-precision training often relies on stochastic rounding (SR) to keep quantized gradients unbiased and prevent small updates from rounding to zero. Standard SR draws an independent random threshold for every gradient element. However, accelerators generate random numbers on vector units whose throughput lags far behind their matrix units. Drawing one threshold per element saturates the vector unit and can make INT8 training with SR slower than BF16 training. Sharing random thresholds across tensor elements removes this cost but forces those elements to round in the same direction and shifts their rounding errors by a common offset. We find that this offset degrades training primarily through the activation gradient, which propagates the error backward into earlier layers. Because earlier layers cannot cancel an incoming offset using their own local rounding errors, the offset must be removed at the layer where it originates. We propose Structured Subspace Stochastic Rounding (S3R), which quantizes each upstream gradient once for both the activation and weight gradient matrix multiplications and shares a single threshold per token across the hidden dimension. Its error correction, S3R-EC, subtracts the structured mean rounding error from the activation and weight gradients while leaving the optimizer unchanged. In LLM pre-training experiments, uncorrected threshold sharing degrades convergence, whereas S3R-EC eliminates this degradation and matches the validation loss of independent SR. Furthermore, S3R-EC accelerates full INT8 training steps of dense LLMs on TPU v5p by 1.24x to 1.32x over BF16 and by 1.11x over independent SR.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, quantization, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zeyu Wang, Yiheng Duan, Tao Chen, Donghyun Koo, Sihan Liu, Wenbo Zhang, Chuan He, Liang Liu
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
