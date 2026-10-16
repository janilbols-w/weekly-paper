---
title: "Quota-Based Aging for Prediction-Guided Scheduling in LLM Serving"
description: "Large language model (LLM) serving systems use token-level continuous batching to improve resource utilization, but heterogeneous response lengths complicate request scheduling."
---

**评分：50/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](http://arxiv.org/abs/2610.17795v1) · [PDF](https://arxiv.org/pdf/2610.17795v1)

## 一句话摘要

Large language model (LLM) serving systems use token-level continuous batching to improve resource utilization, but heterogeneous response lengths complicate request scheduling.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) serving systems use token-level continuous batching to improve resource utilization, but heterogeneous response lengths complicate request scheduling. Prediction-guided short-first scheduling reduces average latency but can severely delay long requests, while unrestricted aging may over-promote delayed long requests under congestion. We propose Quota-Based Aging (QBA), a lightweight policy that combines predicted short-first admission with quota-bounded, debt-enforced promotion of aged predicted-long requests. We also use a reduced M/G/n queueing surrogate, calibrated from simulator traces, to explain first-order mean-latency trends. QBA is evaluated using a serving-aware event-driven simulator that models decode-priority batching, chunked prefill, token-budget constraints, and KV-cache-safe admission. We compare QBA with FCFS, predicted short-first, and aggressive aging under asymmetric prediction errors on synthetic and production-derived workloads. The evaluation considers queueing delay, throughput, utilization, and class-conditional tail performance. Results show that QBA provides a controllable middle ground between aggressive short-first prioritization and unrestricted aging, substantially reducing long-request tail latency while retaining much of the mean-latency benefit of prediction-guided scheduling.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hanzhi Zhang, Anxuan Che, Hang Qi, Qiyue Li, Jingjin Wu
- 发布：2026-10-13；更新：2026-10-13
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
