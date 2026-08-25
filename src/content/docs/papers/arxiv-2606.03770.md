---
title: "E2LLM: Towards Efficient LLM Serving in Heterogeneous Edge/Fog Environments"
description: "Large Language Models (LLMs) have become integral to modern applications, yet their deployment remains challenging."
---

**评分：49/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2606.03770) · [PDF](https://arxiv.org/pdf/2606.03770)

## 一句话摘要

Large Language Models (LLMs) have become integral to modern applications, yet their deployment remains challenging.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) have become integral to modern applications, yet their deployment remains challenging. Beyond executing the models themselves, practical deployment must address cost efficiency, low latency, and optimal resource utilization. Conventional approaches typically assume that an entire model can be hosted on a single device, which does not hold in many real-world scenarios, particularly in Edge and Fog environments where device resources are constrained. In this paper, we introduce E2LLM, a framework designed to enable efficient LLM deployment in such resource limited settings. Rather than simply partitioning a single model across all available devices, E2LLM replicates the full model across multiple groups of devices (replicas) and applies model parallelism within each replica. Each replica is assigned a specialized role PREFILL or DECODER based on its efficiency in handling input and output tokens. This separation leverages the inherent differences between these two phases of LLM inference. To effectively organize devices, we utilize a Genetic Algorithm to form clusters that maximize system performance. Within each cluster, we apply Dynamic Programming to determine an optimal partitioning strategy that minimizes bottlenecks in model-parallel execution. Experimental results demonstrate that our approach adapts robustly to varying workloads, including scenarios with significant variation in input and output token lengths. Compared to the Splitwise baseline, E2LLM reduces average waiting time by over 50% under high-demand conditions

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Truong-Thanh Le, Amir Taherkordi, Hoang-Loc La, Frank Eliassen, Phuong Hoai Ha, Peiyuan Guan
- 发布：2026-08-18；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
