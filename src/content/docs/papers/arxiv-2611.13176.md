---
title: "SHADOWPREFILL: Keeping Your Next Model Warm for Per-Step Model Routing in Agentic LLM Serving"
description: "Per-step model routers send each LLM call of an agent to the cost-optimal model dynamically within each session."
---

**评分：51/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2611.13176) · [PDF](https://arxiv.org/pdf/2611.13176)

## 一句话摘要

Per-step model routers send each LLM call of an agent to the cost-optimal model dynamically within each session.

## 为什么值得关注

待编辑增强。

## 摘要原文

Per-step model routers send each LLM call of an agent to the cost-optimal model dynamically within each session. However, every model switch discards prefix-cache reuse: KV caches are per model, so the new model must prefill the relevant context before it emits a token. Across representative agentic workloads, including a production coding-agent trace with a mean context of 63K tokens, the prefix hit rate falls from 80-89% on same model calls to 44-65% after a switch, and a switch call takes 1.5-3.2x as long. We present SHADOWPREFILL, which prefills the session's context on the model the router has not chosen, in capacity that instances serving normal traffic leave idle, so the next switch finds its prefix cached. SHADOWPREFILL harvests the per-iteration SLO slack of requests in flight, protects routed calls, spills shadow KV to host memory, and falls back to a cold switch whenever the shadow is incomplete. With LLMRouter routing 24 model pairs over five agentic benchmark suites, SHADOWPREFILL cuts switch-call latency by 8.5-21.4%, LLM-call latency by 3.7-17.7%, and routed token cost by 22.5-46.1%, while normal traffic keeps its SLO and energy per request rises by 0.4%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: model routing
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Haoran Qiu, Rohan Mahapatra, Rodrigo Fonseca, Mark Russinovich
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
