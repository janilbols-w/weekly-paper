---
title: "AttSVD:Prompt-Adaptive Low-Rank KV Cache Compression via Attention-Guided SVD"
description: "The key-value (KV) cache of autoregressive transformers grows linearly with context length and dominates memory at long context."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.06927) · [PDF](https://arxiv.org/pdf/2610.06927)

## 一句话摘要

The key-value (KV) cache of autoregressive transformers grows linearly with context length and dominates memory at long context.

## 为什么值得关注

待编辑增强。

## 摘要原文

The key-value (KV) cache of autoregressive transformers grows linearly with context length and dominates memory at long context. Most training-free remedies evict low-importance tokens, an irreversible choice along the sequence axis. We instead keep every token and store it more cheaply along the "feature" axis. We therefore propose AttSVD, a new "interpretable" low-rank compression whose basis is derived from each prompt's own attention geometry: an online, per-prompt truncated SVD that keeps only the directions attention actually reads, cutting persistent per-head KV memory in proportion to the retained rank. We propose two decode-time caching strategies, accumulating and streaming, for short and long generation regimes. Furthermore, we propose two refinements that make compression adaptive. A per-matrix energy rule sizes the logit space and the attention mass independently. An attention-aware basis truncates only in the spaces attention actually reads, preserving both the attention logits and the attention output. The same factors also provide free, per-head interpretability insights into the effective rank and the geometry attention consumes. Across multiple models, on both an agentic benchmark and the full LongBench suite AttSVD stays on par with the dense cache while using up to 50% of the KV-cache memory.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sara Abdali, Jongwoo Ko, Pashmina Cameron
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
