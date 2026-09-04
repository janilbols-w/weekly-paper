---
title: "RASER: Resilient Agent Scheduling and Execution Runtime for HPC Clusters"
description: "The emergence of modern agents powered by large language models has created a demand for executing long-horizon, autonomous workflows in various domains that require significant computational resources."
---

**评分：40/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.03598) · [PDF](https://arxiv.org/pdf/2609.03598)

## 一句话摘要

The emergence of modern agents powered by large language models has created a demand for executing long-horizon, autonomous workflows in various domains that require significant computational resources.

## 为什么值得关注

待编辑增强。

## 摘要原文

The emergence of modern agents powered by large language models has created a demand for executing long-horizon, autonomous workflows in various domains that require significant computational resources. While High Performance Computing clusters provide the ideal infrastructure for these computation-intensive workloads, traditional HPC job schedulers such as Slurm are not designed for dynamic, agentic workflows characterized by unpredictable task durations, external API calls, and fault tolerance requirements of modern agents. This work presents RASER, a user-space framework that enables seamless execution of agentic workflows on production HPC clusters by extending Slurm's internal primitives. RASER introduces agentic job arrays with work stealing via shared filesystem queues, user-space checkpointing through application-level state serialization combined with Slurm requeue, and Apptainer container-based isolation without requiring any image modifications. Evaluations demonstrate that RASER reduces makespan by nearly 39% compared to static partitioning while achieving near-full CPU utilization. RASER provides resilience against preemption and failures while maintaining minimal checkpoint/restore overhead. It requires no kernel privileges or external database infrastructure, making it an accessible solution for deploying agentic workflows on existing HPC infrastructure.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint, checkpointing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sima Attar-Khorasani, Matthias Lieber, Siavash Ghiasvand
- 发布：2026-09-03；更新：2026-09-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
