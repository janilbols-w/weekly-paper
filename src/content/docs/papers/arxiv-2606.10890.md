---
title: "Optimal Post-Training Quantization Scales and Where to Find Them"
description: "Post-training quantization (PTQ) compresses large language models by mapping weights to low-bit representations."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2606.10890) · [PDF](https://arxiv.org/pdf/2606.10890)

## 一句话摘要

Post-training quantization (PTQ) compresses large language models by mapping weights to low-bit representations.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training quantization (PTQ) compresses large language models by mapping weights to low-bit representations. While much work has focused on how weights are rounded onto the quantization grid, the scaling factor that defines the grid is typically chosen with simple, data-free heuristics. We observe that, under round-to-nearest (RTN) quantization, the grid assignments are piecewise constant in the scale, making the output reconstruction error piecewise quadratic over finitely many intervals, each admitting a closed-form optimization. Building on this insight, we present PiSO (Piecewise Scale Optimization), an algorithm that leverages calibration data to efficiently select channel-wise scales to achieve globally optimal output reconstruction error to arbitrary accuracy. We extend PiSO to group-wise quantization via tractable objectives. We also propose strategies for integrating it with error-correction methods such as GPTQ and Qronos, which greedily adjust weight assignments to compensate for the rounding errors of previously quantized weights. Experiments on Llama and Qwen models across multiple sizes and bit-widths show consistent improvements in perplexity and zero-shot accuracy, both standalone and combined with error correction, with gains increasing as the bit-width narrows. For instance, on Llama-3, PiSO reduces the 2-bit perplexity of Qronos by up to 7x, and at 3 bits, PiSO without error correction outperforms GPTQ with absmax scales.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Juan Amboage, Pablo Monteagudo-Lago, Ian Colbert, Giuseppe Franco, Nicholas Fraser
- 发布：2026-10-20；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
