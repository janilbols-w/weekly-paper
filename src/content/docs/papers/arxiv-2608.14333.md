---
title: "Beyond Capacity: Scalable MoE LLM Inference via High-Bandwidth Flash with Direct GPU and HBM Paths"
description: "Modern mixture-of-experts (MoE) language models increasingly strain the capacity and cost efficiency of high-bandwidth memory (HBM), as rapidly growing expert weights must be provisioned close to GPUs."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.14333) · [PDF](https://arxiv.org/pdf/2608.14333)

## 一句话摘要

Modern mixture-of-experts (MoE) language models increasingly strain the capacity and cost efficiency of high-bandwidth memory (HBM), as rapidly growing expert weights must be provisioned close to GPUs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern mixture-of-experts (MoE) language models increasingly strain the capacity and cost efficiency of high-bandwidth memory (HBM), as rapidly growing expert weights must be provisioned close to GPUs. High-bandwidth flash (HBF) offers substantially greater capacity, but conventional designs typically deliver HBF-resident expert weights to the GPU through HBM, leaving an additional direct GPU-HBF connection underutilized. We explore an HBF organization that simultaneously exploits two independent expert-delivery routes: a direct path that transfers expert weights from HBF to the GPU and a relay path that transfers them from HBF through the HBM base die to the GPU. Whole experts are assigned to one of the two routes, and transfers over both routes proceed concurrently, increasing aggregate expert-delivery bandwidth without replicating expert weights or introducing a shared relay bottleneck. Early expert determination identifies upcoming experts ahead of their conventional execution point, allowing HBF read latency to overlap with preceding computation, while separate management of immutable expert weights and mutable KV-cache data reduces interference between the two traffic classes. We evaluate the architecture using an event-driven continuous-batching LLM serving simulator with empirically measured GPU compute latencies. Across representative MoE workloads, concurrently utilizing the direct GPU-HBF and HBF-HBM-GPU routes consistently improves expert-delivery efficiency over designs restricted to either route alone. For a representative workload, the proposed architecture can achieve 1.94$\times$ higher throughput and 1.90$\times$ end-to-end speedup over a design that delivers all HBF-resident expert weights to the GPU through the HBM base die.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 15 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Seeyeon Kim, Juhyeong Jin, Joo-Young Kim
- 发布：2026-08-17；更新：2026-08-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
