---
title: "Fairway: Load-Aware KV Cache Reuse for LLM Prefill Scheduling"
description: "LLM-based applications often employ agentic workflows and retrieval-augmented generation (RAG), which build long prompts from shared context."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.02082) · [PDF](https://arxiv.org/pdf/2611.02082)

## 一句话摘要

LLM-based applications often employ agentic workflows and retrieval-augmented generation (RAG), which build long prompts from shared context.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM-based applications often employ agentic workflows and retrieval-augmented generation (RAG), which build long prompts from shared context. When prefixes are shared across requests, serving engines reuse the key-value (KV) cache to skip parts of the prefill computation. Reuse is typically graded: the uncached work of requests in a queue can differ by up to 100x. In this setting, the order of scheduling determines the time-to-first-token (TTFT) for the queued requests. KV reuse-first scheduling, which prioritizes the requests with the longest KV cache hit, gives the lowest median TTFT but starves expensive requests under load spikes; first-come-first-served (FCFS) scheduling bounds the tail but raises the median TTFT. We present Fairway, a prefill scheduler built on adaptive reuse prioritization: it favors KV cache reuse while queues are short, and shifts toward fair allocation as requests wait longer relative to their own prefill time. Fairway employs a virtual dual lane model: a KV reuse-first Fast lane and a Fair lane atop the serving engine's waiting queue that enables speeding up of cheap reuse requests without starving expensive ones. This model automatically adapts to the workload without any per-workload tuning. Fairway lowers the tail TTFT at no cost to the median in transient overload. Across workloads and load levels, Fairway matches or beats the best baseline, with a p99 TTFT up to 8.6x lower than prior prefix-aware schedulers. During load spikes, it keeps the tail of FCFS at a 6x lower median TTFT.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Hamidreza Alikhani, Nazmul Takbir, Matin Khajavi, Rajat Bhattacharjya, Sangeetha Abdu Jyothi, Nikil Dutt
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
