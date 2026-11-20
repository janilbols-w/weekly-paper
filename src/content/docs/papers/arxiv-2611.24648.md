---
title: "Zonotopic Analysis of Quantization Error in Neural Networks"
description: "Quantized neural networks achieve computational efficiency by reducing precision, but bounding their quantization error remains a challenge due to discrete rounding and clamping operations."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.24648) · [PDF](https://arxiv.org/pdf/2611.24648)

## 一句话摘要

Quantized neural networks achieve computational efficiency by reducing precision, but bounding their quantization error remains a challenge due to discrete rounding and clamping operations.

## 为什么值得关注

待编辑增强。

## 摘要原文

Quantized neural networks achieve computational efficiency by reducing precision, but bounding their quantization error remains a challenge due to discrete rounding and clamping operations. We present a zonotope-based abstract interpretation framework for quantized ReLU feed-forward network verification, introducing a unified round-clamp abstract transformer that jointly handles both operations. We extend this framework to constrained zonotopes, which add linear constraints to tighten bounds, and derive sound quantization error representations. We establish soundness and affine-strip optimality of the round-clamp abstract transformer, as well as convex-hull optimality of its complete constrained formulation. On the ACAS Xu benchmarks, our constrained zonotope method reduces average error-bound widths by approximately 70-85% and runtimes by 65-80% compared to QEBVerif's symbolic DRA propagation at the two smallest tested perturbation radii (r=3 and r=6). These improvements are not uniform across bitwidths, and symbolic DRA achieves tighter bounds at larger radii. Our plain zonotope method delivers competitive sound bounds nearly 300 times faster on average.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Robert Debbas, Éric Goubault, Sylvie Putot
- 发布：2026-11-18；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
