---
title: "hyperbolix: Hyperbolic Deep Learning in JAX"
description: "We present hyperbolix, an open-source library for hyperbolic deep learning in JAX, built on Flax NNX."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.28248) · [PDF](https://arxiv.org/pdf/2609.28248)

## 一句话摘要

We present hyperbolix, an open-source library for hyperbolic deep learning in JAX, built on Flax NNX.

## 为什么值得关注

待编辑增强。

## 摘要原文

We present hyperbolix, an open-source library for hyperbolic deep learning in JAX, built on Flax NNX. To our knowledge, it is the first comprehensive, general-purpose hyperbolic deep learning library in JAX. It includes six manifolds with a common interface: Euclidean space, the Poincar\'e ball, the hyperboloid, the $\kappa$-stereographic model, mixed-curvature product spaces, and the proper velocity space. We implement layer families that cover linear layers, convolutions, attention, normalization, positional encoding, regression, and vector quantization. These building blocks span methods ranging from Ganea's original hyperbolic neural networks to recent fully hyperbolic architectures such as Hypformer and Lorentzian ResNet. Additionally, hyperbolix contains Riemannian optimizers implemented as optax transformations, wrapped distributions, and hyperbolic dimensionality-reduction techniques. Its API uses idiomatic JAX: Manifolds are stateless, with curvature being passed at call time, while manifold operations act on single points, with jax.vmap enabling batch operations. The precision of every checked operation is tested against a closed-form NumPy/SciPy transcription from the source paper or a finite difference, for both float32 and float64. On the hyperboloid, standard formulas for two-point operations, such as the distance, lose precision far from the origin, because they subtract two large, nearly equal terms. hyperbolix replaces these subtractions with cancellation-free formulas that stay accurate in float32 at distances where prior implementations return NaN. hyperbolix is available under the MIT license at https://github.com/timoklein/hyperbolix .

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Timo Klein, Thomas Lang, Yllka Velaj, Sebastian Tschiatschek
- 发布：2026-09-23；更新：2026-09-24
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/timoklein/hyperbolix](https://github.com/timoklein/hyperbolix)
- 阅读深度：metadata
