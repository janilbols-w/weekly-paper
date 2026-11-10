---
title: "Learnable Hodge-Laplacian Driven Mixture of Experts for Steady-PDE Surrogates on Coarse Unstructured Meshes"
description: "Surrogate models approximate the solutions of partial differential equations given a certain geometry and boundary conditions."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2610.20585) · [PDF](https://arxiv.org/pdf/2610.20585)

## 一句话摘要

Surrogate models approximate the solutions of partial differential equations given a certain geometry and boundary conditions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Surrogate models approximate the solutions of partial differential equations given a certain geometry and boundary conditions. Traditional transformer-based approaches employ a single mixing mechanism to the whole solution. although the solution fields exhibit variations across multiple spatial scales. We propose a mixture of transformer experts that combines a routing mechanism with multiscale supervision. Specifically, the individual experts are routed through a controller that utilizes learnable Laplacian matrices to compute weights that are subsequently used to define a weighted sum of the experts for the output feature vectors at each point of the domain. Subsequently, a decoder receives the weighted sum of the experts output and predicts the solution fields. During training, the reference fields are decomposed into components at different spatial scales by repeated smoothing with a mesh Laplacian. We evaluate our approach on the official AirFRANS dataset using remeshed solution domains leading to unstructured triangular meshes of $4.9$k vertices. The experimental outcomes reveal lower mean relative $L_2$ error and interior mean squared errors among the compared models of this study.

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

- taxonomy keywords: mixture of experts
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Stavros Nousias, Akis Nousias, Konstantinos Gkrispanis
- 发布：2026-10-14；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
