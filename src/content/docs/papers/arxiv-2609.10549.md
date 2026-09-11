---
title: "Compass: Dissecting Communication and Computation Operators for Efficient LLM Training"
description: "Overlapping communication and computation operators is a common practice to hide communication overheads, accelerating large language models (LLMs) training on GPU clusters."
---

**评分：48/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2609.10549) · [PDF](https://arxiv.org/pdf/2609.10549)

## 一句话摘要

Overlapping communication and computation operators is a common practice to hide communication overheads, accelerating large language models (LLMs) training on GPU clusters.

## 为什么值得关注

待编辑增强。

## 摘要原文

Overlapping communication and computation operators is a common practice to hide communication overheads, accelerating large language models (LLMs) training on GPU clusters. Existing systems achieve this through either intra-operator fusion (IntraFusion), which packs operators into a single large kernel, or inter-operator decomposition (InterDecom), which splits a tensor into multiple parts for pipelined execution. However, current IntraFusion methods underutilize network topology, causing suboptimal bandwidth usage on multi-GPU systems, while InterDecom struggles to determine the optimal number of decomposed parts for peak performance. To address these issues, we introduce Compass, which employs systematic optimization and comprehensive modeling. First, we design a novel IntraFusion algorithm leveraging double-ring communications to maximize bandwidth utilization in hybrid NVLink-PCIe systems, achieving 1.5x-2.5x speedups. Second, we develop a decomposition model that mathematically derives the optimal tensor decomposition degree for InterDecom, improving performance by up to 1.3x. Finally, we develop a unified performance framework that accurately determines the best strategy for different scenarios. We validate Compass through extensive evaluation across 288 configurations and end-to-end experiments on real-world applications. The results demonstrate that Compass consistently selects the optimal strategy, achieving up to a 1.42x end-to-end speedup compared to the Megatron-LM baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 11 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: operator fusion
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Guangyu Xiang, Lin Zhang, Haoxuan Yu, Xinglin Pan, Shaohuai Shi, Xiaowen Chu
- 发布：2026-09-11；更新：2026-09-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
