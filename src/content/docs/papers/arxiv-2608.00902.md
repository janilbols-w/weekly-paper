---
title: "Practical Online KV Cache Compaction for LLM Agents: An Empirical Study"
description: "LLM agents accumulate long trajectories of reasoning steps, tool calls, and environment feedback, making the KV cache a major inference bottleneck."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.00902) · [PDF](https://arxiv.org/pdf/2608.00902)

## 一句话摘要

LLM agents accumulate long trajectories of reasoning steps, tool calls, and environment feedback, making the KV cache a major inference bottleneck.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM agents accumulate long trajectories of reasoning steps, tool calls, and environment feedback, making the KV cache a major inference bottleneck. KV cache compaction can reduce this cost, but most prior methods assume a static context where future queries are known or can be approximated offline. Agents instead require online compaction: new information must be compressed before future relevance is known, using proxy queries cheap enough for the inference path. We study online compaction across token eviction (TE) and attention matching (AM), adapting both to compact agent turns and comparing cheap proxy sources such as boundary, repeat-prefill, and delayed future-generation queries. Experiments on BrowseComp-Plus and WideSearch show that immediate compaction often hurts performance, whereas delaying compaction to use the agent's future queries recovers much of the gap. Moreover, TE is often more robust than AM under imperfect proxies. Across models at different scales, TE preserves most of the accuracy while reducing KV cache by 80%, and can improve throughput over the no compaction baseline. These results position proxy-query selection as a core design choice for practical online KV compaction.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yujian Liu, Jiabao Ji, Li An, Rohit Jain, Gungor Polatkan, Siyu Zhu, Shiyu Chang
- 发布：2026-08-02；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
