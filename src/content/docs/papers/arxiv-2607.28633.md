---
title: "Topology-Aware Data Movement for Disaggregated GPU Inference"
description: "Disaggregated LLM inference creates a datacenter networking problem that no existing system solves correctly."
---

**评分：45/100** · AI 基础设施 > 集群与资源系统 > 网络、RDMA 与互联

[论文原文](https://arxiv.org/abs/2607.28633) · [PDF](https://arxiv.org/pdf/2607.28633)

## 一句话摘要

Disaggregated LLM inference creates a datacenter networking problem that no existing system solves correctly.

## 为什么值得关注

待编辑增强。

## 摘要原文

Disaggregated LLM inference creates a datacenter networking problem that no existing system solves correctly. When prefill and decode run on separate GPU pools, the KV cache must be transferred between them. For a 70B model this is 1.3 GB per request, exceeding 100 GB/s aggregate at production scale. Yet DistServe, Splitwise, and Mooncake all use uniform RDMA, ignoring that bandwidth between two GPUs varies by 72x depending on their physical relationship: 900 GB/s via NVLink 4.0 within a domain (1.8 TB/s on NVLink 5, widening the gap to 144x), 50 GB/s via InfiniBand across nodes, 12.5 GB/s via TCP across data centers. We design a topology-aware transfer orchestrator that discovers interconnect hierarchy at startup and selects optimal transport per transfer. Three mechanisms work together: (1) pipelined layer-by-layer transfer that overlaps transmission with ongoing prefill, hiding 76 to 100 percent of transfer latency behind computation depending on transport, with NVLink and PCIe transfers hidden entirely; (2) NVLink domain-aware placement for Mixture-of-Experts models that co-optimizes expert dispatch with KV cache locality; and (3) CXL 3.0 memory expanders as a shared overflow tier providing 6x capacity at 86x lower latency than NVMe. Full evaluation requires multi-node clusters with heterogeneous interconnects and CXL 3.0 hardware that is beyond academic resources and not yet available in GPU clouds. We present analytical bandwidth models, component implementations, and projected analysis across three architectures showing 3 to 18x transfer latency reduction over uniform RDMA.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: infiniband, interconnect, rdma
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Sanjeev Rao Ganjihal
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
