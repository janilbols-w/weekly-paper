---
title: "A Flat KV Cache Storage Architecture for LLM Serving"
description: "KV cache reuse accelerates LLM serving, but existing systems manage host DRAM and NVMe SSD as a tiered hierarchy where DRAM acts as an intermediate cache."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.38355) · [PDF](https://arxiv.org/pdf/2610.38355)

## 一句话摘要

KV cache reuse accelerates LLM serving, but existing systems manage host DRAM and NVMe SSD as a tiered hierarchy where DRAM acts as an intermediate cache.

## 为什么值得关注

待编辑增强。

## 摘要原文

KV cache reuse accelerates LLM serving, but existing systems manage host DRAM and NVMe SSD as a tiered hierarchy where DRAM acts as an intermediate cache. Production LLM workloads break both premises of this hierarchy. First, bimodal reuse defeats DRAM temporal filtering, since workloads are dominated either by one-shot blocks with long reuse distances or by multi-gigabyte agentic sessions that exceed DRAM capacity, putting SSD on the critical read path. Second, DRAM staging and eviction-ordered layout bottleneck SSD restoration. Holding host staging buffers for in-flight prefixes causes contention under load that aborts prefetches, while incremental eviction scatters a session's blocks across the SSD and prevents large sequential reads. We present FlatCake, a flat KV storage architecture that exposes host DRAM and NVMe SSD as peer media in a unified 64-bit address space. Exploiting the fact that KV blocks are write-once, immutable, and reused together within a prompt or session, FlatCake places each block directly onto its target medium in session-contiguous, layer-major order at creation time and never migrates it. FlatCake streams coalesced SSD reads directly into a bounded GPU window via GPUDirect Storage and decouples DRAM and SSD request queues to prevent head-of-line blocking. We implement FlatCake in SGLang and compare it against host-staged (Mooncake) and GDS-enabled (Mooncake-GDS) tiered storage, as well as SSD-direct storage (Tutti). Across three production agentic, coding, and conversational traces with DeepSeek-V4-Flash, FlatCake reduces mean TTFT near the baselines' latency knees by $1.40\times$--$2.42\times$ over the fastest baseline. On the agentic Claude Code trace, FlatCake sustains a 91.6% cache hit rate under load (versus 71.1% for all three baselines) and delivers up to $2.16\times$ higher token throughput.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xin Huang, Teng Ma, Zhuoran Li, Yibo Zhao, Zhaoshi Li, Qianchao Zhu, Wei Yang, Chenxi Wang, Tao Xie, Youwei Zhuo
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
