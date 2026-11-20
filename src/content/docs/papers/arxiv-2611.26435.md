---
title: "Aggron: Aggressive Compression of Agentic KV Caches during Head-of-Line Stalls in the Request Queue"
description: "LLM agents run long, multi-turn programs whose contexts grow at every step, and serving them is limited by KV cache capacity."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2611.26435v1) · [PDF](https://arxiv.org/pdf/2611.26435v1)

## 一句话摘要

LLM agents run long, multi-turn programs whose contexts grow at every step, and serving them is limited by KV cache capacity.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM agents run long, multi-turn programs whose contexts grow at every step, and serving them is limited by KV cache capacity. To alleviate this limitation, systems use context compression techniques, which typically wait until the KV cache crosses a large threshold and then summarize large spans of history at once, either in the background while the agent progresses or on the critical path. These summarizations can be done using the same model running on the same engine, or using the same or a different model running on extra hardware. When running on the same engine, summarization competes with the requests being served for both compute and memory capacity. To maximize the cost-effectiveness of summarization, this paper presents a new serving system called {\em Aggron}. Aggron summarizes agentic requests at every turn and selectively summarizes only certain parts of the KV cache. As a result, Aggron retains accuracy and keeps summarization requests lightweight. Moreover, Aggron launches summarization requests from a separate {\em Summarization Queue} while the corresponding agentic request whose KV cache we want to compress is stalled in the main request queue due to head-of-line stalls. The Summarization queue utilizes compute and memory capacity left over by the head-of-line stalls in the main queue. Further, to maximize efficiency, the server issues summarizations only when it predicts that they can complete before the corresponding agentic request will finally execute. In our evaluation, we compare Aggron to state-of-the-art asynchronous summarization. At high load, Aggron reduces P99 program latency by $27$--$31\%$, and raises throughput by $1.34$--$1.40\times$.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Rishabh Ravi, Tony Hong, Chen Wang, Yue Zhu, Mengmei Ye, Hubertus Franke, Fan Lai, Josep Torrellas
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
