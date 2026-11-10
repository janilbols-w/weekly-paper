---
title: "CacheGraft: Enhancing Retrieval-Augmented Generation via Latent-Space Document Enrichment"
description: "Recent work in machine learning has demonstrated that transformer-based language model agents can communicate state not only through text, but also directly in latent space via key-value (KV) caches."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.07393) · [PDF](https://arxiv.org/pdf/2611.07393)

## 一句话摘要

Recent work in machine learning has demonstrated that transformer-based language model agents can communicate state not only through text, but also directly in latent space via key-value (KV) caches.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent work in machine learning has demonstrated that transformer-based language model agents can communicate state not only through text, but also directly in latent space via key-value (KV) caches. In this paper, we argue that such cache-to-cache translation can provide utility beyond the original motivating application of real-time agent communication and can instead be utilized for retrieval-augmented generation (RAG). Building on the Cache-to-Cache (C2C) fusion framework, our proposed system CacheGraft encodes each corpus passage offline into a fused KV cache representation between a larger sharer model (4B parameters in our experiments) and a smaller receiver model (0.6B parameters) such that this cache can be injected into the receiver at query time with no need for the larger model. Across five QA benchmarks and two independent locally-run judges, CacheGraft improves answer quality over the text-only receiver baseline in 29 out of 30 comparisons, of which 17 of the 30 are statistically significant. Notably, these gains are zero-shot with respect to the fuser, which was never trained on retrieval data. These initial results suggest that latent-space document enrichment may be a promising avenue for enhancing the performance of RAG systems, particularly in compute-constrained settings where it is only feasible to deploy a small model at inference time.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Vihan Lakshman, Peter Baile Chen, Zhuohan Gu, Michael Cafarella
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
