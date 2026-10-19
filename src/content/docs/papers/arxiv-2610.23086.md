---
title: "PairSight: Characterizing and Predicting Operator-Level Interference in GPU Sharing for DNN Inference"
description: "Serving DNN inference is costly, yet a single task seldom saturates both the compute units and the memory bandwidth of a GPU."
---

**评分：46/100** · AI 基础设施 > 集群与资源系统 > GPU 调度与虚拟化

[论文原文](https://arxiv.org/abs/2610.23086) · [PDF](https://arxiv.org/pdf/2610.23086)

## 一句话摘要

Serving DNN inference is costly, yet a single task seldom saturates both the compute units and the memory bandwidth of a GPU.

## 为什么值得关注

待编辑增强。

## 摘要原文

Serving DNN inference is costly, yet a single task seldom saturates both the compute units and the memory bandwidth of a GPU. GPU sharing raises utilization by co-locating several tasks on one GPU, at the cost of interference among them. Existing systems estimate this interference with binary compute-memory rules, standalone scaling curves, or model-level predictors. However, these estimates rest on a limited understanding of interference. They leave the software and hardware properties of co-located operators largely unexplored and give no slowdown prediction that is both interpretable and accurate. We conduct an operator-level study of interference under SM partitioning and use hardware counters to trace it to contention on the shared memory path, where the slowdown depends jointly on both co-located operators. Based on these findings, we propose PairSight, a hardware-aware interference predictor that learns how the hardware behaviors of co-located tasks interact and predicts the latency of each task before co-location. On six DNN models including LLMs, PairSight predicts latency under sharing with 4.3% mean error, against 19.0% for a compute-memory intensity rule, and adapts to unseen models and inputs with a few samples.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu sharing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xiao Liu, Yujia Fu, Yue Yu, Dan Huang
- 发布：2026-10-19；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
