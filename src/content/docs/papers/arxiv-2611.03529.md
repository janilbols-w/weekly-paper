---
title: "ParaDeAl: Parallel Descent Algorithms for Sparse Statistics"
description: "Best subset selection is a central problem in statistical regression, drawing increasing attention from the broader optimization and machine learning communities."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.03529) · [PDF](https://arxiv.org/pdf/2611.03529)

## 一句话摘要

Best subset selection is a central problem in statistical regression, drawing increasing attention from the broader optimization and machine learning communities.

## 为什么值得关注

待编辑增强。

## 摘要原文

Best subset selection is a central problem in statistical regression, drawing increasing attention from the broader optimization and machine learning communities. Solving the hard L0 sparsity constraint directly has been computationally challenging; as a result, most existing work proposes formulations which do not enforce the constraint, but instead use a mix of L0/L1/L2 penalties to encourage sparsity. Modern methods for solving such penalized formulations are tractable for p = 100,000, but give up direct control over sparsity. In this paper, we propose a two-stage proximal gradient descent-based approach which both enforces the sparsity constraint and incorporates L1/L2 penalties, leveraging GPUs for computational acceleration to find approximate solutions. Our method, ParaDeAl, offers the user the ability to select the problem hyperparameters, solves all configurations in parallel, and obtains solutions up to 15x faster than the best state-of-the-art CPU competitors while achieving almost identical test accuracy for the same support size for large (p > 100,000) synthetic and real-world datasets.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Adam Deng, Rahul Mazumder
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
