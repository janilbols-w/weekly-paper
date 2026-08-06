---
title: "AnchorKV: Anchor-Residual KV Cache Compression"
description: "The key-value (KV) cache is the primary memory bottleneck in long-context LLM inference."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.02901) · [PDF](https://arxiv.org/pdf/2608.02901)

## 一句话摘要

The key-value (KV) cache is the primary memory bottleneck in long-context LLM inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

The key-value (KV) cache is the primary memory bottleneck in long-context LLM inference. Existing approaches attack it from opposite ends: eviction methods permanently discard tokens, degrading performance whenever a discarded token later proves essential, while quantization methods retain all tokens at low precision but offer limited compression. We propose AnchorKV, a compression scheme that shrinks the cache by $20\times$ without discarding a single token. AnchorKV represents the cache using a small set of anchors stored exactly, expresses every other token through its most similar anchor, and refines only those whose approximation most affects the model's output. AnchorKV consistently preserves accuracy across models and datasets, retaining 99% of the full-cache score at the 70B scale, while keeping the entire context at a fraction of its cost.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Malik Khalaf, Yara Shamshoum, Nitzan Hodos, Yuval Sieradzki, Assaf Schuster
- 发布：2026-08-05；更新：2026-08-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
