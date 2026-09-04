---
title: "mzCache: On-Device LLM Memory Management under Multitasking"
description: "On-device mobile Large Language Model (LLM) inference is gaining significant attention."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2609.01338) · [PDF](https://arxiv.org/pdf/2609.01338)

## 一句话摘要

On-device mobile Large Language Model (LLM) inference is gaining significant attention.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-device mobile Large Language Model (LLM) inference is gaining significant attention. However, mobile devices operate in highly dynamic multitasking environments where users frequently switch between applications. This creates memory pressure, forcing LLM memory (model weights and KV cache) to be evicted by the operating system. When a new inference request arrives, the inference system must restore the evicted memory through slow storage reads or recompute the entire KV cache, severely degrading responsiveness. To address this, we present mzCache, an on-device LLM inference system with specialized memory management for multitasking environments. Under unpredictable memory pressure, mzCache elastically evicts LLM memory and leverages the unified memory of mobile SoCs to enable zero-wait inference on the GPU with concurrent CPU-side restoration. mzCache realizes this through restoration-oriented memory management: LLM memory is partitioned into fine-grained shared buffers to enable partial eviction and restoration with concurrent cross-processor access, while hybrid swap and backward-out eviction policies ensure low-latency restoration from any eviction state. Implemented on llama.cpp and deployed as an Android application, mzCache achieves 2.1-5.5$\times$ reduction in Time-to-First-Token compared to storage-backed partial offload and demonstrates its effectiveness in real multitasking scenarios.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: memory management, unified memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hongseung Yu, Minsung Kim, Jongseok Park, Kyunghan Lee
- 发布：2026-09-01；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
