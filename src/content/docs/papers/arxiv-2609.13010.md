---
title: "Dual-guided Hierarchical Edge Localization for Large-scale Optimal Transport Across Dimensions"
description: "Optimal transport (OT) compares distributions and aligns datasets in machine learning, yet unregularized discrete OT requires a linear program with quadratically many transport variables."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2609.13010) · [PDF](https://arxiv.org/pdf/2609.13010)

## 一句话摘要

Optimal transport (OT) compares distributions and aligns datasets in machine learning, yet unregularized discrete OT requires a linear program with quadratically many transport variables.

## 为什么值得关注

待编辑增强。

## 摘要原文

Optimal transport (OT) compares distributions and aligns datasets in machine learning, yet unregularized discrete OT requires a linear program with quadratically many transport variables. We propose HELLO, a hierarchical solver that casts large-scale discrete OT as edge localization and uses dual potentials to guide both coarse-to-fine initialization and within-level refinement. Initialization propagates coarse dual potentials across a recursive subsampling hierarchy to assign candidate edges. Refinement then iteratively inserts the largest dual violators in each row and column until the relative KKT residual meets a prescribed tolerance, while budgeted pruning ensures linear memory complexity. For exact-arithmetic refinement, we prove finite termination at a global optimum under a symbolic lexicographic rule. At the million-point scale, HELLO attains lower transport objectives with order-of-magnitude runtime improvements over strong baselines across feature dimensions from single digits to thousands. It further scales to 1.28 million samples per marginal in 8192 dimensions on a single H100, using 41.6 GiB peak GPU memory while satisfying a full relative KKT residual below $10^{-6}$. Beyond standard discrete OT, the framework supports general pairwise costs and serves as a scalable balanced-OT oracle for semi-discrete OT, Gromov--Wasserstein, unbalanced OT, and OT-based Flow Matching.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Wenzhou Xia, Qiaoqiao Ding, Jingwei Liang, Xiaoqun Zhang
- 发布：2026-09-14；更新：2026-09-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
