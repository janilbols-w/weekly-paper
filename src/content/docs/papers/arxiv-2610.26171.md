---
title: "CEMA-Router: Infrastructure-Aware Batch Routing for LLM Inference in Cloud-Edge Systems"
description: "Large language models (LLM) are increasingly integrated into pervasive applications spanning heterogeneous cloud-edge resources."
---

**评分：41/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2610.26171) · [PDF](https://arxiv.org/pdf/2610.26171)

## 一句话摘要

Large language models (LLM) are increasingly integrated into pervasive applications spanning heterogeneous cloud-edge resources.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLM) are increasingly integrated into pervasive applications spanning heterogeneous cloud-edge resources. These heterogeneous resources differ in computational capacity, energy efficiency, network conditions, and deployed model quality, creating trade-offs among response quality, monetary cost, energy consumption, and batch completion time when routing inference requests. Existing LLM routers typically make per-query routing decisions based primarily on model quality and token cost, whereas cloud-edge schedulers often overlook quality differences among deployed models. Consequently, these objectives remain insufficiently coordinated. We present CEMA-Router, an infrastructure-aware batch router for LLM inference in pervasive cloud-edge systems. CEMA-Router formulates batch routing as a multi-objective search problem that jointly minimizes model-quality loss, monetary cost, energy consumption, and straggler-dominated batch completion time. To efficiently explore the search space, it employs a routing-specific memetic algorithm, combining largest-request-first, load-aware seeding with probabilistic, evaluator-guided Lamarckian repair. Routing decisions are informed by deployment-specific node profiles, dynamic backlog estimates, and model-quality signals. We further implement CEMA-Router as an end-to-end system comprising a request manager, routing service, and profiler, supporting both real cloud-edge deployment and trace-driven simulation. We evaluate the system using RouterBench traces and GSM8K and MMLU workloads on a heterogeneous cloud-edge testbed. Compared with state-of-the-art methods, CEMA-Router reduces the weighted objective by up to 86% for GSM8K and 80% for MMLU, while reducing energy consumption by up to 33% and 19% and batch completion time by up to 27% and 30%, respectively.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xijia Wang, TianZhang He, Mohammad Goudarzi
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
