---
title: "A Year in LLM Serving: Workload Evolution, Caching and Load-Balancing"
description: "Large Language Model (LLM) serving has become a critical cloud workload, and realistic traces are essential for motivating and benchmarking serving systems."
---

**评分：45/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2608.13573) · [PDF](https://arxiv.org/pdf/2608.13573)

## 一句话摘要

Large Language Model (LLM) serving has become a critical cloud workload, and realistic traces are essential for motivating and benchmarking serving systems.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Model (LLM) serving has become a critical cloud workload, and realistic traces are essential for motivating and benchmarking serving systems. However, existing LLM serving workload studies remain limited in scale and scope. They often observe short time periods and provide limited visibility into how users interact with models in production. As a result, they do not fully capture how LLM serving workloads evolve over time or how user-model interactions shape production traffic. In this work, we further the understanding of real-world LLM serving workloads through both a global characterization and a longitudinal study of a one-year production trace from CompanyX. Unlike prior studies, our trace captures full production behavior across many models and users, including both popular and long-tail models. We analyze the workload from aggregate, temporal, model-level, and user-level perspectives, revealing workload evolution and user-model structure that are typically hidden behind aggregate views. To support future research, we publicly release the full one-year trace, enabling downstream studies of production behavior without relying on sampled or synthetically generated workloads. The trace is available at https://github.com/HarvardMadSys/chutes_workload.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：William Nixon, Jon Durbin, Florian Standhartinger, Haryadi S. Gunawi, Juncheng Yang
- 发布：2026-11-04；更新：2026-11-04
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/HarvardMadSys/chutes_workload](https://github.com/HarvardMadSys/chutes_workload)
- 阅读深度：metadata
