---
title: "Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered"
description: "Vision-Language-Action (VLA) models are a promising paradigm for field robotics, but their deployment is bottlenecked by strict edge SWaP-C constraints."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2510.08464) · [PDF](https://arxiv.org/pdf/2510.08464)

## 一句话摘要

Vision-Language-Action (VLA) models are a promising paradigm for field robotics, but their deployment is bottlenecked by strict edge SWaP-C constraints.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision-Language-Action (VLA) models are a promising paradigm for field robotics, but their deployment is bottlenecked by strict edge SWaP-C constraints. Compression techniques such as quantization, distillation, and pruning are well-established for LLMs and VLMs. Pruning, however, remains particularly underexplored for VLA models. We surprisingly find that pruning VLA models yields drastic performance degradation and increased safety violations. Through spectral analysis, we identify structural properties of VLA weights that help explain this fragility. Based on this insight, we introduce GLUESTICK, a post-pruning recovery method that restores much of the original model's capability while preserving sparsity benefits. GLUESTICK computes a one-time corrective term by interpolating between the dense and pruned models in weight space. At inference, each pruned layer applies this correction to recover lost performance with minimal overhead. Our approach requires no additional training and is agnostic to the pruning algorithm. Across diverse VLA architectures and domains, GLUESTICK recovers up to 100% of the success rate and restores safety to near-dense levels, while saving up to 5 GB of memory and achieving up to 1.75x speedup. Additional material can be found at: https://gluestick-vla.github.io/

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation, pruning, sparsity
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jason Jabbour, Dong-Ki Kim, Max Smith, Jay Patrikar, Radhika Ghosal, Youhui Wang, Ali Agha, Vijay Janapa Reddi, Shayegan Omidshafiei
- 发布：2026-10-15；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
