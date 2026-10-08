---
title: "Algorithmic Scratchpads and Curriculum Staging for Arithmetic Reasoning in Tiny Transformers"
description: "Autoregressive Large Language Models (LLMs) frequently struggle with deterministic multi-step algorithmic tasks such as multi-digit multiplication and long division."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2610.09003) · [PDF](https://arxiv.org/pdf/2610.09003)

## 一句话摘要

Autoregressive Large Language Models (LLMs) frequently struggle with deterministic multi-step algorithmic tasks such as multi-digit multiplication and long division.

## 为什么值得关注

待编辑增强。

## 摘要原文

Autoregressive Large Language Models (LLMs) frequently struggle with deterministic multi-step algorithmic tasks such as multi-digit multiplication and long division. In this paper, we investigate the mechanics of multi-step arithmetic in compact "Tiny" Transformers (~10.6M non-embedding parameters, 49.3M total) trained on synthetic data across four basic operations (+, -, *, /) unrolled as step-by-step scratchpads. First, we establish the necessary training foundations: (1) dataloader sequence padding creates an 83% gradient starvation artifact that collapses accuracy from 40% to 1%, remediated via continuous sequence packing; (2) linguistic pretraining is an essential prerequisite (<= 2.0% without it); and (3) modern architectural primitives (RoPE, RMSNorm, SwiGLU) and Sparse Mixture of Experts (MoE) substantially improve additive reasoning over baseline GPT-2. Second, we demonstrate that algorithmic scratchpad formulation directly dictates success. Introducing a deterministic Digit-by-Digit Long Division scratchpad within a 4-stage Hierarchical Developmental Curriculum dramatically elevates single-digit division from 4.0% to 86.7% accuracy on a 4,000-problem held-out benchmark. In contrast, multi-digit multiplication remained challenging: detailed error analysis revealed that while the model correctly computed single-digit sub-products and place-value zeros, our FOIL scratchpad failed because it forced a simultaneous summation of up to nine multi-digit terms in a single step without pairwise intermediate accumulation. Finally, we identify two key boundaries: performance collapses to 0.00% on unseen 4-digit operands, and unbuffered training induces catastrophic forgetting, collapsing division accuracy from 86.7% down to 0.00%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: mixture of experts
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sourabh Kasliwal
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
