---
title: "KVBoost: Chunk-Level Key-Value Cache Reuse with Deviation-Guided Recomputation for Efficient Large Language Model Inference"
description: "Transformer-based large language models (LLMs) incur high prefill latency because key-value (KV) tensors must be recomputed for each request."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.21362) · [PDF](https://arxiv.org/pdf/2608.21362)

## 一句话摘要

Transformer-based large language models (LLMs) incur high prefill latency because key-value (KV) tensors must be recomputed for each request.

## 为什么值得关注

待编辑增强。

## 摘要原文

Transformer-based large language models (LLMs) incur high prefill latency because key-value (KV) tensors must be recomputed for each request. Existing prefix-caching systems reduce this cost but require prompts to share a leading contiguous prefix, limiting effectiveness when shared content appears at arbitrary positions. We present KVBoost, a chunk-level KV cache reuse system for HuggingFace-compatible decoder models that enables reuse regardless of content position. KVBoost introduces a dual-hash keying scheme that separates positional identity (prefix hash) from content identity (content hash), supporting both exact and approximate cache matches. To address attention boundary errors from independently cached chunks, KVBoost employs two repair strategies: SelectiveRecompute, which re-encodes boundary regions, and CacheBlendRecompute, which identifies and recomputes high-deviation tokens after a probe pass. The system further incorporates asymmetric KV quantization (int8/int4), adaptive chunk boundary splitting, and importance-weighted eviction under a fixed memory budget. Evaluated on Qwen/Qwen2.5-3B over 1,000 bug-localization samples, KVBoost achieves a 4.49x reduction in time-to-first-token (142.4 ms vs.\ 639.1 ms) and outperforms prefix caching by 16%, with no loss in accuracy (99.2% vs.\ 99.1%). KVBoost provides a practical, memory-bounded inference acceleration layer compatible with RoPE-based models without architectural modification.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, int8, quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Srihari Unnikrishnan
- 发布：2026-08-25；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
