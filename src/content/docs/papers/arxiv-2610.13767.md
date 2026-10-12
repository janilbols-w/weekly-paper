---
title: "DualQuant: Dual-scale Calibration-free Weight-and-Activation Quantization for LLMs"
description: "Low-bit inference on accelerators with native 4-bit support requires quantizing both weights and activations to realize the full throughput gains these formats provide."
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.13767) · [PDF](https://arxiv.org/pdf/2610.13767)

## 一句话摘要

Low-bit inference on accelerators with native 4-bit support requires quantizing both weights and activations to realize the full throughput gains these formats provide.

## 为什么值得关注

待编辑增强。

## 摘要原文

Low-bit inference on accelerators with native 4-bit support requires quantizing both weights and activations to realize the full throughput gains these formats provide. While post-training weight quantization has been extensively studied, activation quantization remains considerably more challenging and typically requires calibration data. In this work, we introduce DUALQUANT, a dual-scale, calibration-free post-training quantization framework that directly minimizes the weight-reconstruction Mean Squared Error (MSE) and, as an immediate by-product, yields per-channel activation rescalings prior to activation quantization. Our key observation is that the scaling factors obtained by minimizing weight-reconstruction error provide effective activation rescalings, enabling competitive activation quantization without calibration data. We formulate DUALQUANT as a non-differentiable weight-reconstruction problem and develop an efficient solver based on variable splitting and block coordinate descent, where each subproblem admits a closed-form update. DUALQUANT provides a unified algorithm supporting a wide range of formats, including the full MX family and NVFP4. To our knowledge, DUALQUANT is the first dual-scaling method to formally support MX and NV block formats. Across Llama and Qwen models evaluated on WikiText-2, C4, and zero-shot downstream tasks, DUALQUANT matches or exceeds the accuracy of calibration-based SmoothQuant across most models and formats, and substantially outperforms calibration-free baselines, with large gains for MX and NV block formats. We validate these gains with a real packed W4A4 inference path for Llama-3.1-8B on an RTX 4090. The resulting implementation closely matches the accuracy of fake quantization while delivering up to 2.61x memory reduction and up to 2.46x throughput speedup over BF16.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Mahsa Salmani, Sayeh Sharify, Hesham Mostafa
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
