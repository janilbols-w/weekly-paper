---
title: "CHIPSMORE: Compute-in-Interconnect and -Memory Chiplets for Multi-Mode Multi-Request LLM Inference Acceleration"
description: "Large language model (LLM) inference exhibits substantial variability across adaptation modes, context lengths, and request concurrency, creating challenges for maintaining high utilization, memory efficiency, and scalable performance on compute-in-memory (CIM) accelerators."
---

**评分：48/100** · AI 基础设施 > 集群与资源系统 > 网络、RDMA 与互联

[论文原文](https://arxiv.org/abs/2608.30509) · [PDF](https://arxiv.org/pdf/2608.30509)

## 一句话摘要

Large language model (LLM) inference exhibits substantial variability across adaptation modes, context lengths, and request concurrency, creating challenges for maintaining high utilization, memory efficiency, and scalable performance on compute-in-memory (CIM) accelerators.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) inference exhibits substantial variability across adaptation modes, context lengths, and request concurrency, creating challenges for maintaining high utilization, memory efficiency, and scalable performance on compute-in-memory (CIM) accelerators. This paper presents CHIPSMORE, a multi-mode and multi-request LLM inference accelerator that integrates compute-in-interconnect and CIM to support both base-mode and low-rank adaptation (LoRA) inference under diverse workloads. CHIPSMORE employs heterogeneous processing elements consisting of resistive RAM analog compute-in-memory (RRAM-ACIM) and static RAM digital compute-in-memory (SRAM-DCIM) interconnected through a programmable Inter-PE computational network (IPCN). A composable hierarchical key-value (KV) memory scheme dynamically allocates router scratchpad, SRAM-DCIM, and embedded DRAM (eDRAM) resources according to workload requirements, enabling scalable support for long-context and batched inference. Furthermore, a non-replicated multi-request execution pipeline exploits request-level parallelism without duplicating pretrained weights, while a state-aware resource reconfiguration mechanism selectively retains runtime states and power-gates inactive resources to improve energy efficiency. Evaluation using cycle-accurate hardware-software co-simulation demonstrates that CHIPSMORE effectively sustains high throughput across varying model sizes, context lengths, and batch sizes while maintaining favorable power scaling. Compared with Nvidia H100, CHIPSMORE achieves up to $2.38\times$ higher throughput and $27\times$ higher energy efficiency on Mistral-7B inference while eliminating weight replication for multi-request serving.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: interconnect
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yue Jiet Chong, Yimin Wang, Zhen Wu, Zixuan Wang, Wei Zhang, Xuanyao Fong
- 发布：2026-08-31；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
