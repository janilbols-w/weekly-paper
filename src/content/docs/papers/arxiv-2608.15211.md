---
title: "TERRA: A Hierarchical Parallel Training and Memory Orchestration Framework for High-Resolution AI-based Earth Modeling"
description: "Training high-resolution AI-based Earth forecasting models is memory-intensive."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2608.15211) · [PDF](https://arxiv.org/pdf/2608.15211)

## 一句话摘要

Training high-resolution AI-based Earth forecasting models is memory-intensive.

## 为什么值得关注

待编辑增强。

## 摘要原文

Training high-resolution AI-based Earth forecasting models is memory-intensive. Window-based Swin Transformers reduce the quadratic cost of global attention, but existing distributed systems such as AERIS primarily target pixel-level models and do not jointly support convolutional sampling modules and shifted-window execution. Long-lead rollout finetuning further increases activation memory. To address these challenges, we present TERRA, a hierarchical parallel training framework for high-resolution Earth forecasting. TERRA introduces Sampling-Aware Window, Sequence, and Tensor Parallelism (SAWSTP), which preserves spatially contiguous layouts for sampling modules and routes tokens into topology-aware ragged window layouts for Transformer execution. For long-lead finetuning, Memory Orchestration (MO) provides rollout-aware checkpoint planning and combines input buffering with budget-constrained activation offloading. Experiments on the $1/12^\circ$ GLORYS-based Wenhai workload show that TERRA supports models with up to 11.4B parameters on 96 H200 GPUs and sustains up to $39.76$ PFLOPS, achieving $65.0\%$ strong-scaling and $94.1\%$ weak-scaling efficiency. Compared with checkpoint-only policies, MO further reduces peak allocated GPU memory by $32.2\%$--$51.8\%$ with at most $20.0\%$ step-time overhead, which makes finetuning with smaller patch sizes and longer rollouts feasible for improved forecasting accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory, offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ruohan Wu, Ziqi Zhu, Yang Zhao, Jiarui Tang, Yingzhe Cui, Junshi Chen, Zhao Jing, Jun Shi, Hong An
- 发布：2026-08-18；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
