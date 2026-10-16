---
title: "Range: Decoupling KV-Cache Reuse Granularity from Storage Work"
description: "LLM serving reuses cached key-value (KV) state to skip prefill, and growing contexts push that state past GPU HBM and CPU DRAM onto NVMe SSDs, placing prefix restore on the critical path of time-to-first-token (TTFT)."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.21241) · [PDF](https://arxiv.org/pdf/2610.21241)

## 一句话摘要

LLM serving reuses cached key-value (KV) state to skip prefill, and growing contexts push that state past GPU HBM and CPU DRAM onto NVMe SSDs, placing prefix restore on the critical path of time-to-first-token (TTFT).

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM serving reuses cached key-value (KV) state to skip prefill, and growing contexts push that state past GPU HBM and CPU DRAM onto NVMe SSDs, placing prefix restore on the critical path of time-to-first-token (TTFT). We find that on a well-configured host-issued path the SSD is not the bottleneck: restoring the same 6 GiB of KV takes 2.1 s as 192 objects but 3.0 s as 6,144 objects, and more under layerwise loading, because every layer of the storage stack - lookup, allocation, I/O submission, GPU delivery, store, index - charges per logical object while the bytes stay the same. This cost grows with the KV footprint: longer contexts, deeper models under layerwise loading, and tensor parallelism each multiply the object count. Prior systems move this per-object work from the CPU to the GPU; the work remains per object. This paper presents Range, a KV-cache storage engine for vLLM and LMCache built on one principle: every cost on the storage path scales with bytes or physical batches, never with logical objects. Range tickets replace per-key lookup and ownership with token metadata and physical leases; byte stripes make the on-media layout independent of reuse granularity; completion-owned GPU transfer banks batch delivery and extraction and release each layer to attention as it lands. Range keeps the kernel cuFile path and changes four lines of vLLM. On a fixed 6 GiB restore, Range's median TTFT stays at 1.79-1.80 s across a 32x range of object counts and under layerwise delivery, within 70 ms of the prefix already being resident in GPU memory, while tuned in-process LMCache rises from 2.12 s to 3.01 s. Range improves on the fastest multiprocess DRAM-bounced path by 0.44 s at coarse granularity while moving no payload through host memory, and holds layerwise reuse at the cost of coarse-grained reuse, where the best stock path takes 2.24 s.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Dingsen Shi, Jiahao Zhang, Liqiang Lv, Boming Huang, Yanbo Dai, Ying He, Donger Chen, Harry Fu, Wang Feng, Song Fu
- 发布：2026-10-15；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
