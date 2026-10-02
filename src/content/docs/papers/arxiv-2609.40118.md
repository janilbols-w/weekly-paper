---
title: "Persistent Context Graphs for Efficient Memory Compaction in LLM Agents"
description: "As LLM capabilities advance, agents are tackling increasingly complex tasks over longer horizons."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2609.40118v1) · [PDF](https://arxiv.org/pdf/2609.40118v1)

## 一句话摘要

As LLM capabilities advance, agents are tackling increasingly complex tasks over longer horizons.

## 为什么值得关注

待编辑增强。

## 摘要原文

As LLM capabilities advance, agents are tackling increasingly complex tasks over longer horizons. Their growing interaction histories make memory compaction essential for staying within context windows and reducing prefill cost. Existing methods summarize the history or compress its KV cache, often adding model computation to preserve information for future requests. A new user request can change which history matters, but reassessing that history with the model requires re-encoding it if the KV cache has expired. Past attention provides signals of historical importance and dependencies between messages, while relevance to the current task must be assessed using the new user request. We introduce ReCAP, a memory compaction method that stores attention-derived importance scores and dependency links in a lightweight, persistent context graph. For each new request, ReCAP combines stored importance with relevance cues from the request and follows dependency links to select messages and their supporting context, without additional model calls for selection. Compared with Codex's default summarization-based compaction, ReCAP reduces estimated latency for compaction and cold restoration by approximately 95% on both Qwen3-Coder and gpt-oss. It also roughly halves the historical context per call on SWE-Together at comparable task quality and improves accuracy on the code tasks of Lost-in-Conversation over full history by 19.8 and 41.2 points.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jingbo Yang, Kwei-Herng Lai, Xiaowen Wang, Zhaoxuan Tan, Pei Zhou, Mengting Wan, Yaar Harari, Evgeniy Gabrilovich, Shiyu Chang
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
