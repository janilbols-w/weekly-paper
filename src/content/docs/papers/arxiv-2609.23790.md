---
title: "Total Cost of Agency: Exact Attribution of Memory Injection Cost in Multi-Agent LLM Workflows"
description: "Every node in a multi-agent large language model (LLM) workflow retrieves context from memory and injects it into its prompt, where those injected tokens are billed as input tokens at the same per-token price as the system prompt and the user query."
---

**评分：51/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2609.23790) · [PDF](https://arxiv.org/pdf/2609.23790)

## 一句话摘要

Every node in a multi-agent large language model (LLM) workflow retrieves context from memory and injects it into its prompt, where those injected tokens are billed as input tokens at the same per-token price as the system prompt and the user query.

## 为什么值得关注

待编辑增强。

## 摘要原文

Every node in a multi-agent large language model (LLM) workflow retrieves context from memory and injects it into its prompt, where those injected tokens are billed as input tokens at the same per-token price as the system prompt and the user query. Production observability tools report total token cost but do not separate the tokens a node generates from the tokens it is handed, so this component of the bill is invisible to the teams paying it. We introduce the Total Cost of Agency (TCA), a decomposition of multi-agent workflow cost into base prompt, inference, memory injection, miss penalty and context-accumulation components, and an exact attribution method: a two-pass, non-billable token count that measures injected tokens directly rather than estimating them from word-count proxies. On a 200-task enterprise benchmark executed against real model APIs, memory injection accounts for 13.6 percent of the variable cost a compile-time optimizer can act on, about 12 percent of the full billed cost, and its share rises from a structural zero at workflow depth one to 27.6 percent at depth six. Injected tokens grow linearly with depth over the measured range (R^2 = 0.9974, depths two through six); a quadratic fit yields a negative leading coefficient, so the data do not exhibit convex growth at these depths. We show the component is controllable at fixed model tier: reducing the retrieval window capacity from 32 to 2 entries lowers injected tokens by 28.7 percent with an accuracy change within seed-level variation. We report in full that our graph-rewriting transforms are approximately cost-neutral in isolation, that two of the five decomposition terms are zero by construction in this harness, and that total workflow cost is dominated by model tier assignment, which we hold fixed and treat as prior work. Prompt caching is not evaluated; all figures are for the uncached case.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 12 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: observability
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Vivek Kumar Singh, Preeti Priyam, Gautam Bhowmick
- 发布：2026-09-20；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/vsingh45/tca-compiler](https://github.com/vsingh45/tca-compiler)
- 阅读深度：metadata
