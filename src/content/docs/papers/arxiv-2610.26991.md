---
title: "3D-MoE: Complementarity-Guided Hardware-Software Co-Design for MoE Decode on 3D-Stacked NMP"
description: "Mixture-of-Experts (MoE) have become a mainstream way to scale Large Language Models (LLMs), because each token activates only a small subset of experts, reducing inference cost."
---

**评分：45/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2610.26991) · [PDF](https://arxiv.org/pdf/2610.26991)

## 一句话摘要

Mixture-of-Experts (MoE) have become a mainstream way to scale Large Language Models (LLMs), because each token activates only a small subset of experts, reducing inference cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) have become a mainstream way to scale Large Language Models (LLMs), because each token activates only a small subset of experts, reducing inference cost. However, MoE decode remains highly memory-bound and exhibits strongly skewed, time-varying expert loads. 3D-stacked DRAM near-memory processing (NMP) provides the bandwidth that decode demands, yet its tiled organization makes load balancing expensive: expert parallelism (EP) preserves locality but suffers from hotspot-induced imbalance, while more distributed strategies weaken locality and increase NoC traffic. To address this locality-balance conflict, we observe that domain-specialized token routing creates offsetting expert-load fluctuations across decode steps, a property we call expert complementarity. Using this insight, we propose 3D-MoE, a hardware--software co-designed system for MoE decode on 3D-stacked NMP. 3D-MoE uses offline, one-time complementarity-guided grouping and locality-aware mapping to establish coarse-grained inter-group balance, handles residual intra-group hotspots through a lightweight Collaborative Memory-Network (CMN) that streams each hot expert's weight tiles once from its host DRAM channel to helper cores over a reconfigured local broadcast path, and uses cost-aware online remapping to remain robust to workload drift. Across MoE models, 3D-MoE achieves an average 4.63$\times$ MoE-layer speedup over EP and improves end-to-end throughput by 1.58$\times$--1.86$\times$ over the strongest NMP baselines, with 2.11\% additional logic-die area.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: load balancing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yudong Pan, Lian Liu, Shixin Zhao, Yintao He, Kaiyan Chang, Tianhua Han, Chenyang Ai, Haonan Zhu, Mengdi Wang, Yinhe Han, Ying Wang
- 发布：2026-10-21；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
