---
title: "Unleashing the Potential of Large Language Models: A Blueprint for Real-Time, Enterprise-Ready Deployments"
description: "Large language models deployed in real-time, regulated settings face knowledge staleness, catastrophic forgetting, hallucination, and weak feedback loops."
---

**评分：41/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2608.00419) · [PDF](https://arxiv.org/pdf/2608.00419)

## 一句话摘要

Large language models deployed in real-time, regulated settings face knowledge staleness, catastrophic forgetting, hallucination, and weak feedback loops.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models deployed in real-time, regulated settings face knowledge staleness, catastrophic forgetting, hallucination, and weak feedback loops. We present a unified, pattern-driven LLMOps architecture integrating real-time data ingestion, continual learning, retrieval-augmented generation (RAG), and human-in-the-loop feedback into a single operational pipeline. Four contributions map to established software design patterns: an adaptive ingestion pattern orchestrator (AIPO) evaluated with FreshStreamBench; STAR+FAR continual learning with sparse temporal adapter routing and freshness-aware replay; SAGE, an SLO-aware adaptive retrieval policy predicting a per-query passage budget to meet tail-latency targets; and an automated feedback-driven convergence stage with RLHF triggers. The result reduces latency-cost-accuracy trade-offs while supporting auditability and rollback for high-risk sectors such as health care and finance.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 6 |

## 证据与限制

- taxonomy keywords: slo
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Muhammad Faizan Raza, Shuo, Yang, Satish Mahadevan Srinivasan, Joanna F. DeFranco
- 发布：2026-08-01；更新：2026-08-04
- 来源：arXiv RSS；Venue：Computer, vol. 59, no. 4, pp. 195-199, April 2026
- 代码：未发现
- 阅读深度：metadata
