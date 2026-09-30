---
title: "Cartridges++: KV Cache Compression without Off-Context Derailment"
description: "Serving long documents to a Large Language Model (LLM) repeatedly is expensive: computations grow with context length, and the memory footprint of the key-value (KV) cache balloons."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.35621) · [PDF](https://arxiv.org/pdf/2609.35621)

## 一句话摘要

Serving long documents to a Large Language Model (LLM) repeatedly is expensive: computations grow with context length, and the memory footprint of the key-value (KV) cache balloons.

## 为什么值得关注

待编辑增强。

## 摘要原文

Serving long documents to a Large Language Model (LLM) repeatedly is expensive: computations grow with context length, and the memory footprint of the key-value (KV) cache balloons. Compressed KV (CKV) representations aim to mimic the cache of a document and are typically computed once and for all, ahead of inference time. Methods to obtain CKVs range from drop mechanisms that reduce their number of columns, to learned approaches. Among the latter, Cartridges have emerged as a leading compression method, learning compact KV representations through distillation on relevant Q/A pairs. While existing evaluations focus primarily on whether Cartridges and other CKVs yield approximately similar responses to document-related, on-context queries, we investigate the crucial deployment question of whether they can handle off-context queries, something the native KV representation is particularly good at, thanks to the mechanics of attention. We observe a fundamental trade-off: while Cartridges perform better for on-context queries, heuristic-variants preserve better the original LLM's ability to operate off-context. We measure this through their capability to avoid context contamination in their response, retain general knowledge, and follow instructions. We propose Cartridges++, simple modifications to cartridges that retain off-context abilities at small or negligible cost. The router variant decides at inference time whether the query should use the learned long-context memory, while the data-mixing variant allocates a small fraction of training Q/As to queries outside the reference long document. Our study shows that assessing CKVs on document utility alone can mask substantial degradation in broader model capabilities, yet those issues can be fixed with benign changes to CKV inference or training.

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

- 作者：Sonia Laguna, Joao Monteiro, Marco Cuturi, Pierre Ablin, Eleonora Gualdoni
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
