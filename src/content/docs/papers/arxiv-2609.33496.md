---
title: "Chameleon: Dynamic Format Adapter for Efficient Diffusion"
description: "Post-training quantization (PTQ) is the standard way to run modern diffusion models on memory-constrained accelerators, yet every existing diffusion PTQ scheme fixes the $\\mathit{number\\ format}$ in advance and only tunes the scale, zero point, or per-layer bit-width."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.33496) · [PDF](https://arxiv.org/pdf/2609.33496)

## 一句话摘要

Post-training quantization (PTQ) is the standard way to run modern diffusion models on memory-constrained accelerators, yet every existing diffusion PTQ scheme fixes the $\mathit{number\ format}$ in advance and only tunes the scale, zero point, or per-layer bit-width.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training quantization (PTQ) is the standard way to run modern diffusion models on memory-constrained accelerators, yet every existing diffusion PTQ scheme fixes the $\mathit{number\ format}$ in advance and only tunes the scale, zero point, or per-layer bit-width. At a fixed bit-width the best format depends on the distribution being encoded, and that distribution differs across weight channels, across layers, and along the diffusion timestep, where activation distributions slide from heavy-tailed and noise-dominated to tightly clustered and structured. We propose Chameleon, a PTQ framework that holds the bit-width fixed and treats the format itself as a discrete variable, chosen per weight channel and per (layer, timestep bucket) activation tensor. Activation formats come from {INT8, FP8 E4M3, FP8 E5M2, MXFP8, MXINT8}, selected ahead of time from two cheap statistics (empirical kurtosis and the closed-form diffusion SNR) and stored in a lookup table; weight formats come from {INT8, MXINT8} at 8 bits or {INT4, NF4, FP4 E2M1, MXINT4, MXFP4} at 4 bits, selected offline by reconstruction error. An architectural fork adapts the same selection layer to multi-step UNets, single-step distilled models, and Diffusion Transformers. Across SDXL, SDXL-Turbo, and PixArt-$\alpha$ on COCO-2014, Chameleon achieves the best FID in all six backbone $\times$ bit-width settings, with CLIP within 0.24 of the FP16 reference and the best of all quantized methods at $W_{4}A_{8}$.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4, fp8, int4, int8, quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Arnab Sanyal, Sandeep Chinchali
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
