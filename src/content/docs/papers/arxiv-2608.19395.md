---
title: "HYDRA: A Heterogeneous Chiplet DSE Framework for Serving Dynamic Hybrid LLM Workloads"
description: "Hybrid Transformer-Mamba large language models (LLMs) enhance long-context efficiency, but their heterogeneous computation and communication patterns complicate efficient hardware acceleration."
---

**评分：44/100** · LLM 高效推理 > Serving 与分布式推理 > Batching 与请求调度

[论文原文](https://arxiv.org/abs/2608.19395) · [PDF](https://arxiv.org/pdf/2608.19395)

## 一句话摘要

Hybrid Transformer-Mamba large language models (LLMs) enhance long-context efficiency, but their heterogeneous computation and communication patterns complicate efficient hardware acceleration.

## 为什么值得关注

待编辑增强。

## 摘要原文

Hybrid Transformer-Mamba large language models (LLMs) enhance long-context efficiency, but their heterogeneous computation and communication patterns complicate efficient hardware acceleration. Chiplet-based architectures offer a scalable solution by integrating specialized compute and memory units. However, the design space spanning static architectural configurations and dynamic runtime policies is prohibitively large to explore exhaustively. To address this challenge, we present HYDRA, a comprehensive design space exploration framework for hybrid LLM serving on heterogeneous chiplet systems. HYDRA jointly explores chiplet composition, placement, inter-chiplet bandwidth provisioning, dynamic batching, and runtime scheduling. It integrates communication-aware placement, dynamic batching, elastic task scheduling, and a fast Markov-based performance estimator that captures multi-tenant runtime dynamics for efficient and accurate exploration. Across all workloads, HYDRA delivers 1.55x the throughput and 43.7 percent lower time-to-first-token on average, with throughput gains reaching up to 2.3x compared to state-of-the-art baselines. These results highlight that co-designing architecture and runtime policies is critical for efficient large-scale LLM serving on heterogeneous chiplet systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: dynamic batching
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jiahao Lin, Alish Kanani, Sangwan Lee, Jaehyun Park, Umit Ogras
- 发布：2026-08-19；更新：2026-08-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
