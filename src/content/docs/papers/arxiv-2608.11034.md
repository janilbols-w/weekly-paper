---
title: "SCOUT: Symmetric Consensus Outlier Detection for Failure Localization in LLM Pre-Training"
description: "In LLM pre-training, synchronization propagates rank-local stalls, slowdowns, and numerical errors into job-wide symptoms, obscuring their origin."
---

**评分：42/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2608.11034) · [PDF](https://arxiv.org/pdf/2608.11034)

## 一句话摘要

In LLM pre-training, synchronization propagates rank-local stalls, slowdowns, and numerical errors into job-wide symptoms, obscuring their origin.

## 为什么值得关注

待编辑增强。

## 摘要原文

In LLM pre-training, synchronization propagates rank-local stalls, slowdowns, and numerical errors into job-wide symptoms, obscuring their origin. Existing diagnosis often relies on in-process monitors that cannot report after the trainer blocks or terminates, or on post-mortem logs that preserve only synchronized symptoms; offline health tests lose the workload and operating conditions that triggered the failure. We present SCOUT, a unified runtime failure-localization framework built on one design principle: identify outliers through strict-majority consensus among equivalent replicas. SCOUT aligns replica progress, timing, and numerical evidence, then uses its Consensus Collective Communication (C3) abstraction to identify ranks whose compact signatures disagree with their peers. An out-of-band CPU observer remains responsive when training hangs, whereas in-situ replay exercises recurring stragglers and silent data corruption (SDC) beside the live job with its model state, kernels, allocations, communication path, and thermal and memory pressure present. Collective fingerprints expose rank-local protocol divergence. Clean replay coverage certifies checkpoint numerical integrity, preventing recovery from selecting state corrupted by SDC. SCOUT integrates with PyTorch, TorchTitan, Megatron-Core, and DeepSpeed without training-loop or framework-source modifications. SCOUT is open source at https://github.com/LMResiliency/lm-resiliency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zhuang Wang
- 发布：2026-08-12；更新：2026-08-12
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/LMResiliency/lm-resiliency](https://github.com/LMResiliency/lm-resiliency)
- 阅读深度：metadata
