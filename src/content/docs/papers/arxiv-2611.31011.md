---
title: "Lorentz symmetry in self-supervised representation learning"
description: "Self-supervised learning (SSL) and explicit physical inductive biases have driven major advances in jet tagging, yet they are typically pursued along separate tracks."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.31011) · [PDF](https://arxiv.org/pdf/2611.31011)

## 一句话摘要

Self-supervised learning (SSL) and explicit physical inductive biases have driven major advances in jet tagging, yet they are typically pursued along separate tracks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Self-supervised learning (SSL) and explicit physical inductive biases have driven major advances in jet tagging, yet they are typically pursued along separate tracks. In this work, we unify both paradigms by integrating the Lorentz-equivariant Geometric Algebra Transformer slim (L-GATr-slim) architecture with the LeJEPA framework for representation learning. Pre-training on 100 million jets from the JetClass dataset, we optimize towards a latent space, which is invariant across physics-motivated jet augmentations. We demonstrate that enforcing Lorentz symmetry in the latent space is critical for representation quality and that this can be achieved either architecturally or learned via kinematic augmentations. With a standard non-invariant Transformer backbone, LeJEPA outperforms established autoregressive, masked particle modelling, and self-distillation baselines in linear- and MLP-probe accuracy, with L-GATr-slim providing further complementary gains. Across downstream benchmarks, our pre-trained models consistently outperform baselines trained from scratch or through different pre-training objectives.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Andreas Hermansen, Tobias Golling, Slava Voloshynovskiy
- 发布：2026-11-24；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
