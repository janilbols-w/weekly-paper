---
title: "TR-PTQ: High-Accuracy Integer-Only Transformer Post Training Quantization via Taylor Region Reformulation"
description: "Post-training quantization (PTQ) enables efficient deployment, yet transformer architectures remain challenging to quantize due to nonlinear layers."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.09969) · [PDF](https://arxiv.org/pdf/2610.09969)

## 一句话摘要

Post-training quantization (PTQ) enables efficient deployment, yet transformer architectures remain challenging to quantize due to nonlinear layers.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training quantization (PTQ) enables efficient deployment, yet transformer architectures remain challenging to quantize due to nonlinear layers. While existing methods attribute accuracy loss to insufficient numerical precision, often necessitating floating-point fallbacks, we demonstrate that degradation is actually driven by specific structural error sources. We find that learned scale parameters in normalization layers and compounded approximations in GELU are the primary error contributors, whereas SoftMax remains inherently robust to aggressive quantization. To address these bottlenecks, we introduce TR-PTQ, a unified integer-only formulation using shared Taylor Region (TR) exponential and logarithm primitives. This approach allows computationally expensive operations, including division and square roots, to be performed entirely in the log-domain via standard integer arithmetic. Combined with a calibration-free, outlier-aware optimization for LayerNorm parameters, our method eliminates the need for floating-point hardware units for nonlinearities, achieving less than 1.5\% absolute accuracy degradation across vision and language benchmarks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Eliyahu Levy, Adam Teman, Yoni Pugachov
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
