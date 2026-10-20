---
title: "ATEST: Adaptive Resource-Aware Test-Time Scaling for LLM Inference"
description: "Test-time scaling (TTS) improves large language model (LLM) reasoning by sampling multiple answers, but fixed sampling budgets ignore both query difficulty and the changing energy cost of inference under GPU contention."
---

**评分：51/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2610.25519) · [PDF](https://arxiv.org/pdf/2610.25519)

## 一句话摘要

Test-time scaling (TTS) improves large language model (LLM) reasoning by sampling multiple answers, but fixed sampling budgets ignore both query difficulty and the changing energy cost of inference under GPU contention.

## 为什么值得关注

待编辑增强。

## 摘要原文

Test-time scaling (TTS) improves large language model (LLM) reasoning by sampling multiple answers, but fixed sampling budgets ignore both query difficulty and the changing energy cost of inference under GPU contention. We measure up to a 4.1-fold increase in energy for the same four-sample query as GPU load rises. We present ATEST, a resource-aware TTS framework that jointly considers the expected value of additional samples and their current GPU cost. ATEST-Online, its default mode, requires no offline calibration: it incrementally generates samples, estimates the stability of the plurality answer, monitors live GPU conditions, and learns step energy cost online to decide when to stop. ATEST-Calibrated instead selects a per-query budget using offline accuracy and cost models, favoring deployments with stable loads. We evaluate both modes on four reasoning and question-answering datasets using Phi-3-mini on an NVIDIA A100 under controlled varying load, and test transfer to an NVIDIA L40S and Qwen2.5-3B. Across the four A100 datasets, ATEST-Online answers every query without exceeding the energy budget, while achieving the highest or statistically tied accuracy and reducing sampling as load increases. On GSM8K at high load, it achieves 60.0% accuracy with no deferrals, versus 44.0% accuracy and 42.4% deferrals for ATEST-Calibrated. Ablations show that online cost learning drives adaptation to load. Including offline profiling, ATEST-Online uses 42 times less GPU time and 48 times less energy than ATEST-Calibrated for the evaluated workload. Online control trades higher tail latency and lower throughput on short tasks for robustness under varying load; offline calibration remains competitive under stable conditions.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: tail latency
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Mobina Kashaniyan, Ali Jannesari
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
