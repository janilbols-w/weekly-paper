---
title: "Subspace-Aware Sparse Autoencoders for Effective Mechanistic Interpretability"
description: "Sparse Autoencoders (SAEs) are widely used for mechanistic interpretability in large language models, yet their standard formulation assigns each latent feature a single decoder direction, implicitly assuming features to be one-dimensional."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.06333) · [PDF](https://arxiv.org/pdf/2606.06333)

## 一句话摘要

Sparse Autoencoders (SAEs) are widely used for mechanistic interpretability in large language models, yet their standard formulation assigns each latent feature a single decoder direction, implicitly assuming features to be one-dimensional.

## 为什么值得关注

待编辑增强。

## 摘要原文

Sparse Autoencoders (SAEs) are widely used for mechanistic interpretability in large language models, yet their standard formulation assigns each latent feature a single decoder direction, implicitly assuming features to be one-dimensional. We show that this assumption can induce feature splitting when model features are multi-dimensional. Geometrically, accurately reconstructing a feature under a fixed co-activation budget can require exponentially many decoder directions as its dimension grows. From an optimization perspective, adding decoder directions can strictly lower the $\ell_1$-regularized population risk, even when a basis can already reconstruct the feature exactly. Motivated by these results, we introduce Subspace-Aware Sparse Autoencoders (SASA), which replace single-vector decoders with learned subspaces, enforce sparsity through Top-$s$ group gating, and adapt group rank with nuclear-norm regularization. Under an idealized single-feature model, we prove that the SASA objective is minimized by a single group whose reconstruction map recovers the feature subspace. We also derive polynomial sample complexity bounds for subspace estimation within a group and a lower bound on the samples needed to observe every atom in a fixed fragmented dictionary. Experiments on GPT-2 and Mistral-7B show reduced absorption compared with SAEs. Matched-budget GPT-2 comparisons show lower absorption for concept families and more accurate prediction of their members using a small number of latent coordinates, at a reconstruction cost. The code is available at https://github.com/arshandalili/sasa.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Seyed Arshan Dalili, Mehrdad Mahdavi
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/arshandalili/sasa](https://github.com/arshandalili/sasa)
- 阅读深度：metadata
