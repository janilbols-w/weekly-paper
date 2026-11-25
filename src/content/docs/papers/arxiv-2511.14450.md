---
title: "Hyperion: Hierarchical Scheduling for Parallel LLM Acceleration in Multi-tier Networks"
description: "LLMs are increasingly executed at the edge, where limited GPU memory and heterogeneous computation jointly constrain deployment, which motivates model partitioning and request scheduling."
---

**评分：43/100** · LLM 高效推理 > Serving 与分布式推理 > Batching 与请求调度

[论文原文](https://arxiv.org/abs/2511.14450) · [PDF](https://arxiv.org/pdf/2511.14450)

## 一句话摘要

LLMs are increasingly executed at the edge, where limited GPU memory and heterogeneous computation jointly constrain deployment, which motivates model partitioning and request scheduling.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLMs are increasingly executed at the edge, where limited GPU memory and heterogeneous computation jointly constrain deployment, which motivates model partitioning and request scheduling. In this setting, minimizing latency requires addressing the tight coupling between model placement and request scheduling across heterogeneous nodes, as suboptimal decisions in one domain can negate benefits in the other. In this paper, we propose Hyperion, a hierarchical two-stage framework that coordinates partitioning and scheduling for pipelined LLM inference. Hyperion reduces latency by balancing resources across tiers without requiring model retraining. Leveraging the timescale difference between partitioning and request arrivals, Stage 1 performs offline, inter-tier partitioning via a Hyperion Split with Dynamic Programming (HypSplit-DP) procedure to produce balanced stage times under tier capacity and memory constraints; to adapt to time-varying load, Stage 2 performs online, intra-tier scheduling with a lightweight Hyperion Scheduling for Real-Time (HypSched-RT) that maps each request to a feasible node using real-time estimates of queue length and effective capacity. Experiments with Llama 3 and Phi-3 demonstrate that Hyperion reduces latency by up to 46.9% (vs. GPipe) and 31.1% (vs. HEFT). Furthermore, Hyperion exhibits superior scalability for long-sequence generation, maintaining 25.5% lower latency and higher GPU utilization.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: request scheduling
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mulei Ma, Xinyi Xu, Minrui Xu, Zihan Chen, Yang Yang, Tony Q. S. Quek
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
