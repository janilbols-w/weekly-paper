---
title: "B$^3$-PWL: GPU-Batched Branch-and-Bound for Piecewise-Linear Optimization with SOS2 Constraints"
description: "Piecewise-linear (PWL) optimization problems arise in many mixed-integer programming (MIP) optimization applications, including portfolio optimization, workforce scheduling, and resource allocation."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.28988) · [PDF](https://arxiv.org/pdf/2608.28988)

## 一句话摘要

Piecewise-linear (PWL) optimization problems arise in many mixed-integer programming (MIP) optimization applications, including portfolio optimization, workforce scheduling, and resource allocation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Piecewise-linear (PWL) optimization problems arise in many mixed-integer programming (MIP) optimization applications, including portfolio optimization, workforce scheduling, and resource allocation. But solving them to global optimality remains computationally expensive because branch-and-bound repeatedly solves LP relaxation subproblems. Existing solvers are largely CPU-centric, leaving the scalability of modern GPUs underutilized. Few prior GPU-accelerated branch-and-bound either targets neural network which is not suitable for general PWL optimization, or accelerates only auxiliary subroutines such as strong branching heuristics within CPU-centric MIP solvers. To bridge this gap, we propose B$^3$-PWL, a GPU-centric batched branch-and-bound framework for piecewise-linear optimization with Special Ordered Set of type 2 (SOS2) constraints. Our method solves batches of LP relaxation subproblems concurrently on the GPU using a first-order primal-dual solver, enabled by a specialized batched block-tiled sparse matrix kernel. To complement bound computation, we further introduce a unified feasibility search module that combines an SOS2 repair primal heuristic with a batched feasibility pump to rapidly obtain feasible incumbents and improve pruning efficiency. On a benchmark of 43 PWL-MIP instances, B$^3$-PWL achieves a 9.25x geometric-mean speedup over NVIDIA cuOpt while reaching high-quality feasible incumbents on every tested instance. On a public valve-point unit-commitment benchmark, it further outperforms NVIDIA cuOpt and the open-source CPU solvers SCIP and HiGHS, demonstrating the potential of first-order LP methods as the central engine of GPU-accelerated branch-and-bound.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yilin Guan, Shuqing Luo, Pingzhi Li, Tianlong Chen, Kaidi Xu
- 发布：2026-08-29；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
