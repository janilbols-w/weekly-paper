---
title: "A Biophysically-Inspired Feedback Controller for Multi-Class Cache Fairness"
description: "Cache replacement under multi-tenant LLM-serving conditions is a multi-class problem: short, high-reuse system prompts; long, moderate-reuse user documents; medium-length code context; and bursty conversation history share a single eviction pool."
---

**评分：43/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2608.14561) · [PDF](https://arxiv.org/pdf/2608.14561)

## 一句话摘要

Cache replacement under multi-tenant LLM-serving conditions is a multi-class problem: short, high-reuse system prompts; long, moderate-reuse user documents; medium-length code context; and bursty conversation history share a single eviction pool.

## 为什么值得关注

待编辑增强。

## 摘要原文

Cache replacement under multi-tenant LLM-serving conditions is a multi-class problem: short, high-reuse system prompts; long, moderate-reuse user documents; medium-length code context; and bursty conversation history share a single eviction pool. Under skewed multi-class arrivals, conventional flat-LRU policies expose the worst-served-class miss ratio ($m_{\max}$) only as a fixed point. We introduce a class of cache-replacement policies parameterised by a per-class flux formula, where three structural commitments -- a single global token-mass imbalance signal, $K$ parallel rectified per-class promotion accumulators, and an age-ordered eviction backstop -- produce emergent multi-class fairness. We instantiate this class with a linear V-coupled rectified flux and a Goldman-Hodgkin-Katz extension whose $V \to 0$ limit is exactly the linear form. Across four skew levels on synthetic multi-class workloads, the policy class closes 27--72\,\% of the LRU$\to$Belady gap on $m_{\max}$, with linear and GHK interchangeable on the headline objective within search variance. The fairness/throughput tradeoff is exposed as a tunable knob on a single hyperparameter axis. We position this against the LeCaR feedback-controller lineage and the formal-control-theory cache-decay lineage as a novel combination of known ingredients. Code and reproduction scripts: https://github.com/flatmax/membrane.cache

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: multi-tenant
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Matt R. Flax
- 发布：2026-08-18；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/flatmax/membrane.cache](https://github.com/flatmax/membrane.cache)
- 阅读深度：metadata
