---
title: "MiX: Micro-Inverted-Scaling for End-to-End Low-Bit Vision-Language Model Acceleration"
description: "The deployment of Vision-Language Models (VLMs) on edge devices is severely bottlenecked by memory bandwidth, necessitating aggressive sub-8-bit quantization."
---

**评分：54/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.19683) · [PDF](https://arxiv.org/pdf/2609.19683)

## 一句话摘要

The deployment of Vision-Language Models (VLMs) on edge devices is severely bottlenecked by memory bandwidth, necessitating aggressive sub-8-bit quantization.

## 为什么值得关注

待编辑增强。

## 摘要原文

The deployment of Vision-Language Models (VLMs) on edge devices is severely bottlenecked by memory bandwidth, necessitating aggressive sub-8-bit quantization. Since edge accelerators are strictly constrained by area and power, they require end-to-end quantized models. However, the extreme dynamic range gap between multi-modal tokens causes standard block formats to suffer "microscaling collapse," where a single massive outlier hijacks the shared exponent, underflowing surrounding elements and destroying attention maps. To break this bottleneck, we propose Micro-Inverted-Scaling (MiX), a novel format that mathematically inverts the microscaling paradigm: rather than grouping multiple mantissas under one shared exponent, MiX groups private, per-element exponents under a single shared mantissa. To handle asymmetric VLM outlier topologies, we introduce an adaptive dual-format (MiX-MX) inference framework. By algebraically factoring out the shared MiX mantissa, this framework maps to a custom accelerator, replacing multipliers with efficient shifters. Evaluated end-to-end on multiple VLMs, our 4.5-bit MiX formulation exhibits equivalent or superior accuracy on multi-modal benchmarks compared to NVFP4. Simultaneously, the MiX accelerator delivers a 25% improvement in area efficiency over the NVFP4 baseline and a 2.3-4.5x speedup with 1.4-2.9x energy reduction across models compared to the state-of-the-art accelerator Focus, proving the inverted-scaling datapath is physically superior for efficient VLM deployment.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 8 |
| rigor | 11 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: microscaling, quantization, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yuan Liao, Jae-sun Seo
- 发布：2026-09-17；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
