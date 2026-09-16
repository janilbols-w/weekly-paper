---
title: "DeepShare: Assurance-Driven Deep Learning Job Scheduling for Multi-Tenant Clusters"
description: "Multi-tenant GPU clusters frequently remain underutilized even when tenants experience long queueing delays, because quota control, queue ordering, preemption, and GPU sharing are driven by different local signals."
---

**评分：44/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2609.16682) · [PDF](https://arxiv.org/pdf/2609.16682)

## 一句话摘要

Multi-tenant GPU clusters frequently remain underutilized even when tenants experience long queueing delays, because quota control, queue ordering, preemption, and GPU sharing are driven by different local signals.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multi-tenant GPU clusters frequently remain underutilized even when tenants experience long queueing delays, because quota control, queue ordering, preemption, and GPU sharing are driven by different local signals. We present DeepShare, a scheduler that uses a continuous tenant-assurance signal to coordinate these decisions at runtime. DeepShare combines elastic quota borrowing, tenant-specific runtime prediction, cost-aware best-effort preemption, and interference-aware MPS colocation, while using the same assurance signal to decide when borrowed capacity should be reclaimed and when sharing should become more conservative. In trace-driven experiments on 23,859 Venus jobs and 3,200 internal jobs, DeepShare achieves an average GPU utilization of 70.58%, a 29.5% improvement over the strongest non-intrusive sharing baseline, while reducing average queueing delay by 46%. On a 16-GPU Kubernetes testbed, it reduces the average job completion time by 34% and maintains 93% QoS compliance for guaranteed tenants. These results show that treating tenant assurance as a runtime control loop achieves a more advantageous utilization-QoS trade-off than optimizing quotas, scheduling, and resource sharing independently.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: multi-tenant
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jinghao Wang, Yihang Zhou, Xiao Zhou, Xinlei Zheng, Xiaoyang Sun, Tianyu Wo, Chunming Hu, Renyu Yang
- 发布：2026-09-16；更新：2026-09-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
