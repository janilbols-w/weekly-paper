---
title: "OrigaMIG: MIG-Aware VM Placement with a Neighborhood-Restricted BILP and Live Migration"
description: "The extensive use of GPUs in cloud computing, accelerated by the spread of large language model (LLM) services, and the growing need for multitenancy have driven the development of innovative solutions for efficient GPU resource management."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.06646) · [PDF](https://arxiv.org/pdf/2610.06646)

## 一句话摘要

The extensive use of GPUs in cloud computing, accelerated by the spread of large language model (LLM) services, and the growing need for multitenancy have driven the development of innovative solutions for efficient GPU resource management.

## 为什么值得关注

待编辑增强。

## 摘要原文

The extensive use of GPUs in cloud computing, accelerated by the spread of large language model (LLM) services, and the growing need for multitenancy have driven the development of innovative solutions for efficient GPU resource management. Multi-Instance GPU (MIG) technology from NVIDIA enables shared GPU usage in cloud data centers by providing isolated instances, which are offered as MIG-backed virtual GPUs (vGPUs). However, MIG placement rules often lead to fragmentation and suboptimal resource allocation. In this work, we formally model the MIG-aware virtual machine (VM) placement as a binary integer linear programming (BILP) problem aimed at maximizing request acceptance, consolidating resources, and reducing migration overhead. Building upon this formulation, we propose OrigaMIG, a MIG-aware placement optimizer. OrigaMIG places each arriving request at once with a lightweight greedy rule and calls the solver only when a request cannot be placed or the GPUs of a class become fragmented. Each call solves the BILP on a small neighborhood of physical machines (PMs), keeps the rest of the data center fixed, and executes the solution as live migrations. We compare OrigaMIG with the default placement and with two state-of-the-art MIG-aware policies in simulation, across six loads, eleven variants of the workload and the hardware, and data centers of up to 4096 PMs. On 256 A100 and A30 GPUs in 128 PMs, OrigaMIG keeps fewer PMs active than the stronger policy in 29 of 30 paired runs while migrating 29% to 49% fewer VMs, and it uses the least energy per admitted GPU-hour at every load. Against the default placement, it keeps up to 12.5% fewer PMs active and admits up to 7.8 percentage points more of the requested GPU memory. On small data centers, it stays within 4.1% of the optimal number of active PMs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ahmad Siavashi, Mahmoud Momtazpour
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
