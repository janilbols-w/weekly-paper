---
title: "Enhancing Knowledge Density via Hierarchical Context Pruning for Retrieval-Augmented Repository-Level Code Completion"
description: "Retrieval-Augmented Generation (RAG) has advanced repository-level code completion by retrieving external code snippets, API documentation, or type definitions to expand the model's contextual awareness."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2508.10068) · [PDF](https://arxiv.org/pdf/2508.10068)

## 一句话摘要

Retrieval-Augmented Generation (RAG) has advanced repository-level code completion by retrieving external code snippets, API documentation, or type definitions to expand the model's contextual awareness.

## 为什么值得关注

待编辑增强。

## 摘要原文

Retrieval-Augmented Generation (RAG) has advanced repository-level code completion by retrieving external code snippets, API documentation, or type definitions to expand the model's contextual awareness. However, under the finite token budget of the context window, existing retrieval-augmented methods often saturate the budget with highly similar or even redundant code, which not only wastes tokens but also suppresses critical cross-file dependencies, preventing synergistic interaction between semantically similar reference snippets and cross-file dependency definitions. Therefore, further gains are limited by low knowledge density in the retrieved context rather than by model capacity. We propose SaraCoder, a retrieval-augmented framework that enhances knowledge density via hierarchical context pruning under a fixed context budget. A Hierarchical Feature Optimization module prunes an over-complete candidate pool in four stages. The freed tokens are then allocated to an External-Aware Identifier Disambiguator, which selectively injects only the most necessary cross-file dependency definitions. SaraCoder transforms context construction into a budget-aware optimization problem, balancing reference snippets and cross-file dependencies to build a context that is both knowledge-dense and semantically complete. Experiments on CrossCodeEval and RepoEval-Updated, across multiple backbone code LLMs, show that SaraCoder consistently outperforms strong RAG baselines such as GraphCoder and Repocoder in both code-level and identifier-level metrics, without increasing token usage, and yields synergistic gains when combined with other cross-file methods.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xiaohan Chen, Xiang Chen, Yu Tian, Piji Li, Sheng-Jun Huang, Songcan Chen
- 发布：2026-10-16；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
