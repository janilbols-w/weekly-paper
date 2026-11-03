---
title: "Subquadratic Attention with a Hierarchical Tree-Structured Indexer"
description: "The quadratic scaling of attention is a fundamental bottleneck limiting the long-context capabilities of large language models (LLMs)."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.42112) · [PDF](https://arxiv.org/pdf/2610.42112)

## 一句话摘要

The quadratic scaling of attention is a fundamental bottleneck limiting the long-context capabilities of large language models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

The quadratic scaling of attention is a fundamental bottleneck limiting the long-context capabilities of large language models (LLMs). A variety of approaches have attempted to circumvent this, but they either fail to match attention's expressiveness (e.g., sliding-window or linear attention variants with fixed-size state) or only achieve constant-factor speedups (e.g., sparse attention methods whose indexers themselves scale quadratically). In this paper, we derive an asymptotically subquadratic sparse attention method based on a hierarchical, tree-structured indexer, which we call Zyphra Hierarchical Attention (ZHA). ZHA constructs a tree of recursively compressed key summaries over the KV cache, which future queries traverse from the top down to retrieve a sparse subset of keys. Crucially, by iteratively growing the tree's depth, the total cost including routing and final attention grows sublinearly in sequence length, resulting in overall subquadratic (but superlinear) scaling for attention. We demonstrate that ZHA can be cheaply applied to existing pretrained models with only a short KL distillation training stage over a few billion tokens, and maintains performance on long-context retrieval and challenging reasoning, mathematical, and agentic coding evaluation tasks. Moreover, we show that our method is highly robust to tree geometry including very deep trees of up to 6 levels. Finally, we develop a detailed performance model and show that our approach scales subquadratically, dramatically outperforms competing methods beyond 1 million context, and ultimately has the potential to extend effective context windows to the hundreds of millions or billions of tokens.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Leon Lufkin, Cutter Dawes, Alexander Speicher, Kamesh Krishnamurthy, Tom\'as Figliolia, Beren Millidge
- 发布：2026-11-02；更新：2026-11-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
