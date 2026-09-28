---
title: "Aligning One-Step Generative Models with Reward-Weighted Transport Distillation"
description: "One-step generators enable high-quality visual generation with a single network evaluation, but their post-training is difficult: general implicit generators provide neither tractable likelihoods nor denoising trajectories, and many rewards are non-differentiable."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.30840) · [PDF](https://arxiv.org/pdf/2609.30840)

## 一句话摘要

One-step generators enable high-quality visual generation with a single network evaluation, but their post-training is difficult: general implicit generators provide neither tractable likelihoods nor denoising trajectories, and many rewards are non-differentiable.

## 为什么值得关注

待编辑增强。

## 摘要原文

One-step generators enable high-quality visual generation with a single network evaluation, but their post-training is difficult: general implicit generators provide neither tractable likelihoods nor denoising trajectories, and many rewards are non-differentiable. We introduce Reward-Weighted Transport Distillation (RWTD), a post-training method that requires only generated samples and scalar reward evaluations. Rather than aligning solely to the conventional reward-tilted reference distribution, RWTD constructs an adaptive target that mixes separately tilted current and reference distributions. The current component incorporates improvements discovered during training, while the reference component anchors the target to the pretrained generator. RWTD realizes this target through feature-space optimal transport and fixed-point regression. Theoretical analysis shows that the fixed-point distributions of RWTD interpolate between off-policy reward tilting of the reference and on-policy tilting of the current model, providing a principled approach to balancing reward adaptation with retention of prior knowledge. Empirically, RWTD substantially improves the GenEval score of the one-step SANA Sprint 1.6B backbone from 0.73 to 0.80, while separate preference alignment experiments demonstrate strong cross-reward generalization that yields balanced improvements and preservation of compositional capabilities.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Austin Wang, Ziheng Cheng, Lexing Ying
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
