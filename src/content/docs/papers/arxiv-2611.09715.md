---
title: "Intent-Aware Caching for Efficient LLM Serving"
description: "Modern LLM serving systems use prefix caching to accelerate multi-turn conversational workloads."
---

**评分：43/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.09715) · [PDF](https://arxiv.org/pdf/2611.09715)

## 一句话摘要

Modern LLM serving systems use prefix caching to accelerate multi-turn conversational workloads.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern LLM serving systems use prefix caching to accelerate multi-turn conversational workloads. They cache the key-value states of previous conversation prefixes and reuse them when subsequent requests share the same prefix, to avoid redundant prefill computation and reduce serving latency. However, achieving a high cache hit rate remains challenging because cache reuse depends on whether a conversation continues and how soon the next turn arrives. Our analysis of real workloads shows that user intent is a useful signal for this behavior, as different intents exhibit different continuation probabilities and inter-turn delays. Based on this key insight, we propose Intent-Aware Caching (IAC), an online eviction policy that classifies requests by intent, learns lightweight reuse statistics from recent serving logs and leverages these statistics to guide an oracle-inspired eviction strategy. Extensive evaluation on real workloads (WildChat and ShareChat) shows that IAC reaches a 34.6% cache hit rate. This substantially outperforms both the previous learning-based approach (18.8%) and traditional methods such as least recently used (LRU, 12.2%), while reducing average serving latency by up to 46.1%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kazi Hasan Ibn Arif, JinYi Yoon, Dimitrios S. Nikolopoulos, Hans Vandierendonck, Deepu John, Bo Ji
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
