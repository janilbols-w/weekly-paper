---
title: "SAGE: SLO-Aware Adaptive Retrieval for Production RAG Systems"
description: "Retrieval-Augmented Generation (RAG) systems in production operate under strict service level objectives (SLOs) on tail latency and infrastructure cost."
---

**评分：44/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2608.08237) · [PDF](https://arxiv.org/pdf/2608.08237)

## 一句话摘要

Retrieval-Augmented Generation (RAG) systems in production operate under strict service level objectives (SLOs) on tail latency and infrastructure cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Retrieval-Augmented Generation (RAG) systems in production operate under strict service level objectives (SLOs) on tail latency and infrastructure cost. However, standard retrieval pipelines rely on fixed retrieval budgets that ignore query difficulty, over-retrieving for easy queries and under-serving hard ones, forcing operators to trade answer quality against SLO compliance. This paper proposes SAGE, a learned SLO-aware adaptive retrieval policy that dynamically selects the number of passages k per query. SAGE uses lightweight features derived from initial retrieval (e.g., score distributions, rank gaps, lexical signals) and is trained offline via imitation learning from an oracle that approximates optimal latency-quality trade-offs. At inference, it adds no LLM calls and minimal overhead. On Natural Questions, under a 5s P95 latency SLO, SAGE achieves 95% SLO compliance versus 30% for the best static baseline (k=20), reduces P95 latency by 36% and retrieval cost by 51% with only 2 percentage points Exact Match (EM) loss. A single policy trained on Natural Questions generalizes across HotpotQA, UnSeenTimeQA, and four LLM families (Llama, Qwen, Mistral, Gemma), consistently yielding +45-52 point SLO improvements without quality degradation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: slo, tail latency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Muhammad Faizan Raza (Luna), Shuo (Luna), Yang, Satish Mahadevan Srinivasan
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
