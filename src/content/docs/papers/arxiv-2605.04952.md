---
title: "Adaptive Inverted-Index Routing for Granular Mixtures-of-Experts"
description: "Sparse Mixture-of-experts (MoE) models enable scalable transformer architectures by activating only a subset of experts per token."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2605.04952) · [PDF](https://arxiv.org/pdf/2605.04952)

## 一句话摘要

Sparse Mixture-of-experts (MoE) models enable scalable transformer architectures by activating only a subset of experts per token.

## 为什么值得关注

待编辑增强。

## 摘要原文

Sparse Mixture-of-experts (MoE) models enable scalable transformer architectures by activating only a subset of experts per token. Recent evidence suggests that performance improves with increasingly granular experts, i.e., many small experts instead of a few large ones. However, this regime substantially increases routing cost, which can dominate computation and memory. We introduce adaptive inverted-index routing for MoE (AIR-MoE), an inverted-index-inspired routing architecture based on vector quantization (VQ). In a first stage, AIR-MoE performs coarse shortlisting by assigning tokens to VQ codewords to construct a candidate set of experts. In a second stage, fine scoring computes exact routing scores restricted to this shortlist. This two-stage procedure approximates true top-K routing while avoiding full expert scoring and, in contrast to prior work, imposing no structural constraints on expert parameters. AIR-MoE serves as a drop-in replacement for standard routers and requires no modifications to the model architecture or loss function. We further provide a lower bound on the mass recall achieved by AIR-MoE that yields insights into the inner workings. Empirically, AIR-MoE improves the perplexity-FLOPs trade-off over existing MoE routers in regimes with up to more than a million tiny experts, and achieves consistent perplexity improvements over the best existing baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Klaus-Rudolf Kladny, Maximilian Mordig, Bernhard Sch\"olkopf, Michael Muehlebach
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
