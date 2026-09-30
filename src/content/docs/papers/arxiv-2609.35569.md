---
title: "Beyond Energy: When Sustainability Dimensions Reshape LLM Serving Decisions"
description: "Large language model (LLM) serving has environmental impacts across energy consumption, carbon emission, water consumption, and biodiversity loss."
---

**评分：44/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.35569) · [PDF](https://arxiv.org/pdf/2609.35569)

## 一句话摘要

Large language model (LLM) serving has environmental impacts across energy consumption, carbon emission, water consumption, and biodiversity loss.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) serving has environmental impacts across energy consumption, carbon emission, water consumption, and biodiversity loss. Yet these dimensions are largely evaluated in isolation, leaving it unclear when and how they lead to different optimization decisions. We present PRISM, a unified framework for characterizing and optimizing LLM serving across energy, carbon, water, and biodiversity impacts. Our analysis reveals a fundamental distinction: computing configurations determine energy consumption, whereas where and when LLM serving is deployed determine its carbon, water, and biodiversity impacts. Under a fixed deployment choice and operational-only accounting, all dimensions preserve the same energy-based configuration ranking. Deployment rankings can diverge across dimensions, while embodied impacts can break configuration invariance when they exceed a lifecycle crossover boundary. PRISM identifies these conditions, quantifies cross-dimensional regrets, and balances the four dimensions. In regional-routing experiments, PRISM reduces median worst-case regret by 50.2% relative to the strongest baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tianyao Shi, Xipeng Shen, Yi Ding
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
