---
title: "RR-Evict: Fine-Grained Prefix Cache Eviction beyond LRU for Agentic LLM Serving"
description: "LLM-based agents execute long-horizon tasks through repeated model calls interleaved with tool execution and user interaction."
---

**评分：43/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.32278) · [PDF](https://arxiv.org/pdf/2609.32278)

## 一句话摘要

LLM-based agents execute long-horizon tasks through repeated model calls interleaved with tool execution and user interaction.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM-based agents execute long-horizon tasks through repeated model calls interleaved with tool execution and user interaction. As each call extends the history accumulated in previous turns, prefix caching avoids repeated prefill of the agent's entire context. However, the aggregate cache footprint grows with context length and concurrency, forcing serving systems to reclaim cached KV tensors. We identify recency synchronization: accesses to an agent's cached history refresh its cache nodes together, causing least recently used (LRU) eviction to concentrate on a few agents' private histories. When a fully evicted agent returns, it must recompute nearly its entire accumulated context, producing a large time-to-first-token (TTFT) outlier even if most other requests retain substantial cache reuse. We present RR-EVICT, a fine-grained prefix-cache eviction strategy that distributes reclamation across idle agent trajectories. RR-EVICT visits agents in round-robin order and evicts a tail chunk from each, preserving reusable prefixes for more agents when capacity remains for idle state. Returning agents can reuse these partial histories and recompute smaller missing suffixes. The policy requires no prediction of future arrivals or tool latency. We implement RR-EVICT in SGLang and evaluate conversational and coding-agent workloads under colocated and prefill-decode-disaggregated serving. Compared with LRU, RR-EVICT reduces P99 TTFT by up to 75.4% and P99 uncached prompt tokens by up to 65.7%.

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

- 作者：Zaifeng Pan, Chris Wu, Zhengding Hu, Xinwei Qiang, Zhongkai Yu, Yufei Ding
- 发布：2026-09-26；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
