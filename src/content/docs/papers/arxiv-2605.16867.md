---
title: "GoodServe: Globally-coordinated Routing of Agentic LLM Inferences for High Goodput"
description: "Agentic applications consume LLM inferences as complete outputs: a code patch or database query is useful only after its last token arrives."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2605.16867) · [PDF](https://arxiv.org/pdf/2605.16867)

## 一句话摘要

Agentic applications consume LLM inferences as complete outputs: a code patch or database query is useful only after its last token arrives.

## 为什么值得关注

待编辑增强。

## 摘要原文

Agentic applications consume LLM inferences as complete outputs: a code patch or database query is useful only after its last token arrives. Their performance is thus measured by end-to-end deadline satisfaction and goodput, the number of inferences completed within their deadlines. In heterogeneous GPU pools, existing greedy routers favor the fastest or least-loaded instance, often wasting powerful GPUs on requests that could meet their deadlines on weaker ones. Maximizing goodput instead requires globally coordinated routing, informed by uncertain output lengths and dynamic instance performance. We present GoodServe, a goodput-oriented routing system that addresses these challenges through a predict-and-rectify design. A task-gated mixture-of-experts predictor estimates request output lengths, while an EMA-smoothed black-box estimator tracks queuing delays and per-token speeds, accounting for prefix-cache reuse. A just-enough policy routes each request to the weakest instance capable of meeting its deadline and rejects requests that cannot finish on time. Periodic risk checks trigger migration of endangered requests using token IDs, at 7-15 times lower cost than KV-cache transfer. On a four-GPU heterogeneous testbed with three agentic benchmarks, GoodServe achieves the highest goodput across all evaluated SLO levels, improving over the best existing router by up to 31.0%. Its routing overhead remains 5 ms per request at 10,000 requests per second across 512 simulated instances.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Boxiao Du, Boning Huangfu, Yizhou Luo, Chen Chen, Zijun Li, Minchen Yu, Xiaoyi Fan, Minyi Guo
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
