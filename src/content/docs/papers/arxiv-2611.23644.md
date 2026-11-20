---
title: "Polymorph: Operating System Kernel Optimization Through Artificial Intelligence"
description: "While popular operating systems such as Linux and Windows were originally designed as monolithic kernels, an increasing number of kernel subsystems have become extensible using eBPF."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2611.23644) · [PDF](https://arxiv.org/pdf/2611.23644)

## 一句话摘要

While popular operating systems such as Linux and Windows were originally designed as monolithic kernels, an increasing number of kernel subsystems have become extensible using eBPF.

## 为什么值得关注

待编辑增强。

## 摘要原文

While popular operating systems such as Linux and Windows were originally designed as monolithic kernels, an increasing number of kernel subsystems have become extensible using eBPF. Users can now define custom policies for essential kernel mechanisms, such as the process scheduler, page cache, and network stack, without recompiling the kernel. These mechanisms give developers significant freedom to fit the kernel to their applications' workloads, but the question of which policy to deploy remains open. We study how to use agentic AI to automate kernel policy development, selection, and deployment, focusing on the page cache and the process scheduler as two representative subsystems. We show that existing approaches fall short: evolutionary and agentic search runs offline, is relatively expensive, and often fails to generalize to online workloads, while online knob tuners are encumbered by the knobs' lack of expressivity. In contrast, we propose Polymorph, which learns online: an AI agent writes a generalized, granular policy once, and a user mode tuner adjusts its parameters during runtime, with no LLM in the loop. For the page cache, Polymorph improves throughput over Linux's LRU by 8.4% on unseen data, nearly twice the gain of the best existing policy, while adapting to workload changes at runtime and costing only 16M tokens once, versus 125-240M tokens per workload for agentic offline search. For the process scheduler, it improves on Linux's default by 2.75x across six workloads, versus 2.27x for the best fixed sched_ext policy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kernel optimization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Dean Sysman, Georgios Liargkovas, Tal Zussman, Hasan Zengin, Petra Hedesiu, Hubertus Franke, Tamar Eilam, Kostis Kaffes, Asaf Cidon
- 发布：2026-11-18；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
