---
title: "Knowledge boundary probing and demand-guided intervention for LLM-based power system code generation"
description: "Large language models (LLMs) can turn grid-analysis requests into executable programs for power-system simulation, but utilities and research laboratories often require on-premise deployment."
---

**评分：47/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2605.31478) · [PDF](https://arxiv.org/pdf/2605.31478)

## 一句话摘要

Large language models (LLMs) can turn grid-analysis requests into executable programs for power-system simulation, but utilities and research laboratories often require on-premise deployment.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) can turn grid-analysis requests into executable programs for power-system simulation, but utilities and research laboratories often require on-premise deployment. In this setting, first-pass failures frequently arise at an API-knowledge boundary, through hallucinated functions, misused parameters, and mishandled result tables. We present PowerCodeBench, a parameterised benchmark generator released as a frozen 2,000-task suite for pandapower, and a deployment-time workflow that requires no weight updates. Documentation-driven L0-L3 probes produce per-model API profiles for diagnosis, model comparison, documentation allocation, and backend calibration. A query-side demand estimator selects layered API evidence before generation, while execution feedback routes targeted repair. Across ten open-weight LLMs (1.5B-480B) and four mid-tier APIs, the validation-enabled workflow raises scalar-match accuracy by 32-56 percentage points after up to three repair rounds relative to an unassisted first pass, for every model of at least 7B and every API. Open-weight models in the 70B-120B range reach the four-vendor mid-tier accuracy range under matched no-tool conditions. Selective injection approaches the full-layer reference using 41% of its prompt tokens. Among model-item pairs passing numerical checks under both workflows, engineering review confirms the requested analysis in 88% of full-workflow outputs versus 66% under plain repair. Round-0 pilots on OpenDSS and PyPSA motivate staged onboarding from broad retrieval at cold start to calibrated selective injection. Measured throughput, latency, energy, and allocated GPU memory establish a practical on-premise serving envelope.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hui Wu, Xiaoyang Wang, Zhong Fan
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
