---
title: "Unifying Depth and Width Pruning for LLMs via Binary Knapsack Optimization"
description: "Structured pruning is a promising approach for compressing large language models (LLMs), yet existing methods rely heavily on greedy heuristics that produce myopic decisions, and often fail to precisely meet target compression budgets."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.12953) · [PDF](https://arxiv.org/pdf/2608.12953)

## 一句话摘要

Structured pruning is a promising approach for compressing large language models (LLMs), yet existing methods rely heavily on greedy heuristics that produce myopic decisions, and often fail to precisely meet target compression budgets.

## 为什么值得关注

待编辑增强。

## 摘要原文

Structured pruning is a promising approach for compressing large language models (LLMs), yet existing methods rely heavily on greedy heuristics that produce myopic decisions, and often fail to precisely meet target compression budgets. We present SNIPER, a two-stage structured pruning framework that solves a knapsack optimization over coarse-granularity components to yield conditionally optimal parameter allocations with respect to fixed importance estimates, followed by a fine-grained pruning stage to meet strict budget constraints. We introduce the Compression Ratio Adherence Factor (CRAFT) to quantify budget fidelity, showing that while existing pruners deviate from target compression ratios by up to 33%, SNIPER achieves near-exact adherence with a CRAFT score of 0.98. Evaluations across four diverse architectures over a set of 18 tasks spanning five domains demonstrate SNIPER's consistent improvements in average performance retention and task-level stability over six state-of-the-art pruners. Across all pruning configurations, SNIPER achieves an excellent mean rank of 1.25, indicating its robust cross-architectural generalizability and excellent reliability.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Palaash Goel, Ayan Sengupta, Akshay Nambi, Tanmoy Chakraborty
- 发布：2026-08-13；更新：2026-08-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
