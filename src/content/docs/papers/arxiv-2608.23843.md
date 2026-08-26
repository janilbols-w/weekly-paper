---
title: "PuzzleKV: Page-Wise Low-Rank Decomposition for KV Cache Compression"
description: "Long-context inference in large language models (LLMs) is increasingly limited by the memory required for the key-value (KV) cache."
---

**评分：47/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.23843) · [PDF](https://arxiv.org/pdf/2608.23843)

## 一句话摘要

Long-context inference in large language models (LLMs) is increasingly limited by the memory required for the key-value (KV) cache.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context inference in large language models (LLMs) is increasingly limited by the memory required for the key-value (KV) cache. KV cache compression addresses this problem by reducing the storage cost of previous tokens. Among existing approaches, low-rank compression is particularly attractive because it represents every token in reduced dimensions. Previous low-rank methods typically derive fixed projection spaces from model weights, construct fixed spaces from calibration activations, or construct a shared basis over a broad cache region. Such representations may not capture detailed but important information. We partition each per-head KV cache into fixed-length logical pages and observe substantial low-rank structure within individual pages. Based on this observation, we propose PuzzleKV, a training- and calibration-free method that treats each completed page as an independent compression unit. PuzzleKV decomposes pages within each layer and KV head, computes attention directly over dense and factorized pages, and incrementally compresses newly eligible pages during autoregressive decoding. Experiments across models, context lengths, and benchmarks demonstrate the effectiveness of PuzzleKV under matched storage budgets. At approximately 60% of the original KV cache storage, PuzzleKV achieves more than 96% of Full KV performance across both evaluated models and all benchmark settings, with substantial gains over Global SVD on RULER and competitive performance on LongBench. To achieve a more aggressive compression ratio, PuzzleKV can be further combined with quantization while retaining more than 93% of Full KV performance using only 18.7% of the original storage.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zizhong Wang, Jieying Wang, Zhao Zhang, Jiajia Li
- 发布：2026-08-26；更新：2026-08-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
