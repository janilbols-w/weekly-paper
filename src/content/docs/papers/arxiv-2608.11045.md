---
title: "ReRound: Reconstructive Rounding to Resolve Midpoint Ambiguity in Calibration-Free LLM Quantization"
description: "ReRound (Reconstructive Rounding) is a post-training quantization method that addresses the midpoint ambiguity inherent in standard round-to-nearest (RTN) schemes when quantizing weights near the centers of quantization intervals."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.11045) · [PDF](https://arxiv.org/pdf/2608.11045)

## 一句话摘要

ReRound (Reconstructive Rounding) is a post-training quantization method that addresses the midpoint ambiguity inherent in standard round-to-nearest (RTN) schemes when quantizing weights near the centers of quantization intervals.

## 为什么值得关注

待编辑增强。

## 摘要原文

ReRound (Reconstructive Rounding) is a post-training quantization method that addresses the midpoint ambiguity inherent in standard round-to-nearest (RTN) schemes when quantizing weights near the centers of quantization intervals. Starting from a pretrained LLM, ReRound trains a conditional diffusion model to produce continuous reconstructions of low-bit weights for the LLM. These reconstructed weights act as a guidance signal to disambiguate the rounding direction of weights located close to interval midpoints. To integrate this reconstruction-guided rounding with conventional RTN, ReRound introduces a tolerance metric measuring how far the quantized weight (not the final quantized integer) is away from the midpoint: quantized weights within a tolerance region around midpoints are quantized using diffusion-based reconstructions, whereas weights closer to quantization boundaries are quantized with RTN. By sweeping the tolerance parameter, ReRound generates multiple candidate quantized integer weight matrices and selects the de-quantized weight matrix candidate whose leading singular values most closely match those of the original full-precision weights. This selected candidate determines the tolerance parameter ReRound uses. ReRound is particularly effective for smaller LLMs. Across a range of such models, it consistently outperforms standard RTN for 3-bit and 4-bit weight quantization. ReRound achieves superior accuracy compared to an extensive set of calibration-free methods, remains competitive with calibration-dependent approaches, and operates entirely offline, introducing no additional overhead during low-bit inference. The ReRound strategy represents a new approach for low-bit quantization. The method applies to AI models beyond LLMs. This paper focuses on its applications to small LLMs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：He-Yen Hsieh, H. T. Kung
- 发布：2026-08-12；更新：2026-08-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
