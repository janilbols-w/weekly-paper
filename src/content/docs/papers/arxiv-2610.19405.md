---
title: "Scaling LLM Inference via Parallelism: Throughput-Latency Trade-off"
description: "Large Language Model (LLM) serving systems must balance latency and throughput while efficiently utilizing distributed GPU resources."
---

**评分：42/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2610.19405) · [PDF](https://arxiv.org/pdf/2610.19405)

## 一句话摘要

Large Language Model (LLM) serving systems must balance latency and throughput while efficiently utilizing distributed GPU resources.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Model (LLM) serving systems must balance latency and throughput while efficiently utilizing distributed GPU resources. This challenge arises because inference consists of two fundamentally different phases: prefill, which determines time-to-first-token (TTFT), and decode, which determines inter-token latency (ITL). The use of tensor parallelism (TP), pipeline parallelism (PP), and hybrid configurations exposes different trade-offs between these latency dimensions, making the optimal parallelism configuration highly dependent on workload characteristics, latency requirements, and context length. Moreover, despite the widespread adoption of distributed inference, there is still limited understanding of how parallelism configurations should be selected under varying workload conditions and service-level objectives (SLO). In this paper, we develop a systematic framework for characterizing LLM inference parallelism via throughput-latency trade-offs, SLO-aware serving, and long-context scalability. We introduce the notion of parallelism operating regions by constructing TTFT-ITL feasible sets and Pareto frontiers across different workload compositions, thereby revealing a systematic transition from TP-dominant to PP-dominant configurations as workloads become increasingly prefill-heavy. We further formulate SLO-aware parallelism selection using goodput, showing that stringent TTFT requirements favor PP-dominated configurations, whereas relaxed latency constraints progressively shift the optimality toward TP-dominated configurations with higher serving capacity. Finally, we demonstrate that increasing context length fundamentally changes the relative advantages of parallelism configurations, with PP-dominant configurations exhibiting more favorable scalability and SLO attainment in the long-context regime.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: slo
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Javad Mirzaei, Jeebak Mitra
- 发布：2026-10-14；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
