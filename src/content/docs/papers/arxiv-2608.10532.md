---
title: "Benchmarking LLM-Guided Control-Plane Policies for Backend Fault Isolation in HAProxy"
description: "Static load balancers cannot mitigate a backend that is degraded rather than down: round-robin and least-connections keep routing traffic to a server returning HTTP 500s until an operator intervenes."
---

**评分：44/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2608.10532) · [PDF](https://arxiv.org/pdf/2608.10532)

## 一句话摘要

Static load balancers cannot mitigate a backend that is degraded rather than down: round-robin and least-connections keep routing traffic to a server returning HTTP 500s until an operator intervenes.

## 为什么值得关注

待编辑增强。

## 摘要原文

Static load balancers cannot mitigate a backend that is degraded rather than down: round-robin and least-connections keep routing traffic to a server returning HTTP 500s until an operator intervenes. We ask whether a Large Language Model can replace the static routing policy itself, reading HAProxy and Prometheus telemetry every 10 seconds and isolating faulty servers through guardrailed calls to the HAProxy Data Plane API. On a reproducible benchmark with a persistent structural fault built into roughly one-third of a heterogeneous fleet, we sweep 15 open-weight models across five families (0.35B to 35B total parameters; dense, mixture-of-experts, and efficient-sparse architectures), reasoning modes, fleet scales of 3 to 9 backends, and two routing algorithms, totaling 240 runs. We find a capability threshold near 3B active parameters. Below it, LLM policies are typically unreliable and sometimes worse than no policy; above it, every model, regardless of architecture, saturates near an 88% reduction in client-perceived 5xx errors over the static baseline. The threshold is approximate: Gemma 4 E2B clears it with 2B active parameters, while the dense 3B Granite 4.0 Micro does not. The availability gain has costs. Draining concentrates load onto surviving servers, inflating tail latency 2.6 to 2.8 times, and enabling reasoning multiplies token spend roughly tenfold, overrunning the control interval and degrading effectiveness. The efficient operating point is a supra-threshold model in its cheapest non-reasoning mode, wrapped inside deterministic guardrails.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: tail latency
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Aman Chauhan, Vishnu Pendyala
- 发布：2026-08-11；更新：2026-08-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
