---
title: "TokenPowerSandbox: Evidence-Gated CPU-First Screening for Energy-Aware LLM Serving"
description: "Energy-aware LLM serving requires comparing configurations under realistic request shapes, yet exhaustive target-GPU profiling is costly and a cheap predictor can be dangerously confident outside its measured scope."
---

**评分：47/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2608.18149) · [PDF](https://arxiv.org/pdf/2608.18149)

## 一句话摘要

Energy-aware LLM serving requires comparing configurations under realistic request shapes, yet exhaustive target-GPU profiling is costly and a cheap predictor can be dangerously confident outside its measured scope.

## 为什么值得关注

待编辑增强。

## 摘要原文

Energy-aware LLM serving requires comparing configurations under realistic request shapes, yet exhaustive target-GPU profiling is costly and a cheap predictor can be dangerously confident outside its measured scope. We present TokenPowerSandbox, an evidence-gated workflow that combines an interpretable CPU-resident projector, short target-GPU probes, full-workload verification, and tamper-evident freeze-before-measurement provenance. On one NVIDIA H100 80GB serving Qwen2.5-7B-Instruct with vLLM, three anchor repeats and six development workloads calibrate workload transfer. The same frozen model is evaluated on a blind holdout and a separately predeclared no-refit confirmation totaling 51 post-freeze runs. Energy MAPE is 6.23% and 7.35%, with Spearman rank correlations of 0.976 and 0.933. However, a predeclared TTFT gate passes at concurrency four (9.27% MAPE) and triggers abstention below four (64.80%), showing why energy accuracy cannot certify latency.

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

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chenxu Niu
- 发布：2026-08-20；更新：2026-08-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
