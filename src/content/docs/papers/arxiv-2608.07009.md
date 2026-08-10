---
title: "HiSparse: Scaling Sparse-Attention Decoding with Hierarchical KV Cache Management"
description: "Top-k sparse attention makes long-context LLM decoding cheap to compute: each step reads only a few thousand selected KV entries rather than the full context."
---

**评分：52/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.07009) · [PDF](https://arxiv.org/pdf/2608.07009)

## 一句话摘要

Top-k sparse attention makes long-context LLM decoding cheap to compute: each step reads only a few thousand selected KV entries rather than the full context.

## 为什么值得关注

待编辑增强。

## 摘要原文

Top-k sparse attention makes long-context LLM decoding cheap to compute: each step reads only a few thousand selected KV entries rather than the full context. Serving systems, however, typically keep the entire KV cache in GPU HBM so that every position stays selectable, so a request's memory bill still grows with its full context length--decoding hits a capacity wall long before it runs out of compute, and a context whose KV cache exceeds HBM cannot be served at all. We present HiSparse, an exact, indexer-agnostic hierarchical KV cache for sparse-attention serving. HiSparse keeps each request's full KV history in host memory and bounds its decode footprint with a small, fixed-size GPU cache; a fused CUDA kernel resolves each layer's selections--hit detection, LRU replacement, and host-to-device fetches--inside the decode CUDA graph; and, for models that share selections across layers, exact layer-wise prefetching hides roughly half of the remaining miss overhead. Because only KV placement changes, model outputs are unchanged. HiSparse is merged into upstream SGLang and evaluated across three sparse-attention families (DSA, NSA, and Quest) on H200, B200, and GH200 platforms: it improves peak generation throughput by up to 4.7x on long-context workloads while preserving comparable per-token latency and reducing time-to-first-token at high load--and a no-IO oracle shows the resolution mechanism itself adds no measurable per-token cost, leaving host-device IO as the only price of bounded residency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zhiqiang Xie, Zhangheng Huang, Tingwei Huang, Ziyi Xu, Ruiyang Ma, Christos Kozyrakis
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
