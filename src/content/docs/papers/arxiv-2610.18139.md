---
title: "Revisiting Error Feedback for Model Quantization"
description: "We study causal error-feedback coefficients as design variables for model quantization."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2610.18139v1) · [PDF](https://arxiv.org/pdf/2610.18139v1)

## 一句话摘要

We study causal error-feedback coefficients as design variables for model quantization.

## 为什么值得关注

待编辑增强。

## 摘要原文

We study causal error-feedback coefficients as design variables for model quantization. Modeling instantaneous quantization errors as independent, zero-mean variables with a common fixed variance, we formulated a metric-dependent trace problem for designing feedback coefficients. The formulation resembles fixed-order GPTQ/LDLQ feedback and supports Jacobian-aware designs that account for downstream error propagation. For a positive-definite metric $\boldsymbol{H}$, we prove that the joint rotation-feedback trace minimum is $n\det(\boldsymbol{H})^{1/n}$ and present an attaining pair using the geometric mean decomposition. Experiments on synthetic networks, trained MLPs, and language models show benefits from downstream-sensitive feedback, but also reveal that trace optimality need not improve finite-level performance. Small QAT experiments further illustrate direct loss-driven feedback tuning with fixed or trainable network weights.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Wai-Yiu Keung, Chi Cui, Wing-Kin Ma, Jesús Cid-Sueiro, Hei Victor Cheng
- 发布：2026-10-13；更新：2026-10-13
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
