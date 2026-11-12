---
title: "Decode Token Parallelism: Memory-Efficient Distributed Attention Parallelism for Scalable LLM Decoding"
description: "Serving large language models at high concurrency with long contexts requires KV-cache capacity and attention bandwidth that grow with the decode pool."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.13293) · [PDF](https://arxiv.org/pdf/2611.13293)

## 一句话摘要

Serving large language models at high concurrency with long contexts requires KV-cache capacity and attention bandwidth that grow with the decode pool.

## 为什么值得关注

待编辑增强。

## 摘要原文

Serving large language models at high concurrency with long contexts requires KV-cache capacity and attention bandwidth that grow with the decode pool. Existing parallelization strategies trade one against the other: data parallelism replicates model weights, limiting KV capacity; tensor parallelism stops scaling attention at the model's KV-head count and pushes dense collectives across nodes; and decode context parallelism (DCP) recovers capacity by sharding the sequence but adds cross-node aggregation of partial attention results. We observe that during decode, dense layers and attention scale differently: dense layers amortize weight reads across the batch and run efficiently within a single NVLink domain, whereas attention cost grows with every active request's KV cache. We present Decode Token Parallelism (TKNP), a decode-pool architecture that decouples weight placement from attention ownership. TKNP distributes a single model copy across nodes in balanced layer blocks. The active node holding a block executes its projections and MLP for the full batch using intra-node tensor parallelism, while every node computes attention for its own requests against locally resident KV cache. This extends request-local attention across nodes without replicating weights: only current-token activations cross the network, dense all-reduces remain within NVLink, and attention requires no cross-node merging of partial results. Implemented in vLLM and evaluated on Llama 3.1 405B and Nemotron-4 340B on up to 64 H100 GPUs, TKNP improves completion throughput for long-context, high-concurrency workloads by up to 1.7$\times$ over DCP and by up to 2.06$\times$ over data parallelism at matched GPU count.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Susav Shrestha, Brad Settlemyer, Narasimha Reddy
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
