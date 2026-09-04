---
title: "Compression-Aware Abstention: Teaching LLMs to Refuse When KV-Compression Masks Remove Answer Evidence"
description: "KV-cache compression reduces LLM inference memory by evicting context tokens, but when the evicted tokens contain answer-bearing evidence, the model may hallucinate instead of recognizing that the compressed context is insufficient."
---

**评分：51/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.29934) · [PDF](https://arxiv.org/pdf/2608.29934)

## 一句话摘要

KV-cache compression reduces LLM inference memory by evicting context tokens, but when the evicted tokens contain answer-bearing evidence, the model may hallucinate instead of recognizing that the compressed context is insufficient.

## 为什么值得关注

待编辑增强。

## 摘要原文

KV-cache compression reduces LLM inference memory by evicting context tokens, but when the evicted tokens contain answer-bearing evidence, the model may hallucinate instead of recognizing that the compressed context is insufficient. We address this failure from a behavioral perspective: to our knowledge, this is the first work to formulate compression-aware abstention as a learning problem, in which a model learns to answer when supporting evidence survives compression and abstain when it does not. We construct supervision from compressor survival masks and tight answer-bearing spans, labeling examples as Confident when evidence survives and Abstain when it is removed. A 10.1M-parameter LoRA adapter trained on ~2.6K MuSiQue 2-hop QA examples reduces base-model hallucinations by 97% under prompt-style truncation while preserving correct answering on evidence-retaining examples. Unlike prompt-only abstention baselines, which over-abstain on many answerable high-retention examples, the trained adapter learns a conditional policy. We also evaluate the method under actual compressed-cache decoding, where multi-compressor training yields a 6-22x relative lift over the unaided base on evidence-retaining examples. Controlled-deletion experiments show that the learned behavior is driven by evidence content rather than input length alone.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 10 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Mohammadali Khodabandehlou, Bhaskar Krishnamachari
- 发布：2026-08-30；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/mali-kh/compression-aware-abstention](https://github.com/mali-kh/compression-aware-abstention)
- 阅读深度：metadata
