---
title: "Flip, Don't Shuffle: Watermarking LLMs at the Speed of Inference"
description: "We introduce Stateless Bernoulli Watermarking (SBW), a new statistical watermark for Large Language Models that determines green list membership through independent per-token Bernoulli trials."
---

**评分：38/100** · LLM 高效推理 > Serving 与分布式推理 > 并行与通信

[论文原文](https://arxiv.org/abs/2609.03844) · [PDF](https://arxiv.org/pdf/2609.03844)

## 一句话摘要

We introduce Stateless Bernoulli Watermarking (SBW), a new statistical watermark for Large Language Models that determines green list membership through independent per-token Bernoulli trials.

## 为什么值得关注

待编辑增强。

## 摘要原文

We introduce Stateless Bernoulli Watermarking (SBW), a new statistical watermark for Large Language Models that determines green list membership through independent per-token Bernoulli trials. Unlike KGW's vocabulary permutation or SynthID's multi-layer tournament, SBW requires only a single comparison per token against a counter-based random number generator, reducing membership complexity to $O(1)$ and enabling single-kernel execution with zero intermediate allocations. We prove that this formulation preserves the same detection guarantees as fixed-size green lists: the z-score test remains $\mathcal{N}(0,1)$ under the null. The stateless architecture enables capabilities unavailable to existing methods: full-vocabulary self-salt watermarking (over 6000$\times$ faster than KGW's self-salt and 2$\times$ faster than SynthID despite biasing the entire vocabulary with candidate-dependent seeding) and architectural compatibility with distributed inference. In end-to-end generation benchmarks, SBW adds less than 1\% overhead at all batch sizes. We additionally identify hash function design as a previously unexplored axis for watermark quality, showing that a GPU-native Jenkins hash improves null calibration by 1.8$\times$ while producing more diverse text. Experiments across two seeding schemes and eight $(\gamma, \delta)$ configurations confirm statistical equivalence with ROC-AUC differences below 0.01.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distributed inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Simone Ceppi, Ignacio Sanchez
- 发布：2026-09-03；更新：2026-09-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
