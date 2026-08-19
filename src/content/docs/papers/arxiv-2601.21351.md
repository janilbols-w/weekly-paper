---
title: "Analytical Provisioning for Attention-FFN Disaggregated LLM Serving under Stochastic Workloads"
description: "Attentio-FFN disaggregation (AFD) is an emerging architecture for LLM decoding that separates state-heavy, KV-cache-dominated Attention computation from stateless, compute-intensive FFN computation, connected by per-step communication."
---

**评分：42/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2601.21351) · [PDF](https://arxiv.org/pdf/2601.21351)

## 一句话摘要

Attentio-FFN disaggregation (AFD) is an emerging architecture for LLM decoding that separates state-heavy, KV-cache-dominated Attention computation from stateless, compute-intensive FFN computation, connected by per-step communication.

## 为什么值得关注

待编辑增强。

## 摘要原文

Attentio-FFN disaggregation (AFD) is an emerging architecture for LLM decoding that separates state-heavy, KV-cache-dominated Attention computation from stateless, compute-intensive FFN computation, connected by per-step communication. While AFD enables independent scaling of memory and compute resources, its performance is highly sensitive to the Attention/FFN provisioning ratio: mis-sizing induces step-level blocking and costly device idle time. We develop an analytical provisioning framework for AFD bundles in an $r$A--$1$F topology under stochastic workloads. Two sources of randomness shape the problem: per-slot Attention workload evolves as KV caches grow and completed requests are replenished with random prompt and decode lengths, and synchronized execution across Attention workers introduces a barrier governed by the slowest worker. We address both via a renewal-reward characterization of the per-slot stationary token load, identifying a single workload statistic $\theta$ that governs provisioning under arbitrary prefill-decode distributions and admits a nonparametric estimator from request traces. The analysis yields a closed-form mean-field rule for the optimal A/F ratio decomposing into Attention-, communication-, and FFN-bottleneck regimes, together with a Gaussian barrier-aware refinement that quantifies cross-worker synchronization overhead. A trace-calibrated AFD simulator supports the framework across workloads: the predicted optimal ratio matches the simulation-optimal within 10%. Together, these results provide a compact, calibratable account of how stochastic workload structure determines provisioning in disaggregated LLM serving.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chendong Song, Meixuan Wang, Hang Zhou, Hong Liang, Yuan Lyu, Zixi Chen, Yuwei Fan, Zijie Zhou
- 发布：2026-08-18；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
