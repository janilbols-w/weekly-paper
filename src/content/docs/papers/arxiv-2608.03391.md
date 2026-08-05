---
title: "TimeRLM: Recursive Language Models Enable Precise Anomaly Localization in Long-Context Time-Series"
description: "Precise anomaly localization over long-context time series is a crucial task in monitoring applications across clinical care, industrial operations, financial services, and logistics, where brief evidence may hide inside long spans of high-frequency data."
---

**评分：38/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2608.03391) · [PDF](https://arxiv.org/pdf/2608.03391)

## 一句话摘要

Precise anomaly localization over long-context time series is a crucial task in monitoring applications across clinical care, industrial operations, financial services, and logistics, where brief evidence may hide inside long spans of high-frequency data.

## 为什么值得关注

待编辑增强。

## 摘要原文

Precise anomaly localization over long-context time series is a crucial task in monitoring applications across clinical care, industrial operations, financial services, and logistics, where brief evidence may hide inside long spans of high-frequency data. Time-Series Language Models (TSLMs) are able to ingest time series data and verbalize findings on anomalies in natural language; however, recent benchmarks report a decrease in retrieval performance at long contexts, mirroring failure modes in text, vision, and audio. In the text domain, Recursive Language Models (RLMs) can recover much of this lost performance by keeping context external to the large language model (LLM), allowing the model to query it through code. We present TimeRLM, an RLM formulation for time-series that sequentially manipulates the signal using code and vision capabilities. We further introduce AnomalyXL, a synthetic long-context anomaly localization benchmark with programmatically injected anomalies that require precise retrieval. We implement five different task categories and two variants: AnomalyXL-MCQ and AnomalyXL-Localize. TimeRLM outperforms every evaluated TSLM and single-pass baseline on four of the five AnomalyXL-Localize tasks, reaching 0.682 IoU on localization and 0.745 on classify-with-evidence, versus at most 0.329 and 0.072 across all baselines. We post-train TimeRLM using reinforcement learning. The resulting model further improves performance and requires approximately one-third as many agent interaction turns as its untrained base model to produce a final answer. On unseen real-world ECG, sleep and software observability recordings, the post-trained TimeRLM retains or improves performance, surpassing TSLMs despite being trained exclusively on synthetic data. Our findings suggest recursive interaction with time-series is an effective approach for long-horizon retrieval.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: observability
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Nicolas Zumarraga, Lorenzo Steno, Ning Wang, Max Rosenblattl, Thomas Kaar, Maxwell A. Xu, Kevin O'Sullivan, Markus Kreft, Elgar Fleisch, Paul Schmiedmayer, Patrick Langer, Robert Jakob
- 发布：2026-08-05；更新：2026-08-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
