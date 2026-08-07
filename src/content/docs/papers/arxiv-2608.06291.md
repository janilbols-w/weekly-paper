---
title: "BaKron: Efficient Quantization with Kronecker-Factored Hessians"
description: "We accelerate a family of algorithms for neural network quantization whose geometry is informed by any Kronecker-factored approximation of the Hessian."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.06291) · [PDF](https://arxiv.org/pdf/2608.06291)

## 一句话摘要

We accelerate a family of algorithms for neural network quantization whose geometry is informed by any Kronecker-factored approximation of the Hessian.

## 为什么值得关注

待编辑增强。

## 摘要原文

We accelerate a family of algorithms for neural network quantization whose geometry is informed by any Kronecker-factored approximation of the Hessian. GPTQ-style adaptive rounding typically uses one-sided information derived from input activations. Two-sided Kronecker-factored Hessian approximations can additionally capture correlations across output coordinates, but applying GPTQ directly in the vectorized weight domain is computationally expensive. Building on the two-sided adaptive-rounding formulation used by BoA and YAQA, we introduce BaKron, an efficient solver that combines anti-diagonal parallelism with a recursive divide-and-conquer construction. For an $m\times n$ weight matrix, BaKron uses $O(m+n)$ sequential steps while reducing the total work from $O(m^2n^2)$ to $O(mn(m+n))$. Thus, it matches the cubic scaling of GPTQ while exploiting richer curvature information. Moreover, BaKron is modular with respect to both the base quantizer and the Hessian estimator. We also provide practical benchmarks, consider a range of Hessians that BaKron can be called with, find an efficient technique to compute these Hessians, and evaluate the algorithm experimentally.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Johann Birnick, Rayan Saab
- 发布：2026-08-06；更新：2026-08-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
