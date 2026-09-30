---
title: "AgentWare: Automating the Lifecycle of Agentic Applications across the Edge-to-Cloud Continuum"
description: "Deploying LLM-enabled agentic applications across the Edge-to-Cloud continuum remains challenging due to hardware heterogeneity, deployment complexity, limited observability, and the lack of systematic evaluation methods."
---

**评分：43/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2609.34586) · [PDF](https://arxiv.org/pdf/2609.34586)

## 一句话摘要

Deploying LLM-enabled agentic applications across the Edge-to-Cloud continuum remains challenging due to hardware heterogeneity, deployment complexity, limited observability, and the lack of systematic evaluation methods.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deploying LLM-enabled agentic applications across the Edge-to-Cloud continuum remains challenging due to hardware heterogeneity, deployment complexity, limited observability, and the lack of systematic evaluation methods. Existing solutions address agent development, observability, or benchmarking separately, offering limited support for the full lifecycle of distributed agentic applications. This paper presents AgentWare, an AgenticOps framework that automates the provisioning, deployment, observability, and evaluation of agentic applications across Edge-to-Cloud infrastructures. AgentWare introduces an end-to-end lifecycle pipeline that automatically prepares heterogeneous execution environments, transforms user-defined agent implementations into distributed applications, deploys agent components across the continuum, and performs unified collection of execution traces, infrastructure telemetry, and evaluation metrics. The framework further supports automated semantic evaluation through LLM-as-a-Judge workflows and generates reproducible reports covering correctness, performance, resource utilization, and energy consumption. We demonstrate the applicability of AgentWare through a distributed book assistant agent deployed across real Edge-to-Cloud infrastructure under multiple deployment and model configurations. The results show that AgentWare enables systematic experimentation and evaluation of distributed agentic applications while significantly reducing the manual effort required for deployment, instrumentation, and analysis.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: observability
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Michalis Kasioulis, Moysis Symeonides, George Pallis, Marios D. Dikaiakos
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
