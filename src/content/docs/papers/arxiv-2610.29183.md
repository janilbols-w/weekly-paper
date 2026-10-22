---
title: "Resuming Vision-Language Inference across Onboard Interruptions"
description: "Executing vision-language models (VLMs) aboard low-Earth orbit satellites enables flexible processing of observation data without first downlinking it to the ground."
---

**评分：45/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.29183) · [PDF](https://arxiv.org/pdf/2610.29183)

## 一句话摘要

Executing vision-language models (VLMs) aboard low-Earth orbit satellites enables flexible processing of observation data without first downlinking it to the ground.

## 为什么值得关注

待编辑增强。

## 摘要原文

Executing vision-language models (VLMs) aboard low-Earth orbit satellites enables flexible processing of observation data without first downlinking it to the ground. On commercial off-the-shelf payloads, however, a request may span multiple execution windows: power and thermal constraints, fault-triggered reboots, and competing payload demands can interrupt inference before it completes. Each shutdown discards volatile activations and KV caches, forcing an unprotected request to repeat work after restart. We present OrbitWeaver, a framework that preserves VLM inference progress across onboard interruptions through coordinated checkpointing and recovery. Its phase-aware checkpointing selects recovery boundaries according to the state lifetimes and computational characteristics of vision encoding, language-model prefill, and decoding, balancing storage traffic against recomputation. Its dependency-aware dynamic recovery schedules restoration from partially completed states across the layer and token-chunk dimensions. By overlapping checkpoint and weight reads with recomputation, it reduces restart latency; the recovery planner computes an optimal execution order under its scheduling model within 100 ms. Experiments on satellite payload hardware using on-orbit telemetry traces show up to a 4.07-fold end-to-end speedup and a 3.56-fold reduction in SSD write volume over the evaluated baselines. A 72-hour deployment on two low-Earth orbit satellites demonstrates that OrbitWeaver retains inference progress and resumes execution across repeated bus-enforced shutdowns.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint, checkpointing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xiaolong Huang, Yinyuan Zhang, Daliang Xu, Yun Ma, Qing Li, Mengwei Xu, Shangguang Wang, Gang Huang, Xuanzhe Liu
- 发布：2026-10-22；更新：2026-10-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
