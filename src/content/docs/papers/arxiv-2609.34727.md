---
title: "Dynamic Flow, Static Graph: KV Cache Reuse for Efficient LLM Serving on Mobile NPUs"
description: "On-device large language model (LLM) serving is a cornerstone of local-first personal intelligence, offering users data sovereignty, strong privacy guarantees, and freedom from cloud API latency and cost."
---

**评分：48/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2609.34727v1) · [PDF](https://arxiv.org/pdf/2609.34727v1)

## 一句话摘要

On-device large language model (LLM) serving is a cornerstone of local-first personal intelligence, offering users data sovereignty, strong privacy guarantees, and freedom from cloud API latency and cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-device large language model (LLM) serving is a cornerstone of local-first personal intelligence, offering users data sovereignty, strong privacy guarantees, and freedom from cloud API latency and cost. Although KV caching is widely used to reduce latency in long-context inference, existing designs were primarily optimized for cloud GPUs with dynamic execution environments and abundant memory bandwidth. These architectural assumptions do not hold on mobile NPUs, where computation graphs must be statically compiled and both memory capacity and I/O bandwidth are severely constrained. In this work, we present a compute-storage co-design for mobile-centric prefix and non-prefix KV reuse. We first propose an intra-graph mechanism that maps selective KV recomputation onto static NPU graphs, reconciling algorithmic dynamicity with NPU staticity. We further develop an inter-graph scheduler to optimize chunk merging and minimize padding with dynamic programming. To address mobile bandwidth limitations, we introduce a hierarchical KV manager featuring a tree-hash-semantic hybrid structure, along with cost-aware prefetching and eviction policies. We also build a two-dimensional pipeline that overlaps KV loading, rerotation, and storage with NPU execution, hiding data-movement latency. Experiments across representative on-device workloads and LLMs show that our design reduces time-to-first-token (TTFT) by $40-60\%$ compared with no reuse and prefix-only caching.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhengxiang Huang, Shengheng Chen, Chaoyue Niu, Yujie Sun, Zhaode Wang, Zeyu Zhao, Chengfei Lv, Fan Wu, Guihai Chen
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
