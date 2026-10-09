---
title: "RouterInterp: Understanding Superposed Specialisation in Mixture of Experts Routing"
description: "Sparse Mixture of Experts (MoE) models scale more efficiently than dense models by routing tokens to modular expert networks that are only active for processing a fraction of tokens."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2610.11775) · [PDF](https://arxiv.org/pdf/2610.11775)

## 一句话摘要

Sparse Mixture of Experts (MoE) models scale more efficiently than dense models by routing tokens to modular expert networks that are only active for processing a fraction of tokens.

## 为什么值得关注

待编辑增强。

## 摘要原文

Sparse Mixture of Experts (MoE) models scale more efficiently than dense models by routing tokens to modular expert networks that are only active for processing a fraction of tokens. A leading hypothesis for the performance of MoE models is that each expert specialises in a single, coherent domain. However, interpretability efforts that assume this hypothesis have generally been unsuccessful. We propose and present evidence for an alternative account that we call the Superposed Specialisation Hypothesis (SSH): experts specialise in a disjoint union of fine-grained features rather than one broad domain. Leveraging the SSH, we introduce RouterInterp, a method for interpreting expert routing that identifies Sparse Autoencoder features most predictive of routing decisions and produces unified natural language explanations. On gpt-oss-20b, RouterInterp explains expert routing with ${\sim}65\%$ higher detection accuracy than prior token statistics based methods. This work provides a scalable method for generating more accurate explanations of expert routing and increases our understanding of a previously uninterpretable component of foundation models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: expert routing, mixture of experts
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ilya Lasy, Nora Yinuo Cai, Kola Ayonrinde
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
