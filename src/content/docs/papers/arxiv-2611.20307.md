---
title: "PoCoAttn: Position-Content Collaborative Sparse Attention for Fast and High-Fidelity Video Generation"
description: "Video diffusion transformers rely on 3D full attention over tens of thousands of spatiotemporal tokens, and its quadratic cost dominates inference latency."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.20307) · [PDF](https://arxiv.org/pdf/2611.20307)

## 一句话摘要

Video diffusion transformers rely on 3D full attention over tens of thousands of spatiotemporal tokens, and its quadratic cost dominates inference latency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Video diffusion transformers rely on 3D full attention over tens of thousands of spatiotemporal tokens, and its quadratic cost dominates inference latency. Sparse attention reduces this cost, but existing methods face a dilemma: static methods apply predefined masks and cannot capture input-dependent attention, whereas dynamic methods reconstruct the sparse mask repeatedly, paying online to rediscover positional structure that is largely stable across inputs. To this end, we propose PoCoAttn, a training-free sparse attention framework that separates input-stable from input-dependent attention and resolves the former offline and the latter online. PoCoAttn features: (1) A relative-offset analysis of 3D query-key pairs, which shows that video attention decomposes into an input-stable positional prior that carries most of the attention mass and a small content-dependent residual. (2) A position-content collaborative sparse attention mechanism, which retrieves positional keys from offline-calibrated tables, selects content keys online with a head-adaptive ratio between the two sources, and compensates for the discarded keys to approximate full attention. (3) A step-adaptive budget allocation algorithm, which models how early-step sparse attention errors are amplified along the denoising trajectory and derives the optimal sparsity budget per step. Extensive experiments across four video diffusion models and three tasks show that PoCoAttn consistently achieves a better speed-fidelity Pareto frontier than state-of-the-art (SOTA) methods, improving PSNR by 1.9 to 5.0 dB over baselines and delivering up to 4.1$\times$ attention and 2.0$\times$ denoising speedups over dense FlashAttention-3 attention.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jianwen Wu, Meiling Wang, Junkang Zhou, Yipeng Shen, Haoran You
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
