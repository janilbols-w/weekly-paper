---
title: "JointServe: Serving Multi-Model Agents on Memory-Constrained GPUs"
description: "LLM agents are evolving from a single model calling tools to planners that orchestrate multiple expert models whose capabilities live in distinct weights."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.19822) · [PDF](https://arxiv.org/pdf/2610.19822)

## 一句话摘要

LLM agents are evolving from a single model calling tools to planners that orchestrate multiple expert models whose capabilities live in distinct weights.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM agents are evolving from a single model calling tools to planners that orchestrate multiple expert models whose capabilities live in distinct weights. This shift breaks a hidden assumption of today's serving systems: that the working set of models fits in GPU memory. On the memory-constrained GPUs typical of private and edge deployments, naive whole-model swapping serializes weight transfer with computation and, without host-backed KV restoration, discards session state at a switch. We present JointServe, a serving system that treats weight shards and KV blocks as residency objects competing for one unified memory budget. JointServe exploits three structural properties of agent workloads (directed calls, gapped execution, and dual-state residency) to prepare models before they are called: an intent signal parsed from the caller's own output stream triggers prefetch during generation, partial k* residency reduces switching to incremental layers, and a preemptive transfer scheduler protects live-session KV with a guaranteed bandwidth share. A carve-out control step adjusts the weight/KV allocation as workload demands change. Evaluations show that JointServe reduces session completion time by 21.7% over the strongest whole-model swap baseline and stays usable in a crash regime where every whole-model swap baseline fails to finish (a 46-fold gap). On replayed SWE-bench, tau-bench, and OSWorld traces, it cuts session completion time by up to 49% and lifts SLO attainment from 2.8-24.5% to 76.8-100%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory, unified memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Daijin Hu
- 发布：2026-10-15；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
