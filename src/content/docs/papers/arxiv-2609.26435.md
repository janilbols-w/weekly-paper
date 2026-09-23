---
title: "One-Step Generative Surrogate Models via Block-Triangular Joint Drifting"
description: "Drifting provides a direct route to one-step generative models, but applying it directly to stochastic transition modeling requires multiple samples of the next state conditioned on the same current state."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.26435) · [PDF](https://arxiv.org/pdf/2609.26435)

## 一句话摘要

Drifting provides a direct route to one-step generative models, but applying it directly to stochastic transition modeling requires multiple samples of the next state conditioned on the same current state.

## 为什么值得关注

待编辑增强。

## 摘要原文

Drifting provides a direct route to one-step generative models, but applying it directly to stochastic transition modeling requires multiple samples of the next state conditioned on the same current state. Standard trajectory data, however, typically provide only one realized next state for each observed current state and therefore do not provide an empirical approximation of the corresponding conditional distribution over possible next states. We introduce block-triangular joint drifting, which instead applies a projected drift field to the empirically accessible joint distribution of consecutive states. Importantly, the block-triangular architecture preserves the current-state marginal while making its second component a direct sampler of the conditional distribution of possible next states. The resulting surrogate generates stochastic trajectories with one model evaluation per time step, without auxiliary generative steps between time steps. Numerical experiments demonstrate accurate marginal and trajectory-dependent statistics and favorable accuracy-cost tradeoffs compared with deterministic, diffusion-, flow-, and distillation-based generative surrogate models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Nicholas Geissler, Shreya Jha, Ricardo Baptista, Benjamin Peherstorfer
- 发布：2026-09-23；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
