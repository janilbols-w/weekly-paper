---
title: "ReelCache: An Efficient KV Cache Compression and Management System for Multi-Round Video Generation"
description: "Autoregressive video diffusion models produce large KV caches during multi-round video generation."
---

**评分：52/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.09973) · [PDF](https://arxiv.org/pdf/2611.09973)

## 一句话摘要

Autoregressive video diffusion models produce large KV caches during multi-round video generation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Autoregressive video diffusion models produce large KV caches during multi-round video generation. Keeping all these KV chunks would consume substantial memory, while rebuilding discarded caches would significantly delay video chunk generation. This paper presents ReelCache, a KV cache compression system for efficient multi-round, long video generation. ReelCache combines an intra-chunk compressor with an inter-chunk cache manager. The compressor applies low-rank decomposition across channels and video coding to the resulting coefficients, predicting the decomposition rank per transformer layer online to meet retained-energy targets. The cache manager shares basis directions across consecutive chunks and organizes chunk states in a tree, allowing generation branches to share historical state while supporting restoration for resume, rewind, and fork. Experiments across five video generation models show that ReelCache reduces KV storage by 14.46-21.13x relative to baselines and accelerates next-chunk generation by 1.25-3.36x, with less than 1% drop in six representative VBench metrics. GitHub: https://github.com/Tianyu9748/ReelCache

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Tianyu Wang, Daiyang Yu, Zhiwei Ren, Junbo Li, Jitian Zhang, Longfei Shangguan
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Tianyu9748/ReelCache](https://github.com/Tianyu9748/ReelCache)
- 阅读深度：metadata
