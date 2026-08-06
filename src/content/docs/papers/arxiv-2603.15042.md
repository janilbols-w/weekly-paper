---
title: "Determinism-Preserving GPU Spatial Sharing with Vitamin-E"
description: "GPU sharing faces a determinism--utilization tradeoff: fixed bindings can strand capacity as demand fluctuates, while resource-driven kernel reshaping improves utilization by altering a launch's parallel structure, potentially changing output bits."
---

**评分：45/100** · AI 基础设施 > 集群与资源系统 > GPU 调度与虚拟化

[论文原文](https://arxiv.org/abs/2603.15042) · [PDF](https://arxiv.org/pdf/2603.15042)

## 一句话摘要

GPU sharing faces a determinism--utilization tradeoff: fixed bindings can strand capacity as demand fluctuates, while resource-driven kernel reshaping improves utilization by altering a launch's parallel structure, potentially changing output bits.

## 为什么值得关注

待编辑增强。

## 摘要原文

GPU sharing faces a determinism--utilization tradeoff: fixed bindings can strand capacity as demand fluctuates, while resource-driven kernel reshaping improves utilization by altering a launch's parallel structure, potentially changing output bits. We rethink modern GPU scheduling and observe that it decouples logical structure from physical width: one unmodified launch spans a family of widths through changes in block placement and wave count. From this observation, we derive the parallel-structure invariant: for fixed-structure deterministic workloads, keeping each launch immutable makes its output bits independent of physical width. Guided by this invariant, Vitamin-E late-binds immutable launches to pooled physical contexts, preserving bitwise equality across allocations, whereas resource-driven reshaping can alter the selected token under temperature-zero greedy decoding. Across all workload--baseline comparisons, Vitamin-E achieves up to 3.50$\times$ the aggregate normalized LLM training throughput, 62.5\% lower inference p99 latency, and 1.43$\times$ the background-training throughput. With the same mechanism, \textsc{TPOT-First} reduces TPOT SLO violations by up to 46.1\% over \textsc{Throughput-Oriented} on three serving workloads, demonstrating mechanism effectiveness and policy flexibility.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu scheduling, gpu sharing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhenyuan Yang, Wenxin Zheng, Mingyu Li, Haibo Chen
- 发布：2026-08-06；更新：2026-08-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
