---
title: "Multi-Turn Semantic Caching for Low-Cost LLM Serving"
description: "Semantic caching lowers the cost of serving large language models (LLMs) by reusing stored responses for similar requests."
---

**评分：45/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.01077) · [PDF](https://arxiv.org/pdf/2611.01077)

## 一句话摘要

Semantic caching lowers the cost of serving large language models (LLMs) by reusing stored responses for similar requests.

## 为什么值得关注

待编辑增强。

## 摘要原文

Semantic caching lowers the cost of serving large language models (LLMs) by reusing stored responses for similar requests. In multi-turn conversations, whether a cached response is acceptable depends on both conversations' histories, which embedding similarity of requests and histories predicts poorly (AUC 0.62--0.74 on five workloads). We therefore learn the \emph{reuse risk}, the probability that a cached response is unacceptable, from judge feedback, and choose a budgeted set of conversation states to cache by weighing the generation cost a reuse avoids against a price for unacceptable reuse. We propose CUCB-SC-MT, which learns a cache from logged conversations with a suboptimality guarantee, and CLCB-LS-MT, which learns online and has $\tilde O(\sqrt N)$ regret over $N$ requests when conversation states recur. On math-tutoring (SocraTeach) and movie-ticketing (Taskmaster-3) conversations, both achieve lower loss than prior semantic caching approaches: ContextCache, multi-turn variants of ElastiCache and vCache, and single-turn semantic caching at every cache budget. With 1,000 cache entries, CLCB-LS-MT avoids 35--41\% of the generation cost through acceptable reuses, against at most 22--25\% for the baselines, and lowers estimated serving latency by 19--35\%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Baran Atalar, Selly Beyene, Xutong Liu, Carlee Joe-Wong
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
