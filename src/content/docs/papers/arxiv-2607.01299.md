---
title: "HYPIC: Position-Independent Caching for Hybrid-Attention LLM Serving"
description: "In retrieval-augmented generation (RAG) and agentic LLM serving, prompts are assembled from multiple independent segments into long contexts, making prefill dominate the computation cost."
---

**评分：43/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2607.01299) · [PDF](https://arxiv.org/pdf/2607.01299)

## 一句话摘要

In retrieval-augmented generation (RAG) and agentic LLM serving, prompts are assembled from multiple independent segments into long contexts, making prefill dominate the computation cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

In retrieval-augmented generation (RAG) and agentic LLM serving, prompts are assembled from multiple independent segments into long contexts, making prefill dominate the computation cost. To reduce this cost, position-independent caching (PIC) admits KV reuse for non-contiguous segments across requests, while hybrid-attention models reduce computational complexity using linear attention. However, existing PIC methods break down on hybrid-attention models because their per-token KV-cache reuse primitives do not transfer to per-request recurrent states. In this work, we present HYPIC, the first system to accelerate hybrid-attention LLM serving with position-independent caching. For linear-attention layers, we identify the segment-cumulative transition operator as the missing algebraic primitive and cache it for each segment, enabling near-exact and constant-time state composition. For the remaining full-attention layers, we construct a small seam window to propagate hidden states through the linear-attention layers, so that cross-segment attention can be repaired by recomputation. Finally, HYPIC introduces segment parallelism, which parallelizes cache-miss prefill across instances, turning long cold requests into an accelerable workload. Evaluated across four hybrid-attention models and five workloads, HYPIC reduces time-to-first-token (TTFT) by $3.25\times$ on average and improves QPS by $1.66\times$ over Prefix Cache, while preserving task quality with a $1.71$-point gap from Full Recompute.

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

- 作者：Yifei Liu, Juntong Wu, Yang Liu, Junhao Hu, Minghao Li, Xiaoxu Chen, Weihang Chen
- 发布：2026-11-05；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
