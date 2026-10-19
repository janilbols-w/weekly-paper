---
title: "MemLLM: End-to-end In-Storage Acceleration of On-device Retrieval-Augmented Generation using Precomputed KV Caches"
description: "Retrieval-augmented generation (RAG) on edge devices enables personalized large language model (LLM) inference while preserving privacy."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.22579) · [PDF](https://arxiv.org/pdf/2610.22579)

## 一句话摘要

Retrieval-augmented generation (RAG) on edge devices enables personalized large language model (LLM) inference while preserving privacy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Retrieval-augmented generation (RAG) on edge devices enables personalized large language model (LLM) inference while preserving privacy. However, RAG's inherent length asymmetry makes the prefill phase the dominant bottleneck. While precomputing the KV caches offline alleviates the prefill cost on server systems, the multi-gigabyte caches over the narrow interconnect create a severe I/O wall for on-device systems. To mitigate this, we propose MemLLM, an end-to-end in-storage processing (ISP) architecture that executes the complete attention pipeline based on precomputed KV caches within the SSD. MemLLM utilizes per-channel accelerators to fully utilize the aggregated NAND channel bandwidth and accelerates all KV cache-related computations on the storage-side to minimize PCIe transfers. To efficiently handle the sparse updates required by RAG, MemLLM introduces a fused recomputation-query kernel paired with a hardware-based filter logic to halve the NAND read volume and eliminate write-back penalties. Furthermore, MemLLM's global SRAM-based stateful reduction engine enables a completely DRAM-less dataflow, thereby removing the internal memory bottlenecks and bounding the PCIe egress to an $O(1)$ footprint. A full-stack software stack allows asynchronous, zero-copy transfers from the ISP to the host and provides transparent execution within modern ML frameworks. Evaluated across eight real-world RAG datasets and six on-device LLM models, MemLLM achieves an average end-to-end speedup of 4.06$\times$ over the GPU baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Seungkwan Kang, Hyungseok Ko, Heemin Kim, Myoungsoo Jung
- 发布：2026-10-19；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
