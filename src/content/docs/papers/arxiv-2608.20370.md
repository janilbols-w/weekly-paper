---
title: "Benchmarking LLM Serving Systems for Agentic AI Workloads with XPerf"
description: "We present XPerf, a benchmarking framework that load-tests LLM serving systems with diverse agentic AI workloads."
---

**评分：40/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2608.20370) · [PDF](https://arxiv.org/pdf/2608.20370)

## 一句话摘要

We present XPerf, a benchmarking framework that load-tests LLM serving systems with diverse agentic AI workloads.

## 为什么值得关注

待编辑增强。

## 摘要原文

We present XPerf, a benchmarking framework that load-tests LLM serving systems with diverse agentic AI workloads. It provides detailed profiling of the serving system and hardware, enabling users to identify performance bottlenecks introduced by agentic workloads. Benchmarking LLM serving systems under agentic workloads is challenging - agentic applications rely on nondeterministic LLM outputs to guide their control flow; therefore, workload patterns vary unpredictably from run to run. XPerf minimizes this workload variation with a fine-grained trace replay approach: it enables users to easily collect traces from real agentic applications, synthesize new workloads with various patterns if needed, and reproducibly replay them on different LLM serving systems. XPerf includes eight agentic applications across diverse use cases (e.g., coding, deep research, and Q&A) by default. Our empirical study using these workloads shows that XPerf accurately replays agentic workloads, provides detailed performance breakdowns, scales to larger serving systems, and assists in serving system debugging. We will open-source XPerf on GitHub.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Michael Wang, Yikang Yue, Shaobo Li, Yirui Eric Zhou, Chen Wang, Jian Huang
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
