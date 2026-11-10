---
title: "ISER-MoE: Dynamic In-Switch Replication of Hot Experts for Load Balancing in Expert-Parallel"
description: "Expert-parallel mixture-of-experts (MoE) layers run at the pace of the most loaded GPU, and a few hot experts carry most of the excess load."
---

**评分：44/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2611.09008) · [PDF](https://arxiv.org/pdf/2611.09008)

## 一句话摘要

Expert-parallel mixture-of-experts (MoE) layers run at the pace of the most loaded GPU, and a few hot experts carry most of the excess load.

## 为什么值得关注

待编辑增强。

## 摘要原文

Expert-parallel mixture-of-experts (MoE) layers run at the pace of the most loaded GPU, and a few hot experts carry most of the excess load. Replicating them at every MoE layer balances the load only if their weights arrive within the layer, and broadcasting from the owner is the bottleneck: point-to-point copies overload it, and baseline broadcasts pay latency or bandwidth overheads. We present ISER-MoE (In-Switch Expert Replication for MoE), built in TensorRT-LLM, which multicasts hot experts through the NVLink switch to fixed GPU groups, so each byte leaves its owner once. A GPU scheduler assigns hot experts to groups per layer, and a multi-port broadcast spreads the injection over the group's ports, both overlapped with the shared expert. In trace replay, the scheduler removed 98-99% of the excess load; in prefill serving of DeepSeek-V4-Pro, throughput rose 17.4% on a math benchmark and 7.2% on agentic prompts.

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

- taxonomy keywords: load balancing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jintao Peng, Ethan Zhang, Kefeng Duan, Bangyu Sheng, Min Li, Itamar Rosenfeld Rauch, Jack Yang, June Yang
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
