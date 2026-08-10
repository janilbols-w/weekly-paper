---
title: "Lost in Interpolation: Why Predictive Feedback Fails in Diffusion Language Models"
description: "Soft-masking accelerates the convergence of Masked Diffusion Language Models (MDLMs)."
---

**评分：40/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2608.06529) · [PDF](https://arxiv.org/pdf/2608.06529)

## 一句话摘要

Soft-masking accelerates the convergence of Masked Diffusion Language Models (MDLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Soft-masking accelerates the convergence of Masked Diffusion Language Models (MDLMs). Existing formulations build this blend with linear interpolation (LERP) in the raw embedding space, which implicitly treats that space as Euclidean. We analyze the embedding space of MDLMs and find that the mask and predicted-token embeddings maintain a near-constant angle of (\approx 73^\circ) throughout training, while embedding norms remain essentially flat across vocabulary-frequency rank. These indicate a hyperspherical geometry, for which LERP is the wrong interpolation primitive. We introduce Spherical Soft-Masking (S-SM), a drop-in replacement that aggregates the top-(k) predictions with a Fr'echet mean on the hypersphere and blends this mean with the mask direction using spherical linear interpolation (SLERP), then restores the native mask norm. We evaluate S-SM on continued pre-training of a released 169M-parameter MDLM checkpoint across a wide range of inference-time step budgets, SLERP feedback avoids the training degradation that LERP feedback induces and delivers MAUVE gains of up to 2x over the vanilla MDLM baseline and 27.5-56.1% over TopK/LERP at various sampling budgets, alongside consistently lower generative perplexity (16.9-19.6% over the baseline), while leaving output entropy and convergence essentially unchanged.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Lavanya Nigam, Ishaan Bansal, Aryan Sood, Vidit Aggarwal, Gaurav Kumar Nayak
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
