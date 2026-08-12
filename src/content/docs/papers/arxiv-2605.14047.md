---
title: "Evolving Layer-Specific Scalar Functions for Hardware-Aware Transformer Adaptation"
description: "Vision Transformers (ViTs) achieve state-of-the-art performance on challenging vision tasks, but their deployment on edge devices is severely hindered by the computational complexity and global reduction bottleneck imposed by layer normalization."
---

**评分：42/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2605.14047) · [PDF](https://arxiv.org/pdf/2605.14047)

## 一句话摘要

Vision Transformers (ViTs) achieve state-of-the-art performance on challenging vision tasks, but their deployment on edge devices is severely hindered by the computational complexity and global reduction bottleneck imposed by layer normalization.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision Transformers (ViTs) achieve state-of-the-art performance on challenging vision tasks, but their deployment on edge devices is severely hindered by the computational complexity and global reduction bottleneck imposed by layer normalization. Recent methods attempt to bypass this by replacing normalization layers with hardware-friendly scalar approximations. However, these homogeneous replacements do not optimally fit to all layers' behaviour and rely on expensive model retraining. In this work, we propose a highly efficient, hardware-aware framework that utilizes genetic programming (GP) to evolve heterogeneous, layer-specific scalar functions directly from pre-trained weights. Coupled with a novel post-training re-alignment strategy, our approach eliminates the need to retrain models from scratch entirely. Our evolved expressions accurately approximate the target normalization behaviours, capturing $90\%$ of the variance ($R^2$) compared to only $70.2\%$ for homogeneous baselines, allowing our modified architecture to recover $84.32\%$ Top-1 ImageNet-1K accuracy in only 20 epochs. By preserving this performance while eliminating the global reduction bottleneck, our approach achieves a strict reduction in both arithmetic complexity and off-chip memory traffic compared to standard LayerNorm, removing a primary barrier to the efficient deployment of ViTs on edge accelerators.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: hardware-aware
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kieran Carrigg, Sigur de Vries, Amirhossein Sadough, Marcel van Gerven
- 发布：2026-08-12；更新：2026-08-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
