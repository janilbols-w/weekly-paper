---
title: "NANQ: Noise-Floor-Aware Mixed-Precision Non-Uniform Quantization for Analog Compute-in-Memory"
description: "Analog compute-in-memory (CIM) enables energy-efficient neural network inference, but device variation and read noise can severely degrade low-bit quantized models."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.02700) · [PDF](https://arxiv.org/pdf/2608.02700)

## 一句话摘要

Analog compute-in-memory (CIM) enables energy-efficient neural network inference, but device variation and read noise can severely degrade low-bit quantized models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Analog compute-in-memory (CIM) enables energy-efficient neural network inference, but device variation and read noise can severely degrade low-bit quantized models. Existing CIM-oriented quantization methods mainly minimize ideal quantization error, ignoring the hardware noise floor and thus causing inefficient precision allocation. We propose NANQ, a noise-aware mixed-precision non-uniform quantization framework for analog CIM. NANQ models magnitude-dependent weight noise from measured responses of an eFlash CIM array and converts the noise profile into an adaptive quantization density, assigning finer resolution to low-noise regions while avoiding ineffective precision in noise-dominated regions. It further assigns layer-wise bit-widths by identifying each layer's precision saturation point under hardware noise using a unified threshold. On-chip experiments on an eFlash CIM SoC show that, under 2-bit weight-magnitude quantization, NANQ improves vision-model accuracy by 8.05 percentage points and reduces language-model PPL by 54.7% on average over PowerQuant. Mixed-precision NANQ captures most of the gains obtainable from additional quantization resources with only 3.2-3.8 equivalent bits.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yizhe Chen, Wenshuai Yao, Saiya Wang, Yuannuo Feng, Wenbo Qi, Kechao Tang, Ngai Wong, Wenyong Zhou, Wang Kang
- 发布：2026-08-03；更新：2026-08-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
