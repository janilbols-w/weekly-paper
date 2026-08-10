---
title: "TokTier: Exact Stateful CPU+GPU Tokenization for Agentic LLM Serving"
description: "LLM serving caches prompt KV state, yet most front ends still re-tokenize the full request on every call."
---

**评分：44/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2607.29678) · [PDF](https://arxiv.org/pdf/2607.29678)

## 一句话摘要

LLM serving caches prompt KV state, yet most front ends still re-tokenize the full request on every call.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM serving caches prompt KV state, yet most front ends still re-tokenize the full request on every call. Coding agents pay most: sessions repeatedly submit a long transcript after a small append, which can shift token boundaries near the end of the prior sequence. Across 153,951 calls the median append is ~1.4K characters; only 1.0-3.6% of calls start or rebuild a session, yet those carrymulti-million-character contexts. Fleet prompt-cache hit rate is 94.1%, and as it approaches 0.99, tokenization grows from 10% to 64% of time to first token (TTFT) in component measurements. TokTier is a stateful CPU+GPU tokenization service for this two-mode workload, under one contract: emitted token IDs are always identical to full reference tokenization. For session continuations it re-tokenizes a small window around the append and splices only when a per-request check finds a stable pre-tokenization boundary; failed checks widen the window or fall back to full reference tokenization. For calls without a reusable prefix it runs exact GPT-family regex pre-tokenization and BPE on a GPU. A sampled shadow verifier re-checks live traffic. Across 17 production tokenizer families, differential campaigns cover 1.5x10^10 split checks, a 12.4 TB real-text corpus, and 93,000+ replayed agent steps, with zero divergence. Incremental repair takes 0.5-1.1 ms from 100K to 3M characters, up to 437x faster than HF tokenization and 2.1x faster at 1M characters than the strongest cache-based baseline (Gigatoken) fully prewarmed. GPU tokenization encodes a 1M-character request in 0.87 ms, up to 491x below HF and 23.4x below the fastest published CPU method on the same protocol. With vLLM, median TTFT drops 16-34% and P99 TTFT 23% under recorded bursts. Under a 50 ms P99 objective, a four-core repair pool plus one GPU sustains 1,821 requests/s, where a 16-core stateless front end saturates at 40 requests/s.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zhenyu Zhang, Zhichao Cao
- 发布：2026-08-04；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
