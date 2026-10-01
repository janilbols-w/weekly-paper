---
title: "GeoFP8: Geometry-Aware FP8 Gradient Compression for Distributed LLM Training"
description: "Gradient communication is a primary scaling bottleneck in large language model (LLM) pretraining."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2607.07494) · [PDF](https://arxiv.org/pdf/2607.07494)

## 一句话摘要

Gradient communication is a primary scaling bottleneck in large language model (LLM) pretraining.

## 为什么值得关注

待编辑增强。

## 摘要原文

Gradient communication is a primary scaling bottleneck in large language model (LLM) pretraining. Communicating gradients in low-precision formats, such as FP8 and NVFP4, can significantly reduce the communication volume. Existing methods quantize gradients via linear or nonlinear mappings in Euclidean space, often degrading model performance because highly anisotropic gradients incur direction-dependent distortion. We present GeoFP8, a geometry-informed gradient scaling method that performs low-precision communication in geometry-aware coordinates. By transforming gradients into a near-isotropic space before quantization, GeoFP8 makes low-precision representations substantially more faithful to their high-precision counterparts. GeoFP8 only changes the coordinate system used for low-precision gradient communication and does not change the optimizer, training recipe, communication collective, or low-precision format. We also develop a simplified geometry-aware transformation algorithm with low-rank approximation and selective application to balance the computation overhead and communication reduction. We examine the empirical convergence of GeoFP8 using Llama-300M and Llama-600M models. Our results show that GeoFP8 reduces the end-to-end pretraining time of Llama-600M by 7.6% on 64 NVIDIA GH200 Superchips, while improving the downstream task preservation profile over direct Euclidean FP8 communication under the same optimizer and communication path.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jieying Wang, Zizhong Wang, Fangru Linghu, Shuyuan Fan, Jiajia Li, Zhao Zhang
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
