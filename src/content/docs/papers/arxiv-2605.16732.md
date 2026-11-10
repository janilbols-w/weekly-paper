---
title: "DiRotQ: Rotation-Aware Quantization for 4-bit Diffusion Transformers"
description: "Diffusion Transformers (DiTs) achieve state-of-the-art image generation quality but incur substantial memory and computational costs at inference."
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2605.16732) · [PDF](https://arxiv.org/pdf/2605.16732)

## 一句话摘要

Diffusion Transformers (DiTs) achieve state-of-the-art image generation quality but incur substantial memory and computational costs at inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion Transformers (DiTs) achieve state-of-the-art image generation quality but incur substantial memory and computational costs at inference. While aggressive Post-Training Quantization (PTQ) to 4-bit precision offers significant efficiency gains, it typically results in severe quality degradation. Existing approaches, including smoothing-based methods, mixed-precision schemes, rotation techniques, and low-rank residual methods, partially mitigate this issue but still leave a noticeable gap to FP16/BF16 performance. In this work, we introduce DiRotQ, a W4A4 PTQ framework that mitigates this degradation through rotation-aware activation quantization. DiRotQ identifies a low-rank subspace capturing dominant activation variance via Principal Component Analysis (PCA), preserving coefficients in this subspace at higher precision while quantizing the remaining components to 4-bit. Activations are rotated into the PCA basis at inference time using calibration-derived orthogonal transformations, while the inverse rotation is fused into the layer weights offline. Combined with GPTQ-based weight quantization, DiRotQ achieves an FID of 15.9 and PSNR of 19.1 dB on PixArt over the MJHQ-30K dataset, outperforming the prior state-of-the-art SVDQuant (FID 18.9, PSNR 17.6) under the same INT W4A4 setting. Beyond standard metrics, we introduce a VLM-as-a-Judge evaluation protocol for diffusion model quantization, the first such evaluation in this setting, providing a more holistic assessment of perceptual quality and prompt alignment under aggressive compression. On the systems side, our Triton-based custom kernel enables efficient end-to-end inference, reducing memory usage of the 12B FLUX.1-dev model by 2.1x and achieving a 2.3x speedup over BF16 on an RTX 4090. On the RTX PRO 6000 with Blackwell architecture, DiRotQ achieves a 2.0x speedup and memory reduction over BF16 using NVFP4.

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

- 作者：Sayeh Sharify, Mahsa Salmani, Hesham Mostafa
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
