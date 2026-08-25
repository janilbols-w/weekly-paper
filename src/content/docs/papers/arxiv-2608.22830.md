---
title: "Beyond the Harness: End-to-End Optimization of Context Artifacts for Enterprise Text-to-SQL"
description: "Deploying LLMs for enterprise Text-to-SQL is bottlenecked less by the model than by what context reaches it: business logic spans thousands of tables, and no model can ingest a full catalog at once."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.22830) · [PDF](https://arxiv.org/pdf/2608.22830)

## 一句话摘要

Deploying LLMs for enterprise Text-to-SQL is bottlenecked less by the model than by what context reaches it: business logic spans thousands of tables, and no model can ingest a full catalog at once.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deploying LLMs for enterprise Text-to-SQL is bottlenecked less by the model than by what context reaches it: business logic spans thousands of tables, and no model can ingest a full catalog at once. We argue that the most effective place to intervene is therefore the \emph{knowledge-base context} the model consumes, and that this context should be \emph{constructed} from historical usage rather than tuned for as a fixed input. Using a query-DAG decomposition--the same family of intermediates that enterprise benchmarks like BEAVER annotate, here recovered from production SQL--we compare the value of oracle query graphs versus retrieved knowledge-base context. In this ablation, retrieved knowledge-base context provides the largest marginal improvement when added to the full oracle graph. Building on this, we optimize a distillation procedure that turns historical query profiles into reusable SQL reference cards. On a benchmark of 5176 production queries from a major online retailer, optimizing these context artifacts yields larger gains (${\sim}12$--$25\%$ AST similarity) than optimizing the retrieval harness (${\sim}3$--$12\%$). On the public BEAVER benchmark, which lacks the production-usage signals available in our internal setting, the picture is more mixed: table cards alone perform about the same as raw historical SQL. The best optimized variant retrieves both cards and raw SQL, scoring $9.00\%$ versus $6.33\%$ (p-value $0.12$) for the comparable baseline on a held-out $N{=}300$ subset, using retrieved context and harness changes but no agentic loop.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kate Gwimm, Carson Eisenach
- 发布：2026-08-25；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
