---
title: "Recti-Q: Feature-Space Rectification for Out-of-Distribution-Robust Quantized Perception in Edge Robotics"
description: "Robotic perception pipelines increasingly rely on large vision backbones deployed on SWaP-constrained edge platforms, making post-training quantization (PTQ) attractive for real-time inference."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2607.18540) · [PDF](https://arxiv.org/pdf/2607.18540)

## 一句话摘要

Robotic perception pipelines increasingly rely on large vision backbones deployed on SWaP-constrained edge platforms, making post-training quantization (PTQ) attractive for real-time inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Robotic perception pipelines increasingly rely on large vision backbones deployed on SWaP-constrained edge platforms, making post-training quantization (PTQ) attractive for real-time inference. However, while PTQ often preserves clean in-distribution accuracy, we show that it can substantially degrade reliability under deployment-relevant distribution shifts (e.g., sensor noise, severe weather, and novel operating environments), creating a Quantization-Induced Robustness Gap. Across foundational vision benchmarks (ImageNet-C and PACS), 4-bit PTQ models exhibit pronounced robustness degradation despite negligible ID accuracy loss. To address this, we propose Recti-Q, a lightweight feature-space rectification framework that freezes the quantized backbone and trains a small classifier-head LoRA adapter using only source data. Recti-Q is architecture-agnostic across CNNs and Transformers, supports efficient teacher-free training, and recovers a significant portion of the lost robustness, in some cases matching or exceeding FP32 performance. At less than 1% parameter overhead (as small as 6 KB), Recti-Q preserves over 99% of PTQ memory savings, adds negligible compute, and enables low-bandwidth Over-The-Air (OTA) resilience patching for deployed robotic fleets operating in unpredictable physical environments.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hamidreza Yaghoubi Araghi, Parastoo Pilevar, Ming C. Lin
- 发布：2026-08-07；更新：2026-08-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
