---
title: "NUNA: Characterizing and Mitigating Non-Uniform Network Access in Multi-Die GPU Scale-Up Systems"
description: "Graphics processing unit (GPU) architectures are growing in size to meet the increasing compute and memory requirements."
---

**评分：45/100** · LLM 高效推理 > Serving 与分布式推理 > 并行与通信

[论文原文](https://arxiv.org/abs/2608.00867) · [PDF](https://arxiv.org/pdf/2608.00867)

## 一句话摘要

Graphics processing unit (GPU) architectures are growing in size to meet the increasing compute and memory requirements.

## 为什么值得关注

待编辑增强。

## 摘要原文

Graphics processing unit (GPU) architectures are growing in size to meet the increasing compute and memory requirements. As GPU sizes increase, intra-socket wire transfer delay increases significantly. While previous research has optimized for compute and memory locality within a socket, the spatial impact on inter-GPU communication has not been well-studied. We introduce the term non-uniform network access (NUNA) to describe this emerging optimization dimension in multi-GPU systems. We specifically focus on latency-sensitive collective communication, common in machine learning inference. First, we highlight the need for NUNA-aware routing (NAR), choosing optimized, spatially-aware inter-GPU paths in large scale-up network topologies. Second, we introduce NUNA-aware placement (NAP), placing threadblocks and data near I/O to optimize the inter-GPU traffic. We demonstrate that the NAP optimizations alone offer up to 1.5x collective speedups over a locality-unaware baseline. Combining NAP with NAR yields up to 1.8x faster collectives over the locality-unaware baseline. This leads to 7% mean (28% max) time per output token speedup in machine learning inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: collective communication
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Conor James Green, William Won, Tuan Ta, Bradford M. Beckmann
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
