---
title: "Correlation-Aware Structured Pruning for Large Language Models"
description: "Structured pruning is a promising approach for reducing the substantial inference costs of Large Language Models (LLMs) while maintaining hardware efficiency."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.22131) · [PDF](https://arxiv.org/pdf/2609.22131)

## 一句话摘要

Structured pruning is a promising approach for reducing the substantial inference costs of Large Language Models (LLMs) while maintaining hardware efficiency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Structured pruning is a promising approach for reducing the substantial inference costs of Large Language Models (LLMs) while maintaining hardware efficiency. Many existing methods assess the importance of prunable units (e.g., channels or heads) in isolation, implicitly assuming that pruning errors are additive. This independence assumption is often invalidated by the non-orthogonality of model weights and strong correlations between unit activations, potentially leading to performance degradation. To address this, we propose a Correlation-Aware Structured Pruning method. We formulate the pruning objective as a cardinality-constrained binary quadratic program that explicitly models cross-unit dependencies in the reconstruction error. Since this binary quadratic program is NP-hard and difficult to solve exactly, we develop a greedy interaction algorithm based on dependency-aware marginal costs to optimize unit selection. Furthermore, we incorporate a gradient-based strategy to achieve adaptive layer-wise sparsity allocation across the entire model. Extensive experiments on mainstream LLMs demonstrate that incorporating correlation information yields competitive accuracy-efficiency trade-offs compared to representative structured pruning baselines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sicheng Xu, Hao Shi, Wei Zhang, Haoran Pang, Zhenyu Ming, Hao Wu, Zhongyi Huang, Xin Yao, Gong Zhang
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
