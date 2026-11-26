---
title: "Randomized Forward Mode of Automatic Differentiation For Optimization Algorithms"
description: "Reverse mode automatic differentiation (AD) computes a gradient in a single sweep, but at a memory cost that grows with the length of the computational graph."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2310.14168) · [PDF](https://arxiv.org/pdf/2310.14168)

## 一句话摘要

Reverse mode automatic differentiation (AD) computes a gradient in a single sweep, but at a memory cost that grows with the length of the computational graph.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reverse mode automatic differentiation (AD) computes a gradient in a single sweep, but at a memory cost that grows with the length of the computational graph. That cost becomes the binding constraint when the graph is long, as in parameter identification governed by differential equations or in training on memory-limited hardware. We study a randomized forward mode gradient (RFG) as an alternative to backpropagation in precisely this regime. RFG is a random gradient estimator built from the directional derivative along a random vector, a quantity that forward mode AD computes without storing a tape. Replacing the gradient with RFG yields a class of optimization algorithms; for RFG-based gradient descent (GD) and Polyak's heavy ball (PHB) methods, we establish convergence results on quadratic functions. The analysis reveals that using random vectors from a probability distribution with the smallest kurtosis yields the fastest rate of convergence. Computational experiments demonstrate the performance of the proposed algorithms and verify the theoretical findings, including beyond quadratic functions. We further characterize when RFG is computationally preferable to backpropagation. Since the variance of RFG grows with the parameter dimension $d$ while the memory required by the reverse mode grows with the length $\ell$ of the computational graph, the relevant figure of merit is the ratio $\ell/d$. We confirm this by measurement against reverse mode with checkpointing. For a physics-informed neural network, where $d$ is large and $\ell$ short, RFG is not competitive. For parameter identification governed by differential equations, where a handful of coefficients is recovered from a long time integration, RFG requires one to three orders of magnitude less memory. The price is a larger iteration count, which leaves its time to solution comparable to or worse than a well-tuned reverse mode.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpointing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Khemraj Shukla, Yeonjong Shin
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
