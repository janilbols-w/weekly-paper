---
title: "What Does an Observability Foundation Model Know?"
description: "A linear probe can show that a label is recoverable from a model's hidden states, but not whether that goes beyond what the input already reveals, or whether the model uses it."
---

**评分：40/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2610.05577) · [PDF](https://arxiv.org/pdf/2610.05577)

## 一句话摘要

A linear probe can show that a label is recoverable from a model's hidden states, but not whether that goes beyond what the input already reveals, or whether the model uses it.

## 为什么值得关注

待编辑增强。

## 摘要原文

A linear probe can show that a label is recoverable from a model's hidden states, but not whether that goes beyond what the input already reveals, or whether the model uses it. We audit Toto, an observability forecasting foundation model, on the Benchmark of Observability Metrics (BOOM) across five series-disjoint resplits, comparing linear probes on its frozen residual stream with models that read the raw input window and with Toto's architecture stripped of its trained configuration. Short-vs-medium cadence and metric type are more linearly recoverable from Toto's residuals than from the strongest raw-window model in every resplit (macro-F1 0.766 vs. 0.633 and 0.545 vs. 0.498). Domain is nearly tied, and series cardinality is recovered far better from the raw window. MOMENT-base shows related cadence, metric-type, and domain readouts. Recoverability is not use: exchanging Toto's residuals with those of high-burst donors moves a future-burstiness readout as intended but does not make forecasts consistently burstier than a randomized donor. A BOOM-trained coordination probe has negative zero-shot R^2 on the tested external benchmarks. We report each label against its strongest baseline.

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

- taxonomy keywords: observability
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dhyey Dharmendrakumar Mavani, Rian Atri, Tairan Ji
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
