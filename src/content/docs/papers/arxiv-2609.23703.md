---
title: "Financial Language Models as Applied Artificial Intelligence Systems for News-Based Trading under Market Frictions"
description: "Financial language models can transform unstructured firm-specific news into structured decision signals, but financial AI research lacks an integrated deployment framework for evaluating whether those signals remain useful in financial decision systems."
---

**评分：48/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2609.23703) · [PDF](https://arxiv.org/pdf/2609.23703)

## 一句话摘要

Financial language models can transform unstructured firm-specific news into structured decision signals, but financial AI research lacks an integrated deployment framework for evaluating whether those signals remain useful in financial decision systems.

## 为什么值得关注

待编辑增强。

## 摘要原文

Financial language models can transform unstructured firm-specific news into structured decision signals, but financial AI research lacks an integrated deployment framework for evaluating whether those signals remain useful in financial decision systems. Computer science research has developed strong methods for time-series forecasting, text classification, multimodal stock prediction, graph-based market modeling, and machine-learning operations, yet these streams do not provide a domain-specific protocol that jointly tests financial language-model outputs under event-time observability, probability calibration, execution timing, transaction costs, liquidity constraints, capacity limits, operational diagnostics, and statistical inference. We introduce MFAST, a Market-Friction-Aware Sentiment-to-Trading framework that converts timestamped financial text into auditable, reproducible, and market-feasible trading decisions. The application is news-based trading, where firm-specific text must be linked to securities before portfolio decisions can be evaluated. The framework links Refinitiv News Analytics to Center for Research in Security Prices (CRSP) equity data, restricts the primary out-of-sample evaluation to post-release news outside disclosed foundation-model data-freshness periods, and adds a public replication arm using open financial text and public price data. Results show that decoder-only language models outperform encoder baselines and dictionary sentiment in classification, calibration, return prediction, and net portfolio performance, while operational diagnostics reveal trade-offs among accuracy, latency, memory, throughput, and inference cost. The paper shows that credible evaluation of financial language models requires an end-to-end engineering approach combining language understanding, temporal discipline, market-friction-aware deployment, and reproducible validation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 13 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: observability
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kemal Kirtac
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
