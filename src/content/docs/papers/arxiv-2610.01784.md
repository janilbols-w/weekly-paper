---
title: "ePACT: Energy-Performance-Aware Commitment Tracking for LLM Serving"
description: "Reducing LLM serving energy does not by itself guarantee lower deployment cost when electricity procurement exposes operators to unfavorable deviations from preset commitments."
---

**评分：45/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2610.01784) · [PDF](https://arxiv.org/pdf/2610.01784)

## 一句话摘要

Reducing LLM serving energy does not by itself guarantee lower deployment cost when electricity procurement exposes operators to unfavorable deviations from preset commitments.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reducing LLM serving energy does not by itself guarantee lower deployment cost when electricity procurement exposes operators to unfavorable deviations from preset commitments. We study hourly commitments with positive, potentially asymmetric costs for overuse and underuse, and formulate energy-Performance-Aware Commitment Tracking: minimize deviation costs subject to request-level service requirements. We implement ePACT, a two-level controller that adjusts serving capacity and GPU clocks as requests arrive. A global planner updates interval energy targets from measured consumption and the remaining hourly commitment. A local decision maker predicts candidate configurations' energy and completion times, checks predicted deadline misses, and selects among admitted configurations by asymmetric target-deviation cost, with a service-first fallback. Coarse-to-fine action search runs asynchronously with serving. We evaluate ePACT through single-hour comparisons, controller ablations, and full-day trace simulations for H20 and H200 GPU pools. In the 24-hour simulations, ePACT reduces the asymmetric deviation cost by $73.8\%$ and $75.7\%$ relative to vLLM while retaining near-vLLM SLO attainment. Mean absolute hourly deviations are $2.16\%$ and $2.31\%$, respectively.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：You Peng, Youhe Jiang, Chen Wang, Binhang Yuan
- 发布：2026-10-02；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
