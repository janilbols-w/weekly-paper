---
title: "AdaSprite: Resource-efficient Online Co-Adaptation for V2I Systems Under Large-scale Data Drifts"
description: "The rise of vehicle-infrastructure (V2I) collaboration enables safer and broader perception."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2608.16188) · [PDF](https://arxiv.org/pdf/2608.16188)

## 一句话摘要

The rise of vehicle-infrastructure (V2I) collaboration enables safer and broader perception.

## 为什么值得关注

待编辑增强。

## 摘要原文

The rise of vehicle-infrastructure (V2I) collaboration enables safer and broader perception. To process large-scale V2I video streams, vision-language models (VLMs) are promising as they unify multi-view vision into end-to-end task grounding, reducing handcrafted design. We use Vision Mixture-of-Experts (V-MoE) as the distributed visual backbone of VLMs, leveraging sparse expert routing to enable conditional computation across diverse viewpoints under resource constraints. Yet, V-MoEs face a critical challenge: large-scale data shifts over minutes to hours in V2I systems, amplified by agnostic participants and biased features propagating through experts. To maintain accuracy efficiently, we find it beneficial to co-adapt multiple V-MoEs on edge servers, avoiding the latency and privacy risks of cloud offloading and the accuracy sacrifices of on-device methods. However, the resource-constrained edge poses challenges for efficient co-adaptation: i) DRAM fragmentation and imbalance limit expert parallelism, ii) memory-I/O bottlenecks restrict computation reuse, and iii) asynchronous adaptation increases task-switch overhead. Also, prior work rarely explores the upper bound of concurrent tasks under limited edge resources, a critical factor for practical V2I deployment. To address these, we present AdaSprite. By combining cooperative elastic scaling with multi-level multiplexing, AdaSprite optimizes expert lifespans to reduce DRAM fragmentation, exploits predictable activation patterns for efficient I/O reuse, and employs twin-buffer scheduling to leverage sparsity. On a weak edge, AdaSprite supports up to 17 concurrent V2I tasks (vs. up to 6 for baselines), improving SLO attainment by 1.6x and throughput by 2.1x. Also, it allows users to trade accuracy and concurrency for second-level adaptation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Lehao Wang, Zhiwen Yu, Sicong Liu, Kefan Chen, Fengmin Wu, Bin Guo
- 发布：2026-08-18；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
