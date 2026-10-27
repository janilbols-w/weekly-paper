---
title: "MCF: A Memory- and Communication-Aware Co-Designed Framework for Long-Context LLM Inference"
description: "This paper presents Memory- and Communication-Aware Framework for Long-Context LLM Inference (MCF) that optimizes long-context inference through communication-aware and stage-adaptive KV-cache layout transitions."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.34731) · [PDF](https://arxiv.org/pdf/2610.34731)

## 一句话摘要

This paper presents Memory- and Communication-Aware Framework for Long-Context LLM Inference (MCF) that optimizes long-context inference through communication-aware and stage-adaptive KV-cache layout transitions.

## 为什么值得关注

待编辑增强。

## 摘要原文

This paper presents Memory- and Communication-Aware Framework for Long-Context LLM Inference (MCF) that optimizes long-context inference through communication-aware and stage-adaptive KV-cache layout transitions. At the core of MCF is {Memory-Aware Replication and Scheduling} (MARS), a dynamic orchestration mechanism for chunked prefill. MARS exploits early-stage memory headroom by selectively replicating highly reused KV blocks, improving locality and hiding KV propagation latency behind attention computation. As prefill progresses and memory pressure increases, MARS progressively drains redundant replicas and converges the KV cache into a sharded decode-ready layout, avoiding expensive layout conversion at the prefill--decode boundary. For decoding, MCF adopts a query-centric execution model in which KV shards remain stationary while lightweight query tensors are routed across workers. This changes communication from KV-cache-dependent transfer to query-dependent transfer, reducing communication growth with context length. MCF further integrates a hardware-software co-designed execution layer based on an FPGA compute-NIC datapath, enabling metadata-driven KV routing and collective operations directly in the network path. Experiments show that MCF improves TTFT, throughput, and scalability over state-of-the-art distributed inference systems, with larger benefits as context length and cluster size increase.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Huaizhi Zhang, Jiacheng Zhu, Xuqi Zhu, Junkyu Lee, Klaus McDonald-Maier, Xiaojun Zhai
- 发布：2026-10-27；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
