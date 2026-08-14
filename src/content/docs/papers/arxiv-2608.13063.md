---
title: "Explanatory Engagement Under Rare Anomalous Failure: Asymptotic Rarity in Model Behavior (or: The Asymptotic AI)"
description: "Prior work on LLM behavior under anomalous conditions asks whether a model notices anomalies."
---

**评分：38/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2608.13063) · [PDF](https://arxiv.org/pdf/2608.13063)

## 一句话摘要

Prior work on LLM behavior under anomalous conditions asks whether a model notices anomalies.

## 为什么值得关注

待编辑增强。

## 摘要原文

Prior work on LLM behavior under anomalous conditions asks whether a model notices anomalies. We ask a narrower question: once a model sits in a workflow with a low, controllable failure rate, does its explanatory engagement - length, specificity, self-reported confidence - change as failure grows asymptotically rarer? We built a local, zero-cost harness on three open-weight models (qwen3:8b, llama3.1:8b, mistral:7b) running a repeated tool-call task where one call fails at probability p, swept across eight rates from 0.2 to 0.0001, under five elicitation conditions from immediate prompting to none. We hypothesized a rise in engagement as failures grew rarer, then a collapse near a detectability threshold. Pooled across conditions this appeared false: length fell in a flat, monotonic pattern. Splitting by condition overturned that. Under immediate_forced, where the model must explain every failure instantly, the predicted rise is confirmed but followed by a plateau, not a collapse: length peaks at 28.4 words at p=0.05, settles to 17.4-19.0 words at the rarest rates, and confidence rises unevenly from about 53% to the 70s-90s. Under grouped_runs, explanation batched to run-end, no collapse appears. Under passive_unprompted, aggregate magnitude is a floor artifact, but a recovered logging gap revealed real, model-specific self-monitoring: llama3.1:8b volunteers structured confidence reports unprompted, sometimes eroding its own confidence as trials accumulate; the other two do so only once, as boilerplate. Elicitation structure is a first-class moderator of collapse observability. A companion guaranteed-failure run (72 cells, backfilling rates where random sampling gave zero real failures) shows models differ in whether they recognize an anomaly, distinct from engagement once recognized. Limitation: discrete rate points cannot capture behavior between them, a direction for future work.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: observability
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sam Mao
- 发布：2026-08-13；更新：2026-08-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
