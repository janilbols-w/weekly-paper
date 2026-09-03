---
title: "Shiva-DiT: Residual-Based Differentiable Top-$k$ Selection for Efficient Diffusion Transformers"
description: "Diffusion Transformers (DiTs) are costly at high resolution because self-attention scales quadratically with token sequence length."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2602.05605) · [PDF](https://arxiv.org/pdf/2602.05605)

## 一句话摘要

Diffusion Transformers (DiTs) are costly at high resolution because self-attention scales quadratically with token sequence length.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion Transformers (DiTs) are costly at high resolution because self-attention scales quadratically with token sequence length. Existing pruning methods do not jointly provide end-to-end learnability, low training overhead, and deterministic token counts for predictable token-dependent computation. We propose Shiva-DiT, based on Residual-Based Differentiable Top-k Selection. Its forward pass executes hard top-k selection, while a residual-aware straight-through estimator propagates gradients to both token scores and the budget k without evaluating a second backbone path. A Context-Aware Router and Adaptive Ratio Policy learn layer- and timestep-dependent retention schedules under a target average budget. Experiments on SD3-Medium, Flux.1-dev, and PixArt-{\Sigma} show consistent reductions in FLOPs and measured latency. On SD3-Medium, Shiva-DiT provides four fidelity-latency operating points and reaches a 1.54x wall-clock speedup with competitive fidelity.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jiaji Zhang, Hailiang Zhao, Jiaju Wu, Ruichao Sun, Xinkui Zhao, Shuiguang Deng
- 发布：2026-09-03；更新：2026-09-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
