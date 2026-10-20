---
title: "AgentLens: Framework-Aware Characterization and Resource Control for Heterogeneous LLM Agents"
description: "LLM-based agents are increasingly deployed on shared hosts, yet their host-side resource demands remain poorly understood, limiting effective resource coordination."
---

**评分：41/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2610.25231) · [PDF](https://arxiv.org/pdf/2610.25231)

## 一句话摘要

LLM-based agents are increasingly deployed on shared hosts, yet their host-side resource demands remain poorly understood, limiting effective resource coordination.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM-based agents are increasingly deployed on shared hosts, yet their host-side resource demands remain poorly understood, limiting effective resource coordination. We present AgentLens, which combines a cross-framework workload characterization with a framework-aware resource controller for co-located agents. Across 10 frameworks and 11 matched coding tasks, we find that framework orchestration strongly shapes resource demand: framework identity explains 52.95% of peak RSS variance, compared with 4.22% for task identity, while execve events per tool call differ by 39x between MetaGPT and CAMEL. Resource dimensions are not interchangeable: peak RSS and subprocess count have a Spearman correlation of 0.13. Static budgets and framework-agnostic policies miss these structural differences and the alternation between API waiting and tool execution. AgentLens combines offline framework fingerprints with online execution-phase signals to coordinate memory through cgroup v2, without modifying framework internals. In trace-driven replay across three co-location pairs at a memory budget of 90% of aggregate peak demand, AgentLens keeps the protected worker's P95 allocation latency at 5.7-7.1 ms, improving on static allocation by 2.1-2.6x.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: workload characterization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Wentao Hong
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
