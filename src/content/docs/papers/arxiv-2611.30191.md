---
title: "Making Protocol Effects Explicit: LLM-to-Packet Simulation for Superpod Interconnect Exploration"
description: "Large language models (LLMs) have become the foundation of modern AI services."
---

**评分：44/100** · AI 基础设施 > 集群与资源系统 > 网络、RDMA 与互联

[论文原文](https://arxiv.org/abs/2611.30191) · [PDF](https://arxiv.org/pdf/2611.30191)

## 一句话摘要

Large language models (LLMs) have become the foundation of modern AI services.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) have become the foundation of modern AI services. The rapid growth of LLM sizes and context lengths has exceeded the memory capacity of a single GPU or NPU, requiring model partitioning across devices. However, partitioning models across devices introduces costly communication overhead, driving the need for superpods with large-scale, high-bandwidth, low-latency scale-up fabrics. Exploring superpod designs requires accurate interconnect simulation, as communication latency is jointly determined by link technologies, topologies, and scale-up protocol-stack choices. Latency-bandwidth models estimate communication latency using a startup term and a transfer term derived from message size and effective bandwidth. But they fail to capture contention and protocol effects. Packet-level simulators like ns-3 model routing, queueing, and packet timing, but require protocol-specific LLM-to-packet implementations. This paper presents ProtoBridge, an ns-3-based LLM-to-packet simulator for superpod interconnect exploration. To make protocol effects explicit, ProtoBridge introduces two abstraction layers over ns-3: (1) an operation-to-packet (OTP) layer that captures protocol-specific packet exchanges and dependencies, and (2) a packet-execution (PEX) layer that applies shared packet-level mechanisms to the ns-3 event system. ProtoBridge achieves average latency error of 17.8\% on H200 NVLink4 and 10.3\% on C500 MetaXLink. To enable faster superpod evaluation for further interconnect exploration, we derive a surrogate model that combines OTP parameters with analytical models of PEX mechanisms. The surrogate reduces evaluation time from 2.38$\sim$75.70s to 20.5us per operation. We use ProtoBridge to analyze two emerging superpod designs, scale-up memory pool and co-packaged optics (CPO) interconnects, revealing design insights for future LLM superpod architectures.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: interconnect
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yu Zhu, Xinhao Yang, Zhaoshi Li, Baodong Wu, Boxun Li, Wenxue Li, Guohao Dai, Hongyang Jia, Shuwen Deng, Huazhong Yang, Yuan Xie, Zhenhua Zhu, Yu Wang
- 发布：2026-11-23；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
