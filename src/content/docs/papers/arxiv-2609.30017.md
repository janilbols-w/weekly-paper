---
title: "Canopy: Exploiting Piecewise Smooth Tree Priors for Multi-Fidelity Bandits"
description: "Many LLM inference problems, including model routing, prefix-cache management, prompt trimming, and test-time search, can be viewed as optimization over a tree."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.30017) · [PDF](https://arxiv.org/pdf/2609.30017)

## 一句话摘要

Many LLM inference problems, including model routing, prefix-cache management, prompt trimming, and test-time search, can be viewed as optimization over a tree.

## 为什么值得关注

待编辑增强。

## 摘要原文

Many LLM inference problems, including model routing, prefix-cache management, prompt trimming, and test-time search, can be viewed as optimization over a tree. This structure arises naturally from autoregressive generation: every prefix defines a node, and its continuations form a subtree below it. Internal nodes of the tree provide cheap but biased estimates of a region's value, while leaf evaluations are expensive but accurate. Hierarchical bandit methods can exploit this structure, but typically require a specific smoothness schedule to be specified in advance, even though real objectives are often only piecewise smooth and their optima may lie near sharp boundaries. We introduce CANOPY, a multi-fidelity tree bandit that learns where the smoothness prior is valid rather than assuming it globally. CANOPY uses cheap random-path probes to construct an online certificate of local aggregation bias, then directs expensive leaf evaluations toward cells where the certificate detects a smoothness violation. We prove fixed-budget and regret guarantees whose additional cost is additive in the number of discontinuities, recovering the smooth-tree rate when no violations are present and approaching structure-blind search as violations become dense. Across routing, top-$k$ identification, test-time search, caching, and prompt trimming, CANOPY consistently improves matched-budget performance, including $2.9\times$ higher top-10 recall on a 1000-model pool, $1.6\times$ more SWE-bench Verified issues resolved than best-of-$N$, and $3.6\times$ lower median time-to-first-token with prefix caching.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: prefix caching
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Michael Jerge, Suman Jana
- 发布：2026-09-24；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
