---
title: "TokTier: Exact Stateful CPU+GPU Tokenization for Agentic LLM Serving"
description: "LLM serving stacks cache prompt KV state, yet the front end still re-tokenizes the full request text on every call."
---

**评分：41/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2607.29678) · [PDF](https://arxiv.org/pdf/2607.29678)

## 一句话摘要

LLM serving stacks cache prompt KV state, yet the front end still re-tokenizes the full request text on every call.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM serving stacks cache prompt KV state, yet the front end still re-tokenizes the full request text on every call. Coding agents pay the most: each call resubmits a long transcript after a small append, and reuse is hard because a short append can move token boundaries near the end of the prior sequence. Across 153,951 agent calls, the median append is 1.4K characters; only 1.0-3.6% of calls start or rebuild a session, but those carry multi-million-character contexts. At the fleet's 94.1% prompt-cache hit rate approaching 0.99, tokenization grows from 10% to 64% of time to first token. TokTier is a stateful CPU+GPU tokenization service for this two-mode workload with one contract: emitted token IDs are always identical to full reference tokenization of the request text. For session continuations it re-tokenizes a small window around the append and splices only when a per-request check finds a stable pre-tokenization boundary, else it widens or falls back. For calls without a reusable prefix it decomposes GPT-family regex pre-tokenization into run-local rules and runs exact pre-tokenization and BPE on a GPU. A sampled shadow verifier re-checks live traffic. Differential campaigns over 17 production tokenizer families ($1.5\times10^{10}$ split checks, a 12.4TB real-text corpus, 93,000+ replayed agent steps) show zero divergence. Incremental repair takes 0.5-1.1ms from 100K to 3M characters, up to $437\times$ faster than HF tokenization and $2.1\times$ faster at 1M characters than the strongest cache-based baseline (Gigatoken) fully prewarmed. GPU full tokenization encodes 1M characters in 0.87ms, $491\times$ below HF and $23.4\times$ below the fastest published CPU method. With vLLM, median time to first token drops 16-34% and P99 23%; under a 50ms P99 objective, four repair cores plus one GPU sustain 1,821 requests/s where a 16-core stateless front end saturates at 40.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhenyu Zhang, Zhichao Cao
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
