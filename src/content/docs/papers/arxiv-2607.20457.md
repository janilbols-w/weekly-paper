---
title: "Dropping the Anchor: Statistical Context Summarization for Distributed Systems via Pulsar Attention"
description: "Inference with large language models (LLMs) on long sequences is computationally expensive due to the quadratic complexity of self-attention."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2607.20457) · [PDF](https://arxiv.org/pdf/2607.20457)

## 一句话摘要

Inference with large language models (LLMs) on long sequences is computationally expensive due to the quadratic complexity of self-attention.

## 为什么值得关注

待编辑增强。

## 摘要原文

Inference with large language models (LLMs) on long sequences is computationally expensive due to the quadratic complexity of self-attention. Distributed blockwise methods such as Star Attention reduce this cost by sharding context across hosts, but rely on prepending a static, content-blind copy of the first block to every host. We propose Pulsar Attention, which replaces the static anchor with two lightweight, content-aware components: a small attention-sink prefix that stabilizes softmax, and compact cross-block summaries built via a Max-IDF heuristic that selects chunks containing globally rare tokens. This reduces the Phase 1 per-GPU FLOPs by up to 3.3x over Star Attention while retaining an identical KV cache footprint. On RULER with Llama-3.1-8B-Instruct, Pulsar Attention outperforms Star Attention at sequence lengths up to 128K tokens and remains competitive with dense attention across most tasks, with task-dependent absolute gains of up to 4.7% over the dense baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Aryan Sood, Shantanu Acharya, Gaurav Kumar Nayak
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
