---
title: "Hardware-Friendly Token-Group Activation Quantization for Low-Bit Mamba Super-Resolution"
description: "Mamba-based super-resolution models are efficient alternatives to Transformer-based restoration backbones, but their low-bit post-training quantization remains challenging because selective scan, Mamba's input-dependent state-space operator, induces different activation ranges across spatial tokens."
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2610.16261v1) · [PDF](https://arxiv.org/pdf/2610.16261v1)

## 一句话摘要

Mamba-based super-resolution models are efficient alternatives to Transformer-based restoration backbones, but their low-bit post-training quantization remains challenging because selective scan, Mamba's input-dependent state-space operator, induces different activation ranges across spatial tokens.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mamba-based super-resolution models are efficient alternatives to Transformer-based restoration backbones, but their low-bit post-training quantization remains challenging because selective scan, Mamba's input-dependent state-space operator, induces different activation ranges across spatial tokens. Thus, a single layer-wise clipping range poorly matches all tokens. We propose Token-Group Quantization, a hardware-friendly activation PTQ framework that statically approximates a hardware-unfriendly post-scan grouping oracle, where tokens with similar preferred clipping ranges are assigned to the same group. To avoid runtime post-scan grouping in static low-bit inference, a lightweight predictor infers the groups from pre-scan features available before the quantized scan path. During calibration, we form pseudo-labels by clustering post-scan activation descriptors that capture similar rounding--clipping behavior. At inference, the frozen predictor maps pre-scan features to groups and selects entries from offline-calibrated group-wise clipping-bound tables, without runtime statistics collection, dynamic clipping updates, or post-scan group assignment. To address low-bit restoration degradation, we further introduce a Frequency-Preserving Refinement (FPR) objective for clipping-bound calibration. FPR aligns Fourier amplitude and phase between full-precision teacher and quantized student outputs to preserve high-frequency structures. Across PTQ protocols, bit-widths, backbones, and tasks, our method consistently outperforms prior Mamba and SR PTQ baselines, transfers to Transformer SR and Vision Mamba classification, composes with rotation-based quantization, and achieves 2.23x speedup on Jetson Orin Nano over FP16. Code is available here.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Jinwoo Chung, Jangho Kim
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/imaboybut/TGQ-MambaSR](https://github.com/imaboybut/TGQ-MambaSR)
- 阅读深度：metadata
