---
title: "ReWY: Faster Backpropagation for Delta-Rule Attention - From 7 to 3 Matrix Multiplications"
description: "Delta-rule linear attention underlies language models such as Kimi Linear and Qwen3-Next."
---

**评分：43/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2611.01940) · [PDF](https://arxiv.org/pdf/2611.01940)

## 一句话摘要

Delta-rule linear attention underlies language models such as Kimi Linear and Qwen3-Next.

## 为什么值得关注

待编辑增强。

## 摘要原文

Delta-rule linear attention underlies language models such as Kimi Linear and Qwen3-Next. Chunkwise implementations expose matrix parallelism, but their backward passes compute unnecessary auxiliary adjoints. We present ReWY, an algebraic reformulation that reduces this work before optimizing accelerator execution. Differentiating the chunk correction as one triangular residual system eliminates the inverse adjoint and reduces seven local WY matrix products to three. Two complementary transformations expose further reuse: centered matrix contractions replace pairwise vector-gate processing, and scalar-gate reductions reuse key-gradient products instead of forming a key Gram matrix. These identities simplify backward computation for DeltaNet, GDN, KDA, and GDN2 while preserving the recurrence and gradients in exact arithmetic, without changing the architecture or training objective. We implement the reduced graph on GPUs and Ascend NPUs. Under matched recomputation and full-saving policies, precision-qualified six-shape comparisons with frozen FLA references yield 1.15-1.81$\times$ geometric-mean complete low-level backward speedups on NVIDIA GPUs. All four operators achieve 1.18-1.70$\times$ on H100 and H200 while retaining original FP32 working matrices. A separate public-autograd evaluation on Ascend 950DT, including gradient conversions, yields 1.09-2.89$\times$ under available matched policies. Paired ablations establish further ReWY gains after optimizing the complementary contractions. Complete-gradient checks validate the recorded operator cases; supplementary full-model backward measurements assess integration into community FLA models and a GDN2 layer port. Code and reproduction materials: https://github.com/flashserve/ReWY.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yi Zhang, Zhixin Zhao, Weiwei Sun, Yitao Hu, Sheng Chen, Keqiu Li
- 发布：2026-11-03；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/flashserve/ReWY](https://github.com/flashserve/ReWY)
- 阅读深度：metadata
