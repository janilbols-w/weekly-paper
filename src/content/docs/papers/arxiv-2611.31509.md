---
title: "TokenJoule: Energy Modeling for Distributed Training and Inference of LLMs"
description: "As large language models (LLMs) scale, energy dictates operating cost, cooling, and cluster capacity across training and inference."
---

**评分：44/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2611.31509) · [PDF](https://arxiv.org/pdf/2611.31509)

## 一句话摘要

As large language models (LLMs) scale, energy dictates operating cost, cooling, and cluster capacity across training and inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

As large language models (LLMs) scale, energy dictates operating cost, cooling, and cluster capacity across training and inference. Early hardware design-space exploration (DSE) requires predicting energy before silicon exists, yet performance models miss hidden component work while prior energy predictors calibrate to deployed GPUs. We present TokenJoule, an open-source analytical tool that derives device kernel sequences, tiled compute, shared-memory staging, cache residency, and collective traffic, pricing activity directly with component energies. With zero workload fitting, TokenJoule achieves 3.3-6.6% activity error (151 A100/H100 runs) and 3.0-6.8% A100 energy error, guiding parallelism, memory packaging, and 3D-DRAM chip co-design.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distributed training
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：George Karfakis, Lime Yao, Joyjit Kundu, Debjyoti Bhattacharjee, Puneet Gupta
- 发布：2026-11-23；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
