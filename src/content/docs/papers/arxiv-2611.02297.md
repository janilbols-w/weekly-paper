---
title: "FactorSpec: Serving Exact Relational Constraints as Speculative Drafts"
description: "Speculative decoding speeds up LLM serving by drafting tokens that the target model verifies in one pass, and its gain grows with the drafts the target accepts."
---

**评分：39/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.02297) · [PDF](https://arxiv.org/pdf/2611.02297)

## 一句话摘要

Speculative decoding speeds up LLM serving by drafting tokens that the target model verifies in one pass, and its gain grows with the drafts the target accepts.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding speeds up LLM serving by drafting tokens that the target model verifies in one pass, and its gain grows with the drafts the target accepts. Structured outputs should be an ideal case, because much of a record follows from relations among its fields: an itinerary's days follow from its cities' stays and flights. Serving engines, however, draft such text by proposing it from the prompt or a learned head, and their grammar masks enforce only syntax, so the model must satisfy the relations, which it violates: on NATURAL PLAN's trip problems, Qwen3-8B writes a valid itinerary for 10%, and retries that name the violated relation raise this to 14%. We present FactorSpec, which serves exact relational constraints as speculative drafts. FactorSpec compiles a JSON Schema and its relations into a factor graph with an exact feasibility check, drafts every token the constraint determines as certain, verifies each request at a width chosen for it, and computes the masks in worker processes outside the scheduler while the GPU runs. In SGLang, its drafts yield up to 10.5 tokens per verify step, up to 1.9x those of the fastest n-gram drafter, and it decodes up to 1.43x faster than speculators tuned per load, at a grammar mask's cost; it also leads in vLLM. Because every record is also valid, it serves up to 13.9x the valid records per GPU-second of syntax-only baselines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jianchang Su, Dawei Xiang, Wei Zhang
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
