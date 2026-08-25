---
title: "Tensor Seeks Layout: Formalizing Layout Selection for ML Compilers"
description: "Modern machine learning compilers select tensor memory layouts to minimize execution cost under hardware constraints."
---

**评分：39/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2608.21555) · [PDF](https://arxiv.org/pdf/2608.21555)

## 一句话摘要

Modern machine learning compilers select tensor memory layouts to minimize execution cost under hardware constraints.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern machine learning compilers select tensor memory layouts to minimize execution cost under hardware constraints. Layout selection is global: an operator may be fastest under one layout while its consumers prefer another, and aligning these preferences requires explicit layout conversions that can hurt model performance. Despite its practical importance, layout selection lacks a formal basis, so current compilers rely on ad-hoc heuristics. This paper presents the first formal study of layout selection in machine learning compilers. We formulate the problem as combinatorial optimization over dataflow graphs, minimizing the sum of operator execution costs and the per-tensor cost of these conversions. Our theoretical analysis shows that optimal layout selection is computationally hard, even for programs containing only matrix multiplications over two-dimensional tensors. We design an optimal polynomial-time algorithm for dataflow graphs of bounded treewidth. For general instances, we give a weighted MaxSAT encoding that an off-the-shelf solver can optimize. The formulation unifies several existing layout optimization strategies, including XLA's layout assignment, partition dimension selection in systolic array compilers, and layout planning in mobile GPU optimizers. We implement the formalization in a production compiler for an AI accelerator and measure the execution time of the compiled models under greedy heuristics, the compiler's rule-based strategy, and an optimal solver. Simple heuristics degrade execution time by up to $5\times$ on some workloads. Where the compiler's cost model is accurate, the solver matches or beats the rule-based strategy. On workloads with complex data movement it falls behind, and since the solver minimizes the stated objective exactly, that gap isolates cost-model error from search quality, showing where compiler effort actually pays off.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Clemens Eisenhofer, Yuwen Jia, Daniel Kroening, Sergey Pupyrev
- 发布：2026-08-25；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
