---
title: "Execution-Feasible Dispatch of LLM Pre-training Loads for Renewable-Dominant AI Data Centers"
description: "AI data centers (AIDCs) are emerging as large power-system loads, making their operational flexibility increasingly valuable."
---

**评分：41/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.13047) · [PDF](https://arxiv.org/pdf/2610.13047)

## 一句话摘要

AI data centers (AIDCs) are emerging as large power-system loads, making their operational flexibility increasingly valuable.

## 为什么值得关注

待编辑增强。

## 摘要原文

AI data centers (AIDCs) are emerging as large power-system loads, making their operational flexibility increasingly valuable. Existing studies often treat AIDC demand as continuously adjustable or generically delay-tolerant, which overstating the flexibility of large language model (LLM) pretraining. This paper proposes an execution-feasible dispatch framework for LLM pre-training in renewable-dominant AIDCs. LLM descriptors are first converted into checkpoint-domain daily workloads, then mapped to feasible 3D-parallel GPU modes with explicit throughput, GPU-capacity, memory, and IT-power limits. The resulting checkpoint- and mode-constrained load states are embedded into a day-ahead power dispatch model. Case studies on a 2048 GPUs AIDC with two LLaMA pretraining tasks show that checkpoint-aware 3D dispatch reduces operating cost by 20.02% and renewable curtailment from 1.077 to 0.014 MWh relative to fixed continuous training. Related results also show that checkpoint records alone do not create load flexibility,practical grid-interactive flexibility arises from checkpoint waiting combined with execution-feasible 3D-mode compensation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xi Tong, Ershun Du, Haiyang Jiang, Long Chen, Qin Wang
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
