---
title: "ActTail: Global Activation Sparsity in Large Language Models"
description: "Activation sparsity is a promising approach for accelerating large language model (LLM) inference by reducing computation and memory movement."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2603.12272) · [PDF](https://arxiv.org/pdf/2603.12272)

## 一句话摘要

Activation sparsity is a promising approach for accelerating large language model (LLM) inference by reducing computation and memory movement.

## 为什么值得关注

待编辑增强。

## 摘要原文

Activation sparsity is a promising approach for accelerating large language model (LLM) inference by reducing computation and memory movement. However, existing activation sparsity methods typically apply uniform sparsity across projections, ignoring the heterogeneous statistical properties of Transformer weights and thereby amplifying performance degradation. In this paper, we propose ActTail, a TopK magnitude-based activation sparsity method with global activation sparsity allocation grounded in Heavy-Tailed Self-Regularization (HT-SR) theory. Specifically, we capture this heterogeneity via the heavy-tail exponent computed from each projection's empirical spectral density (ESD), which is used as a quantitative indicator to assign projection-specific sparsity budgets. Importantly, we provide a theoretical analysis that establishes an explicit relationship between the activation sparsity ratio and the heavy-tail exponent under the HT-SR regime, offering principled guidance for sparsity allocation beyond heuristic design. Experiments on LLaMA and Mistral models show that our method improves both perplexity and downstream task performance at high sparsity compared to uniform allocation. At 80% sparsity, perplexity is reduced by 21.8% on LLaMA-2-7B, 40.1% on LLaMA-2-13B, and 9.4% on Mistral-7B.

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

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Wenwen Hou, Xinyuan Song, Wenqian Weng, Shiwei Liu
- 发布：2026-10-27；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
