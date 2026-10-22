---
title: "Building a Nested LADDER for LLM Unstructured Post-Training Pruning"
description: "Non-uniform allocation can improve post-training pruning of large language models, yet quality can still degrade sharply at high sparsity."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.28773) · [PDF](https://arxiv.org/pdf/2610.28773)

## 一句话摘要

Non-uniform allocation can improve post-training pruning of large language models, yet quality can still degrade sharply at high sparsity.

## 为什么值得关注

待编辑增强。

## 摘要原文

Non-uniform allocation can improve post-training pruning of large language models, yet quality can still degrade sharply at high sparsity. To control degradation as sparsity increases, we introduce LADDER (Layer-Wise Allocation via Damage-Driven Evaluation and Refinement), which allocates sparsity incrementally. At each step, it evaluates pruning an additional fraction of weights from each eligible layer and commits the layer update that causes the least end-to-end degradation per removed parameter. This process produces non-uniform sparsity profiles and exactly nested masks across multiple budgets. We evaluate LADDER on five OPT, Llama, and Qwen models across 10-90% sparsity, using SparseGPT as its candidate-generation backend and comparing against uniform and adaptive allocation baselines. Results reveal a clear operating-regime trade-off: LADDER is comparable or slightly weaker at benign sparsity but becomes substantially more robust from 70% onward. This high-sparsity advantage largely persists after posterior distillation across four of five models and translates into improved retention of aggregate zero-shot accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation, pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Nicol\'as Mauricio Cuadrado \'Avila, Ivo Gollini Navarrete, Martin Tak\'a\v{c}, Samuel Horv\'ath
- 发布：2026-10-22；更新：2026-10-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
