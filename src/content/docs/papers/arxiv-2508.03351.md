---
title: "SalQ-VLM: Fine-Grained Saliency-Guided Quantization for Vision-Language Models"
description: "Large language models (LLMs) have demonstrated remarkable capabilities across diverse language tasks, motivating their extension to vision-language models (VLMs) for multimodal understanding."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2508.03351) · [PDF](https://arxiv.org/pdf/2508.03351)

## 一句话摘要

Large language models (LLMs) have demonstrated remarkable capabilities across diverse language tasks, motivating their extension to vision-language models (VLMs) for multimodal understanding.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) have demonstrated remarkable capabilities across diverse language tasks, motivating their extension to vision-language models (VLMs) for multimodal understanding. However, billion-parameter VLMs incur substantial memory and computational costs that hinder deployment in resource-constrained settings. Post-training quantization (PTQ) compresses models and accelerates inference without retraining, yet remains underexplored for VLMs. We identify two intrinsic VLM activation properties in PTQ: (1) visual over-representation, where vision tokens are excessive and often redundant, and (2) the modality gap separating text and vision tokens in the latent feature space. Prior methods largely overlook these properties, leading to quantization performance degradation. To address this mismatch, we propose SalQ-VLM, an importance-aware PTQ framework that prioritizes salient tokens and suppresses redundant vision tokens during calibration. We derive a gradient-driven importance factor that captures token-level importance variance and is theoretically grounded in the relationship among loss perturbation, activation errors, and output gradients. SalQ-VLM obtains this factor through a single lightweight block-wise gradient-caching pass and incorporates it into the layer-wise reconstruction objective. Because SalQ-VLM modifies only calibration, it adds no inference-time operations and remains compatible with existing high-performance kernels. Extensive evaluations across benchmarks and backbones show that SalQ-VLM consistently outperforms strong PTQ baselines, especially under ultra-low-bit quantization. Notably, it improves MME-RealWorld accuracy by 16.45% under INT2g128 quantization.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yufei Xue, Yushi Huang, Lunjie Zhu, Jiawei Shao, Jun Zhang
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
