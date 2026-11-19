---
title: "XM-Sparse: High-Throughput Sparse-Attention LLM Serving over Scale-up Memory Pools"
description: "Sparse attention has been increasingly adopted by production LLMs for long-context inference, yet serving systems must still retain the full KV history, making GPU HBM capacity a key limit on serving concurrency."
---

**评分：45/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.22280) · [PDF](https://arxiv.org/pdf/2611.22280)

## 一句话摘要

Sparse attention has been increasingly adopted by production LLMs for long-context inference, yet serving systems must still retain the full KV history, making GPU HBM capacity a key limit on serving concurrency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Sparse attention has been increasingly adopted by production LLMs for long-context inference, yet serving systems must still retain the full KV history, making GPU HBM capacity a key limit on serving concurrency. Existing systems offload the KV cache to host memory, but suffer from the limited bandwidth of PCIe and the limited capacity of host memory. Emerging scale-up memory pools (e.g., X-Mem) relieve both limits and open new opportunities for sparse-attention offloading. In this paper, we first conduct an in-depth analysis and reveal that, even with scale-up memory pools, decode throughput remains bounded by HBM capacity, as hot KV buffers and the fully resident indexer key (K-index) cache occupy substantial HBM. Moreover, the two caches exhibit distinct access patterns. Based on these insights, we present XM-Sparse, the first sparse-attention offloading system over scale-up memory expansion. The core idea of XM-Sparse is to offload both caches aggressively while matching each with an I/O mechanism tailored to its access pattern. Specifically, for dynamically selected KV entries, XM-Sparse fuses TMA-based retrieval with attention in a tile-level pipeline to hide on-demand retrieval latency. For predictable K-index accesses, it prefetches pages via SM-efficient GPU-initiated DMA and coordinates prefetching with latency-critical operations to avoid interfering with decoding. We have implemented XM-Sparse atop SGLang, and our experiments on DeepSeek-V3.2 and GLM-5.3 with an emulated scale-up memory pool show that XM-Sparse delivers up to 4.98$\times$ and 4.52$\times$ higher decode throughput than PCIe-based ECHO and HiSparse, respectively, and up to 1.34$\times$ over a naive integration on the same platform, across 16K-1M contexts.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yijun Sun, Xudong Liao, Zhuobin Huang, Kai Chen, Nikita Lazarev, Zhizhen Zhong
- 发布：2026-11-18；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
