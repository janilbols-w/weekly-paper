---
title: "AgentKV: Phase-Aware KV Eviction for Agentic LLMs"
description: "Agentic serving can consume orders of magnitude more tokens than chatbot workloads, stressing both KV-cache capacity and decode-time bandwidth."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.14872) · [PDF](https://arxiv.org/pdf/2609.14872)

## 一句话摘要

Agentic serving can consume orders of magnitude more tokens than chatbot workloads, stressing both KV-cache capacity and decode-time bandwidth.

## 为什么值得关注

待编辑增强。

## 摘要原文

Agentic serving can consume orders of magnitude more tokens than chatbot workloads, stressing both KV-cache capacity and decode-time bandwidth. Most KV-eviction methods score cached keys against representative queries drawn from the most recent tokens, assuming future attention resembles recent attention. We show that agentic generation violates this assumption: future queries form a mixture over think, act, tool, and others phases, and principal-angle analysis shows these components occupy measurably different query subspaces, so recency representatives systematically undervalue keys that upcoming phases will need. We propose AGENTKV, which maintains a small query buffer per phase and scores cached keys against their union. We further implement AGENTKV in a persistent multi-turn serving path that carries compressed KV state across turns and compacts retained KV pages online. Across two models, six task domains, and three KV budgets each, AGENTKV improves task score by 5.5 points on average over R-KV and 5.3 over Tri-attention. Relative to upstream full-KV SGLang, AGENTKV improves output-token throughput by up to 1.80x. Code: https://github.com/LiuTaowen-Tony/agentkv.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Taowen Tony Liu, Jeffrey T. H. Wong, Can Xiao, Bowen Yang, Hao Mark Chen, Yiren Zhao
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/LiuTaowen-Tony/agentkv](https://github.com/LiuTaowen-Tony/agentkv)
- 阅读深度：metadata
