---
title: "Bridging LLM Serving and CXL-SSDs with Chunk-Aware KV Cache Management"
description: "NAND-backed storage offers the capacity needed to scale LLM prefix caching, but its block I/O path incurs CPU cache contention and host-DRAM staging in addition to NAND latency."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.26828) · [PDF](https://arxiv.org/pdf/2609.26828)

## 一句话摘要

NAND-backed storage offers the capacity needed to scale LLM prefix caching, but its block I/O path incurs CPU cache contention and host-DRAM staging in addition to NAND latency.

## 为什么值得关注

待编辑增强。

## 摘要原文

NAND-backed storage offers the capacity needed to scale LLM prefix caching, but its block I/O path incurs CPU cache contention and host-DRAM staging in addition to NAND latency. Our characterization shows that these interface costs persist even with DRAM as the storage medium, motivating CXL-SSDs for byte-addressable access to NAND-backed capacity. Surprisingly, however, a stock CXL-SSD remains about 3$\times$ slower than local DRAM and no faster than an NVMe SSD, while generic prefetching provides little benefit. We present LM-CXD, a CXL-SSD specialized for LLM prefix caching. LM-CXD bridges the semantic gap between the serving engine, which knows which KV chunks will be consumed, and the device, which controls their placement and movement. It makes KV chunks device-visible I/O units, exposes NAND-to-DRAM progress to the serving engine, and uses device DRAM as a GPU-accessible buffer. LM-CXD further coordinates request scheduling with windowed prefetching and pipelines layerwise KV movement with GPU computation to hide NAND latency under limited device DRAM. Across five LLM models, LM-CXD reduces average TTFT over a stock CXL-SSD by up to 2.6$\times$ with compute asynchronous prefetching and 4.03$\times$ with layerwise prefetching, achieving TTFT within 1.5$\times$ of local DRAM on average.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, prefix caching
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hyunsun Chung, Taewan Noh, Minji Kim, Joo-Young Hwang, Hong-Yeon Kim, Youngjae Kim
- 发布：2026-09-20；更新：2026-09-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
