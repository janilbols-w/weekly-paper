---
title: "GearUp: DAG-aware Acceleration for Serverless Inference Serving via Slack-guided Pre-loading"
description: "Serverless platforms increasingly host machine learning (ML) inference workflows, modeled as directed acyclic graphs (DAGs) of interdependent functions."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.38196) · [PDF](https://arxiv.org/pdf/2610.38196)

## 一句话摘要

Serverless platforms increasingly host machine learning (ML) inference workflows, modeled as directed acyclic graphs (DAGs) of interdependent functions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Serverless platforms increasingly host machine learning (ML) inference workflows, modeled as directed acyclic graphs (DAGs) of interdependent functions. Beyond container startup, each ML node must load libraries, model weights, and CUDA kernels before it can run. These costs accumulate along dependent DAG paths and place initialization on the end-to-end critical path. Existing systems optimize one half of this problem. DAG-agnostic pre-loading prepares nodes the request may never reach, wasting host and GPU memory. DAG-aware serving routes and scales whole functions, leaving the loading stages inside a node untouched. This paper presents GearUp, a serverless DAG inference serving system that removes ML-node loading from the end-to-end critical path at low resource cost. GearUp profiles the loading stages of each node and schedules them inside the slack time the DAG exposes, hiding initialization behind upstream execution. It reuses initialized instances within and across requests to avoid redundant cold starts. A probabilistic, traffic-adaptive keep-alive policy sets how long idle instances are retained, balancing memory cost against cold-start risk under bursty load. On the AMBER Alert and FINRA-ML workflows with NVIDIA L40S GPUs, GearUp reduces median end-to-end latency by 64.5% and 75.9% against SMIless, for median speedups of 3.1x and 10.0x over cold execution. Integrated GPU and host memory allocation fall by up to 83.9% and 94.6% against eager pre-loading in InstaInfer. GearUp achieves 4.2x strong scaling on four workers.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Qi Qi, Yifan Sui, Hanfei Yu, Hong Zhang, Hao Wang
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
