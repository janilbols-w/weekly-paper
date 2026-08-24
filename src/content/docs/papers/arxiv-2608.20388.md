---
title: "Intent Engine: Natural-Language Intent Translation for Intent-Driven Orchestration in the Compute Continuum"
description: "Microservice placement in the compute continuum is driven by low-level Service-level Objectives (SLOs), but requiring users to specify metric-level constraints creates an adoption barrier and increases misconfiguration risk."
---

**评分：39/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2608.20388) · [PDF](https://arxiv.org/pdf/2608.20388)

## 一句话摘要

Microservice placement in the compute continuum is driven by low-level Service-level Objectives (SLOs), but requiring users to specify metric-level constraints creates an adoption barrier and increases misconfiguration risk.

## 为什么值得关注

待编辑增强。

## 摘要原文

Microservice placement in the compute continuum is driven by low-level Service-level Objectives (SLOs), but requiring users to specify metric-level constraints creates an adoption barrier and increases misconfiguration risk. Although large language models (LLMs) can interpret natural-language intents, direct generation of orchestration-consumable SLO artifacts remains unreliable due to unsupported constraints, incorrect grounded values, and schema violations. These errors can propagate to downstream placement logic and produce infeasible or incorrect placements. This paper presents Intent Engine, a natural-language intent translation architecture that constructs validated SLO artifacts for compute-continuum service placement. Intent Engine acts as an intent acquisition and SLO construction layer for existing intent-driven orchestration and placement frameworks; it does not perform placement or runtime QoS optimization. The architecture combines schema-constrained extraction, retrieval-grounded value construction from monitored infrastructure state, and validation against supported constraints before emitting the final SLO artifact. We evaluate Intent Engine using a 716-record intent-to-SLO dataset derived from an edge-cloud testbed, including valid and invalid intents. Across GPT-4.1 mini, Claude Sonnet 4.5, and DeepSeek V4-Flash, Intent Engine outperforms prompting baselines and a non-LLM rule-based parser. With GPT-4.1 mini, it achieves 0.941 total F1 Score and reduces aggregate hallucination by 85.1%, while lowering downstream placement failure from 30.8% to 2.1%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: slo
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Koushikur Islam, Rodrigo N. Calheiros
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
