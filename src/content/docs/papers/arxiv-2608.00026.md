---
title: "Request-Level Energy Attribution for Batched LLM Serving"
description: "Batched LLM serving improves throughput but complicates energy accounting."
---

**评分：49/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2608.00026) · [PDF](https://arxiv.org/pdf/2608.00026)

## 一句话摘要

Batched LLM serving improves throughput but complicates energy accounting.

## 为什么值得关注

待编辑增强。

## 摘要原文

Batched LLM serving improves throughput but complicates energy accounting. GPU power telemetry is aggregate, whereas sustainability reporting, chargeback, and workload analysis often require request-level energy charges. Existing inference-energy benchmarks report model-, phase-, or token-level energy, and recent carbon-accounting work motivates Shapley fairness conceptually. Neither provides measured request-level ground truth, so how far the accounting rules used in practice deviate from a fair allocation has remained unknown. We present JouleShare, an attribution framework with two components. An offline harness establishes this ground truth by replaying request subsets under vLLM with a reproducible protocol, integrating GPU power telemetry, and computing exact Shapley energy for each request. A lightweight calibration model, JCalib, then learns to predict Shapley shares from cheap request features for use at serving time. Across 16 model/workload runs, token-proportional attribution differs from exact Shapley by 0.440 normalized L1 on average under static batching and by 0.458 under continuous batching, a gap that reproduces across three data-center GPUs. JCalib reduces this error to 0.116 under static batching and 0.177 under continuous batching, below even a standalone-measurement baseline that is unavailable online, while preserving exact batch-energy efficiency. Sampled Shapley extends the measured reference to larger group sizes, where the gap persists and a single offline calibration remains the most accurate deployable rule. The results show that token attribution is not a reliable proxy for marginal energy under batched execution, and that measured Shapley ground truth can calibrate low-cost request features toward fairer attribution.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qi Luo, Kunlin Li, Ziwen Wang, Dongsheng Wang, Yun Chen
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
