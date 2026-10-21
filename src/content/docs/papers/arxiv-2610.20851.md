---
title: "Complete or Sparse: A Tale of Two Identifiabilities"
description: "Understanding when neural networks learn interpretable representations is central to mechanistic interpretability."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2610.20851) · [PDF](https://arxiv.org/pdf/2610.20851)

## 一句话摘要

Understanding when neural networks learn interpretable representations is central to mechanistic interpretability.

## 为什么值得关注

待编辑增强。

## 摘要原文

Understanding when neural networks learn interpretable representations is central to mechanistic interpretability. We study this through identifiability: when can supervised learning recover the true latent variables underlying the data? We introduce two data generating processes distinguished by their causal direction where either labels cause latents (generative) or latents cause labels (discriminative). When the representation has at least as many dimensions as the latent space, we prove that the optimal encoders are linear in the latents. Conversely, when dimensions are insufficient, identifiability generically fails and encoders become nonlinear. We then show that additional constraints yield recovery of individual latent variables, not just linear mixtures. In the generative setting, non-negative activations and energy efficiency force each neuron to encode exactly one latent, providing a precise account of selective grandmother cell-like responses. In the discriminative setting, when latents are sparse and the true measurement matrix satisfies the spark condition, the learned encoder inherits compressed sensing structure, enabling sparse dictionary learning to perfectly recover individual latents. This constitutes, to our knowledge, the first identifiability result for undercomplete nonlinear independent component analysis. Our framework unifies nonlinear ICA, compressed sensing, and neural network interpretability, delineating exactly when representations transition from nonlinear distortions to linear representations and, under additional constraints or steps, to clean, axis-aligned codes. Theoretical predictions are validated on synthetic benchmarks and on activations drawn from vision models, large language models, and macaque inferotemporal cortex.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Junze Zhou, David Klindt
- 发布：2026-10-14；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
