---
title: "LuthorSQL: A One-Pass Text-to-SQL Model as System 1 for a Slower LLM Agent"
description: "Frontier LLM agents that query databases with tools are among the most accurate text-to-SQL systems, but per-query calls to a hosted model are slow, costly, and expose sensitive organizational queries to external APIs."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.17780) · [PDF](https://arxiv.org/pdf/2611.17780)

## 一句话摘要

Frontier LLM agents that query databases with tools are among the most accurate text-to-SQL systems, but per-query calls to a hosted model are slow, costly, and expose sensitive organizational queries to external APIs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Frontier LLM agents that query databases with tools are among the most accurate text-to-SQL systems, but per-query calls to a hosted model are slow, costly, and expose sensitive organizational queries to external APIs. For example, a Claude Opus 5.5 agent serving 10,000 queries a day costs over $70,000 a year at list price. To what extent can local hardware already owned by an organization offload this burden without compromising the agent's accuracy? We present LuthorSQL, a non-autoregressive 7B text-to-SQL model that serves as a rapid System 1 gate for a slower LLM agent (System 2), escalating queries only when uncertain. LuthorSQL makes a single forward pass to predict slot scores over a bounded grammar for query plans, compiles and runs up to 32 candidate plans, and chooses an answer using a trained validator. On its own, LuthorSQL reaches 68.03% execution accuracy on BIRD's hidden test set at 0.84 s per question on a single GPU, maintains its accuracy in 9 GB with 8-bit quantized weights, and transfers zero-shot to Snowflake, BigQuery, MySQL, PostgreSQL, and DuckDB within 3.1 points of its native SQLite accuracy. Combined with Claude Opus 5.5 in a pre-registered confidence cascade over 227 questions on databases published after Opus's training cutoff, LuthorSQL answers nearly half of all questions locally and cuts API cost by 33.3% at the same accuracy. Finally, contamination probing shows that Opus reproduces 48-92% of public benchmark gold queries verbatim without seeing the schema; however, its tool-assisted accuracy holds on renamed schemas and reaches 95.6-97.4% on post-cutoff databases. Code and data: https://github.com/IAMIbrahimmemon/luthorsql

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Ibrahim Memon, Armin Karamzade, M. Hanif Jhaveri, Roy Fox
- 发布：2026-11-16；更新：2026-11-16
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/IAMIbrahimmemon/luthorsql](https://github.com/IAMIbrahimmemon/luthorsql)
- 阅读深度：metadata
