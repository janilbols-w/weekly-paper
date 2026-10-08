---
title: "Continuous Semantic Caching for Low-Cost LLM Serving"
description: "As Large Language Models (LLMs) become increasingly popular, caching responses so that they can be reused by users with semantically similar queries has become a vital strategy for reducing inference costs and latency."
---

**评分：44/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2604.20021) · [PDF](https://arxiv.org/pdf/2604.20021)

## 一句话摘要

As Large Language Models (LLMs) become increasingly popular, caching responses so that they can be reused by users with semantically similar queries has become a vital strategy for reducing inference costs and latency.

## 为什么值得关注

待编辑增强。

## 摘要原文

As Large Language Models (LLMs) become increasingly popular, caching responses so that they can be reused by users with semantically similar queries has become a vital strategy for reducing inference costs and latency. Existing caching frameworks have proposed to decide which query responses to cache by assuming a finite, known universe of discrete queries and learning their serving costs and arrival probabilities. As LLMs' pool of users and queries expands, however, such an assumption becomes increasingly untenable: real-world LLM queries reside in an infinite, continuous embedding space. In this paper, we establish the first rigorous theoretical framework for semantic LLM response caching in continuous query space under uncertainty. To bridge the gap between discrete optimization and continuous representation spaces, we introduce dynamic $\epsilon$-net discretization coupled with Kernel Ridge Regression. This design enables the system to formally quantify estimation uncertainty and generalize partial feedback on LLM query costs across continuous semantic query neighborhoods. We develop both offline learning and online adaptive algorithms optimized to reduce switching costs incurred by changing the cached responses. We prove that our online algorithm achieves a sublinear regret bound against an optimal oracle, which reduces to existing bounds for discrete query models. Extensive empirical evaluations demonstrate that our framework approximates the continuous optimal cache well while also reducing computational and switching overhead compared to existing methods.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Baran Atalar, Xutong Liu, Jinhang Zuo, Siwei Wang, Wei Chen, Carlee Joe-Wong
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
