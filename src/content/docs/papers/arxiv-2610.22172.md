---
title: "Efficient KV Cache Migration for Geo-Distributed LLM Inference in Collaborative Edge Computing"
description: "Large Language Models (LLMs) have shown exceptional capabilities but rely heavily on centralized cloud GPU clusters, leading to high bandwidth costs, latency, and privacy issues."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.22172) · [PDF](https://arxiv.org/pdf/2610.22172)

## 一句话摘要

Large Language Models (LLMs) have shown exceptional capabilities but rely heavily on centralized cloud GPU clusters, leading to high bandwidth costs, latency, and privacy issues.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) have shown exceptional capabilities but rely heavily on centralized cloud GPU clusters, leading to high bandwidth costs, latency, and privacy issues. Edge computing offers a solution by deploying LLMs closer to users on edge servers, yet single edge servers often cannot meet LLMs' heavy computational demands. Collaborative Edge Computing (CEC) addresses this challenge by integrating resources of multiple geo-distributed heterogeneous edge servers, which jointly host small model shards and associated Key-Value (KV) cache for distributed inference. However, edge servers may disconnect or easily become overloaded, making it essential to migrate stateful KV cache to other servers for ensuring continuous service. Existing cloud-based KV cache management methods, such as direct cross-GPUs transmission and recomputation from input tokens are ill-suited for bandwidth-constrained and resource-limited edge environments. In this work, we propose EdgeFlow, a novel hybrid KV cache migration scheme that integrates direct KV cache transmission with activation-based recomputation, leveraging parallel computation and communication to minimize migration time. On this basis, we formulate a multi-node KV migration optimization problem and design a 2-approximation algorithm based on improved linear programming relaxation and bipartite graph techniques. Extensive experiments on a real-world distributed LLM inference platform demonstrate that EdgeFlow reduces migration time by up to 45%, significantly enhancing the robustness and efficiency of distributed LLM inference in collaborative edge computing.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mingjin Zhang, Jiannong Cao, Tao Wu, Xiangchun Chen, Ne Wang
- 发布：2026-10-15；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
