---
title: "Bandwidth-Aware and Cost-Efficient Pipeline Parallel Scheduling in Geo-Distributed LLM Training"
description: "The rapid evolution of large language models (LLMs) has made geographically distributed training necessary due to GPU scarcity within a single cloud region."
---

**评分：44/100** · LLM 高效推理 > Serving 与分布式推理 > 并行与通信

[论文原文](https://arxiv.org/abs/2605.25375) · [PDF](https://arxiv.org/pdf/2605.25375)

## 一句话摘要

The rapid evolution of large language models (LLMs) has made geographically distributed training necessary due to GPU scarcity within a single cloud region.

## 为什么值得关注

待编辑增强。

## 摘要原文

The rapid evolution of large language models (LLMs) has made geographically distributed training necessary due to GPU scarcity within a single cloud region. In such cross-region settings, Pipeline Parallelism (PP) is communication-efficient, yet scheduling PP remains challenging under heterogeneous inter-region bandwidth and regional electricity prices. Existing schedulers are either delay-first, incurring high electricity cost, or cost-first, relying on rigid resource allocation that prolongs Job Completion Time (JCT). They are also ineffective at optimizing execution order in multi-tenant environments, where long-running and bandwidth-intensive jobs can cause head-of-line (HoL) blocking and degrade overall performance. To this end, we propose BACE-Pipe, a bandwidth-aware and cost-efficient pipeline scheduling framework for LLM training across geo-distributed clusters. BACE-Pipe first introduces a dynamic job prioritization mechanism that optimizes execution order by jointly considering job characteristics (e.g., computation time) and real-time network utilization. It then employs a bandwidth-aware pathfinder to identify feasible cross-region pipeline paths that satisfy communication constraints, thereby preventing communication from stalling the pipeline. Among all feasible paths, a cost-minimizing allocator determines the optimal GPU placement strategy by preferentially assigning resources to regions with lower electricity prices. Consequently, BACE-Pipe mitigates HoL blocking, improves resource utilization, and simultaneously reduces both JCT and total electricity cost. Extensive simulations show that BACE-Pipe reduces average JCT by 27.9%--64.7% and total electricity cost by 12.6%--30.6% compared with state-of-the-art baselines.

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

- taxonomy keywords: pipeline parallel
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Han Zhang, Jianchun Liu, Hongli Xu
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
