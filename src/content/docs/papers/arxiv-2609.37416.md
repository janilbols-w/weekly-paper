---
title: "Scale Sensitivity in Low-Bit Post-Training Quantization: Curvature of the Quantization Error Landscape"
description: "Post-training quantization (PTQ) methods in the GPTQ family minimize a layer-wise reconstruction error on a uniform grid whose scale must be chosen; the common max-based choice degrades sharply at low bit-widths."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2609.37416v1) · [PDF](https://arxiv.org/pdf/2609.37416v1)

## 一句话摘要

Post-training quantization (PTQ) methods in the GPTQ family minimize a layer-wise reconstruction error on a uniform grid whose scale must be chosen; the common max-based choice degrades sharply at low bit-widths.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training quantization (PTQ) methods in the GPTQ family minimize a layer-wise reconstruction error on a uniform grid whose scale must be chosen; the common max-based choice degrades sharply at low bit-widths. We study how sensitive this objective is to the scale. For a layer with i.i.d. Gaussian weights and calibration activations of sufficiently large effective rank, we prove that, as the width grows, the normalized round-to-nearest loss converges with high probability, uniformly over all scales, to the mean-squared error of a uniform quantizer applied to a standard Gaussian; we verify the effective-rank condition for wide, randomly initialized MLPs with odd Lipschitz activations and isotropic Gaussian calibration data. The limiting objective has a unique nondegenerate minimizer, whose scale decreases strictly with the number of levels and whose curvature with respect to relative scale errors decays approximately exponentially with the bit-width. GPTQ experiments on five LLMs show the same trend: the scale rule changes perplexity substantially at 2--3 bits and negligibly from 6 bits on, and a local measure of GPTQ scale sensitivity decreases with bit-width in line with the Gaussian curvature. The Gaussian-optimal scale fails on raw weights; after Hadamard incoherence processing it matches the best searched rule at 3 bits and above without any search, but remains clearly worse at 2 bits.

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

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jonas von Berg, Massimiliano Datres, Carlo Kneißl, Gitta Kutyniok
- 发布：2026-09-29；更新：2026-09-29
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
