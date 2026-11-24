---
title: "Mind the Delta: Early Pruning of RTL Variants for Agentic Hardware Optimization"
description: "Autonomous coding agents powered by large language models (LLMs) now write diverse microarchitectural variants of existing register-transfer level (RTL) designs at high throughput, shifting the primary bottleneck of agentic RTL optimization onto logic synthesis."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.27035) · [PDF](https://arxiv.org/pdf/2611.27035)

## 一句话摘要

Autonomous coding agents powered by large language models (LLMs) now write diverse microarchitectural variants of existing register-transfer level (RTL) designs at high throughput, shifting the primary bottleneck of agentic RTL optimization onto logic synthesis.

## 为什么值得关注

待编辑增强。

## 摘要原文

Autonomous coding agents powered by large language models (LLMs) now write diverse microarchitectural variants of existing register-transfer level (RTL) designs at high throughput, shifting the primary bottleneck of agentic RTL optimization onto logic synthesis. Commercial toolchains take hours per variant, creating an acute compute asymmetry between proposing and evaluating variants. Existing fast evaluators falter in this regime. Subtle RTL edits trigger nonlinear synthesis shifts that learned predictors and coding agents cannot resolve, while synthesis proxies at reduced effort either alter the optimization trajectory or retain most of its runtime. Selecting a variant, however, does not require regressing absolute quality of results across designs, only identifying when a candidate cannot surpass the best completed feasible implementation. Based on the observation that synthesis trajectories share strong design-specific bias with their base design, we propose DiffScope, a training-free anytime selection framework that races full synthesis runs in parallel. By pairing live area telemetry with the already synthesized base trajectory, DiffScope cancels early mapping inflation, reducing residual variance during initial mapping by 73.6X, and stops uncompetitive runs via a lower bound calibrated on other design lineages. Across 43 design families from small blocks to processors with millions of cells, DiffScope uniquely recovers the optimum of exhaustive synthesis in every family, cuts total evaluation work by 44.9% (1.81X), and reaches 2.18X on L-tier designs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Siyang Cai, Cangyuan Li, Haoyu Gao, Kun Wang, Mochen Li, Yilin Zhong, Ke Xu, Yinhe Han, Ying Wang
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
