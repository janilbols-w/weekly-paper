---
title: "FastKron: Efficient Quantization with Kronecker-Factored Hessians"
description: "We accelerate a family of algorithms for neural network quantization which utilize a two-sided version of the GPTQ/LDLQ algorithm."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.06291) · [PDF](https://arxiv.org/pdf/2608.06291)

## 一句话摘要

We accelerate a family of algorithms for neural network quantization which utilize a two-sided version of the GPTQ/LDLQ algorithm.

## 为什么值得关注

待编辑增强。

## 摘要原文

We accelerate a family of algorithms for neural network quantization which utilize a two-sided version of the GPTQ/LDLQ algorithm. Standard GPTQ-style adaptive rounding uses one-sided correlation information derived from input activations. A natural two-sided extension can additionally capture correlations across output channels. It utilizes a general Kronecker-factored approximation of the weight matrix curvature. This approach has been used in BoA and YAQA. But making a concrete algorithmic implementation of this two-sided GPTQ variant is nontrivial. BoA uses a large number of sequential steps, while YAQA improves over the sequential depth but still has quartic total cost. We introduce FastKron, an efficient algorithmic implementation that combines anti-diagonal parallelism with a recursive divide-and-conquer construction. For an $m\times n$ weight matrix, FastKron uses $O(m+n)$ sequential steps while reducing the total work from $O(m^2n^2)$ to $O(mn(m+n))$. Thus, it matches the cubic scaling of GPTQ while exploiting richer curvature information. Moreover, FastKron is modular with respect to both the base quantizer and the Hessian estimator. We also provide practical benchmarks, consider a range of Hessian approximations that FastKron can be used with, and provide an efficient technique to compute these Hessians.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Johann Birnick, Rayan Saab
- 发布：2026-08-06；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
