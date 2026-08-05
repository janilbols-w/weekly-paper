---
title: "IPPRO: Importance-based Pruning with PRojective Offset for Magnitude-indifferent Structural Pruning"
description: "Importance-based structured pruning overwhelmingly relies on filter magnitude."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2507.14171) · [PDF](https://arxiv.org/pdf/2507.14171)

## 一句话摘要

Importance-based structured pruning overwhelmingly relies on filter magnitude.

## 为什么值得关注

待编辑增强。

## 摘要原文

Importance-based structured pruning overwhelmingly relies on filter magnitude. This proxy is fundamentally flawed: due to scale invariance, functionally identical filters can receive arbitrarily different importance scores under rescaling. We propose IPPRO (Importance-based Pruning with PROjective Offset), a scale-invariant pruning framework grounded in projective geometry. By embedding filters into real projective space ($\mathbb{RP}^N$), IPPRO resolves the singularity at the origin, placing all filters at an equal angular distance from the zero filter. We define PROscore, which captures functional importance by measuring a filter's angular displacement toward zero under a single gradient step (directional collapse). We further connect PROscore to exact $L_0$ relaxation, proving this one-shot criterion reliably predicts multi-step pruning dynamics. Extensive experiments across CNNs, Vision Transformers, and LLMs (e.g., ResNet, DeiT, LLaMA) demonstrate that IPPRO consistently outperforms existing methods, yielding particularly striking gains under high compression and no-fine-tuning regimes, IPPRO establishes a robust, architecture-agnostic paradigm for neural network compression.

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

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jaeheun Jung, Jaehyuk Lee, Yeajin Lee, Donghun Lee
- 发布：2026-08-05；更新：2026-08-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
