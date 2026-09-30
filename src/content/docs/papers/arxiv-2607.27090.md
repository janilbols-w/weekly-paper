---
title: "InferScale: GPU-Native KV Injection for Personalized LLM Serving"
description: "Large language models are increasingly deployed with persistent personalized context, such as accumulated memory profiles or long conversation histories, that is shared across a user's many requests."
---

**评分：47/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2607.27090) · [PDF](https://arxiv.org/pdf/2607.27090)

## 一句话摘要

Large language models are increasingly deployed with persistent personalized context, such as accumulated memory profiles or long conversation histories, that is shared across a user's many requests.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models are increasingly deployed with persistent personalized context, such as accumulated memory profiles or long conversation histories, that is shared across a user's many requests. Production memory systems (e.g., Mem0, MemGPT, and Zep) retrieve a relevant subset of this memory and inject it into the prompt, forcing the serving engine to repeatedly prefill the same content. As the retrieval budget grows, time-to-first-token (TTFT) increases even though the underlying memory is reused across requests. We present InferScale, a GPU-native LLM memory system that replaces repeated prompt prefilling with reusable KV state. InferScale precomputes each memory fact's KV representation, stores it alongside a semantic embedding on the GPU, retrieves relevant facts at serving time, and injects their KV directly into vLLM's paged cache. To support dynamically assembled memories under rotary position embeddings, we introduce Chunked RoPE, which stores keys before rotation and applies their serving-time positions during injection. However, encoding memory facts independently omits the cross-fact context available during joint prefilling. We mitigate this with Context-Window Encoding, which encodes each memory fact together with a small window of preceding conversation context while caching only the target fact's KV. InferScale is implemented through vLLM's KV-connector interface, requiring neither engine modifications nor model fine-tuning. Across three open-weight models on LoCoMo, InferScale keeps TTFT nearly constant as the retrieval budget increases: at k=50 it reduces TTFT by 72-79% (3.6-4.8x), achieves 60.3% accuracy versus 63.3% for Mem0 without serving-time recomputation, and delivers 3.7-4.5x the throughput under concurrent load. Reusable KV state thus decouples memory-conditioned serving latency from retrieved-context size while preserving application quality.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Peter Li, Prashant Pandey
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
