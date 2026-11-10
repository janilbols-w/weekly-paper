---
title: "Dual-Rate Diffusion: Accelerating diffusion models with an interleaved heavy-light network"
description: "Diffusion models achieve state-of-the-art generative performance but suffer from high computational costs during inference due to the repeated evaluation of a heavy neural network."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.18190) · [PDF](https://arxiv.org/pdf/2605.18190)

## 一句话摘要

Diffusion models achieve state-of-the-art generative performance but suffer from high computational costs during inference due to the repeated evaluation of a heavy neural network.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion models achieve state-of-the-art generative performance but suffer from high computational costs during inference due to the repeated evaluation of a heavy neural network. In this work, we propose Dual-Rate Diffusion, a method to accelerate sampling by interleaving the execution of a heavy high-capacity context encoder and a light efficient denoising model. The context encoder is evaluated sparsely to extract high-dimensional features, which are effectively reused by the light denoising model at every step to refine the sample efficiently. This approach significantly accelerates inference without compromising sample quality. On ImageNet benchmarks, Dual-Rate Diffusion matches the performance of standard baselines while reducing computational cost by a factor of $2$-$4$. Furthermore, we demonstrate that our method is compatible with distillation techniques, such as Moment Matching Distillation, enabling further efficiency gains in few-step generation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Grigory Bartosh, David Ruhe, Emiel Hoogeboom, Jonathan Heek, Thomas Mensink, Tim Salimans
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
