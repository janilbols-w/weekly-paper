---
title: "Workload-Static Optical Circuit Switching For Scalable LLM Inference Decode"
description: "LLM inference decode executes fine-grained collectives whose latency directly limits per-user interactivity, yet scale-up fabrics are still built from electronic packet switches designed for training."
---

**评分：40/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2611.05104) · [PDF](https://arxiv.org/pdf/2611.05104)

## 一句话摘要

LLM inference decode executes fine-grained collectives whose latency directly limits per-user interactivity, yet scale-up fabrics are still built from electronic packet switches designed for training.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM inference decode executes fine-grained collectives whose latency directly limits per-user interactivity, yet scale-up fabrics are still built from electronic packet switches designed for training. We observe that, for a given model deployment and parallelization, the communication structure of decode is fixed, and propose workload-static optical circuit switching (OCS): circuits are configured once per deployment, co-designed with model parallelism and with topology-aware collective schedules that turn spare accelerator ports into fewer communication phases or higher bandwidth. We evaluate this design with GXNET, a graph-based workload emulator coupled to analytical and flit-level network models grounded in hardware measurements. In a 576-accelerator scale-up domain serving 5T-parameter MoE models with up to 5M tokens of context, all-OCS fabrics improve interactivity by up to 65% and energy efficiency by up to 119% over 4:1 oversubscribed packet-switched fabrics.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Maximilian Th\"urmer, Nicolas Scotto di Perto, Eloise Stein, Natanijel Vasic, Mikaeil Bagherli, Zhenguo Wu, Benjamin Klenk, Holger Fr\"oning, Johannes Feldmann
- 发布：2026-11-04；更新：2026-11-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
