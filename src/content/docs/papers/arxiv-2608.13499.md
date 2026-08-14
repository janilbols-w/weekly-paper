---
title: "OpScale: Operator-level Provisioning and Autoscaling for LLM Serving"
description: "Achieving cost efficiency while meeting strict user-facing SLOs (e.g., time-to-first-token) remains a fundamental challenge for cloud GPU clusters serving large language models (LLMs)."
---

**评分：47/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2608.13499) · [PDF](https://arxiv.org/pdf/2608.13499)

## 一句话摘要

Achieving cost efficiency while meeting strict user-facing SLOs (e.g., time-to-first-token) remains a fundamental challenge for cloud GPU clusters serving large language models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Achieving cost efficiency while meeting strict user-facing SLOs (e.g., time-to-first-token) remains a fundamental challenge for cloud GPU clusters serving large language models (LLMs). Autoscaling is the key mechanism for cluster resource management, yet a basic system design question is open for serving LLMs: what should be the unit of scaling? Existing approaches primarily treat the entire model as a monolithic scaling unit--simple but unable to capture the fine-grained dynamics of inference workloads. As a result, such coarse-grained scaling often leads to either SLO violations under bursty demand or significant GPU under-utilization. Our characterization reveals substantial operator heterogeneity, exposing operator-level elasticity as a viable scaling primitive. We present OpScale, a practical operator-level orchestration framework of profiling, provisioning, placement, and runtime serving. OpScale is designed to tackle the high complexity and the space explosion problem, arising from operating at this finer granularity. Evaluated with production traces on up to 40 A100s and 24 GB200s, OpScale attains SLOs with up to 36.3% fewer GPUs and 28% less power, or achieves 44% higher throughput under fixed cost budgets.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: autoscaling
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xingqi Cui, Chieh-Jan Mike Liang, Ziang Tang, Jiarong Xing, Haoran Qiu
- 发布：2026-08-13；更新：2026-08-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
