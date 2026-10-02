---
title: "Manifold-Constrained Initial Noise Optimization for Efficient Generative Model Alignment"
description: "Recent advances in distillation and flow-map models have enabled deterministic one- or few-step generation for high-quality data, facilitating a new branch of reward alignment approaches that directly optimize the initial noise from a Gaussian distribution."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.00365) · [PDF](https://arxiv.org/pdf/2610.00365)

## 一句话摘要

Recent advances in distillation and flow-map models have enabled deterministic one- or few-step generation for high-quality data, facilitating a new branch of reward alignment approaches that directly optimize the initial noise from a Gaussian distribution.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent advances in distillation and flow-map models have enabled deterministic one- or few-step generation for high-quality data, facilitating a new branch of reward alignment approaches that directly optimize the initial noise from a Gaussian distribution. However, most existing initial-noise optimization methods rely on first-order gradient information, which is either inapplicable or suffers from instability and inefficiency in black-box reward scenarios. Here, we introduce ZeNOVA, a stable and efficient initial noise alignment method in a gradient-free manner. Specifically, we address existing algorithms' major challenge in black-box scenarios through annealed soft-value guidance, manifold-constrained hyperspherical Langevin dynamics, and Metropolis-Hastings jumping. Extensive experiments on image and video generative models show that ZeNOVA outperforms all evaluated zeroth-order baselines by optimizing the initial noise toward higher rewards substantially more stably while exploiting the geometry of the Gaussian prior, demonstrating its practical applicability to various black-box reward alignment.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jinho Chang, Jong Chul Ye
- 发布：2026-10-02；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
