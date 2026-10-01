---
title: "PatchKV: Weight-Space Compensation of KV Cache"
description: "Long-context inference with Large Language Models (LLMs) is bottlenecked by the linearly growing memory of the key-value (KV) cache."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.39329) · [PDF](https://arxiv.org/pdf/2609.39329)

## 一句话摘要

Long-context inference with Large Language Models (LLMs) is bottlenecked by the linearly growing memory of the key-value (KV) cache.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context inference with Large Language Models (LLMs) is bottlenecked by the linearly growing memory of the key-value (KV) cache. Existing compression methods reduce the cache through token eviction or approximation, but degrade sharply at aggressive compression budgets. We propose PatchKV, a training-free framework that compensates KV cache compression methods by carrying part of the context in the model's weights. PatchKV pairs an off-the-shelf compressed KV cache with a context-specific weight patch, which is computed once at context-loading time and served for downstream queries for the context. The weight patch is derived in closed form via ridge regression, by aligning the block-wise activations of context-derived reference query tokens under the full cache and the compressed cache. Once merged into the model, the patch leaves the forward graph and per-query inference cost unchanged in the single-context, multi-query setting. Across long-context QA (SCBench with up to 170K tokens, SQuAD, NIAH) and math (GSM8K) benchmarks on three model architectures, PatchKV consistently improves cache compression methods, suggesting an alternative direction to compensate them at aggressive budgets.

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

- 作者：Chanryeol Lee, Chanhyuk Lee, Yeonwoo Choi, Donggyun Kim, Seunghoon Hong
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
