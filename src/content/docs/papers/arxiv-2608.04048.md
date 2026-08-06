---
title: "Recurrent Residual Quantization: A Progressive Multi-Precision Representation for LLMs"
description: "Serving large language models (LLMs) under diverse deployment constraints requires flexible trade-offs between accuracy, memory footprint, and throughput."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.04048) · [PDF](https://arxiv.org/pdf/2608.04048)

## 一句话摘要

Serving large language models (LLMs) under diverse deployment constraints requires flexible trade-offs between accuracy, memory footprint, and throughput.

## 为什么值得关注

待编辑增强。

## 摘要原文

Serving large language models (LLMs) under diverse deployment constraints requires flexible trade-offs between accuracy, memory footprint, and throughput. However, conventional quantization methods typically require a separate checkpoint for each target bit-width. We introduce Recurrent Residual Quantization (RRQ), a post-training quantization (PTQ) framework that represents weights as a low-bit quantized base together with a sequence of quantized residual corrections, enabling multiple effective precisions from a single checkpoint. Starting from a 2-bit model obtained via post-training quantization (PTQ) or round-to-nearest (RTN), RRQ progressively adds lightweight 2-bit residuals generated via RTN to construct 4-, 6-, and 8-bit representations. The method is calibration-free and avoids joint multi-bit optimization. In our Qwen3-8B setup, the full all-RTN 2-/4-/6-/8-bit package is constructed in 1,293 seconds, 3.3 times faster than the measured MatGPTQ construction. Experiments on six recent LLMs show competitive accuracy at 6 and 8 bits, with model-dependent behavior at 4 bits. The code will be made publicly available upon publication.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yu Luo, Bo Dong, Wenhua Cheng, Haihao Shen
- 发布：2026-08-06；更新：2026-08-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
