---
title: "Characterizing Predictability-Latency Trade-offs of KV-Cache SSD Offloading in LMCache for LLM Serving Systems"
description: "KV-cache offload is widely used to stretch GPU memory for LLM serving, but its storage behavior has not been characterized at the block-device level."
---

**评分：49/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.21249) · [PDF](https://arxiv.org/pdf/2610.21249)

## 一句话摘要

KV-cache offload is widely used to stretch GPU memory for LLM serving, but its storage behavior has not been characterized at the block-device level.

## 为什么值得关注

待编辑增强。

## 摘要原文

KV-cache offload is widely used to stretch GPU memory for LLM serving, but its storage behavior has not been characterized at the block-device level. In this paper, we study LMCache through realworld multi-session workloads that span same/different context x same/different prompt, using over 100 stateless requests per workload. Our comparison is observational rather than factorial: it contrasts two realizable deployment snapshots -- LMCache 0.3.0 with buffered I/O and the kernel page cache, and LMCache 0.3.16 with prefix-aware deduplication and O_DIRECT. Key findings define the paper. First, the legacy stack appears almost read-free at the SSD layer in all four workloads, but a flush_ram experiment shows that this is conditional on page-cache warmth: once the cache is evicted, the same path issues about 1 GB of sequential reads in 683 ms. Second, deduplication delivers a dramatic write reduction only for the exact-repeat workload: one set collapses from 1.62 GB to 11.75 MB of writes, while the other three sets remain in the 2-5 GB range. Third, O_DIRECT converts a hidden and bimodal read cost into an explicit and stable one: on one set, warm TTFT rises from 27 ms to 93 ms because each of the 99 warm requests re-reads the same ~12 MB partial chunk from SSD. The main conclusion is therefore not "newer is better," but a system trade-off: predictability versus average-case latency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory, offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ying He, Dingsen Shi, Yanbo Dai, Donger Chen, Harry Fu, Chris Tsu, Wang Feng, Song Fu
- 发布：2026-10-15；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
