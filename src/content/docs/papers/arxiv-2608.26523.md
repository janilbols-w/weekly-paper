---
title: "VPP: Virtual Pipeline Parallelism for Efficient Chunked Prefill in Long-Context LLM Inference"
description: "Chunked prefill pipeline parallelism (CPP) is a key technique for LLM inference."
---

**评分：43/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2608.26523) · [PDF](https://arxiv.org/pdf/2608.26523)

## 一句话摘要

Chunked prefill pipeline parallelism (CPP) is a key technique for LLM inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Chunked prefill pipeline parallelism (CPP) is a key technique for LLM inference. However, equal-size chunks exhibit imbalanced latency, as later chunks attend longer prefix KV caches and incur higher attention costs, leading to pipeline bubbles. Existing approaches mitigate this imbalance through dynamic chunk resizing (Dynamic CPP, DCPP), but our measurements show that this trades scheduling overhead for load balancing, which becomes unfavorable on long sequences. In this study, we propose Virtual Pipeline Parallelism (VPP), which keeps chunk sizes fixed and optimizes the pipeline layout through virtual stages. A V-shaped virtual-stage traversal overlaps each chunk's expensive middle stages with the lighter head and tail stages of its neighbors, while asynchronous communication and pipelined packing further reduce communication stalls and cross-request drain bubbles. We implement VPP in vLLM-Ascend and evaluate it on three MoE-based LLMs with sequences up to 1M tokens on 16 Ascend 910C NPUs. VPP improves throughput by up to 13.1% over DCPP on long sequences and 6.7% on mixed workloads, while preserving performance on short sequences. On a 512K-token DeepSeek-V3.1 prefill workload, VPP reduces the pipeline bubble ratio from 6.4% to 0.1%, achieving a 98.0% reduction compared with DCPP.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: load balancing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yan Shi, Xiaochao Wang, Jingchun Gao, Jintao Luo, Xinyi Zhou, Feng Liu, Kui Luo, Xushi Li, Xinjie Guo, Liangjun Feng
- 发布：2026-08-27；更新：2026-08-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
