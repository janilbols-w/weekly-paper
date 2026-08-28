---
title: "PowerSlider: Exploiting Phase Asymmetry for LLM Serving under Demand Response"
description: "AI inference clusters are increasingly constrained by instantaneous power, not just energy: grid operators condition new capacity on demand response, imposing time-varying power caps."
---

**评分：48/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2608.21719) · [PDF](https://arxiv.org/pdf/2608.21719)

## 一句话摘要

AI inference clusters are increasingly constrained by instantaneous power, not just energy: grid operators condition new capacity on demand response, imposing time-varying power caps.

## 为什么值得关注

待编辑增强。

## 摘要原文

AI inference clusters are increasingly constrained by instantaneous power, not just energy: grid operators condition new capacity on demand response, imposing time-varying power caps. Existing LLM serving systems optimize a static energy objective or shed fixed priority tiers under load; either way, goodput collapses when the power envelope moves. An LLM pipeline is not a uniform load: compute-bound prefill loses throughput almost linearly with GPU frequency, memory-bound answer decode sustains it down to $0.57\times$ nominal, and reasoning's thinking phase couples KV-cache capacity to scheduling -- so a cap should be steered to where each watt costs the least performance. \sys{} does so with a new Flex SLO contract that turns bounded user slack into an optimization constraint, prefill--think--answer disaggregation exposing per-stage frequency and KV control, and a Karush--Kuhn--Tucker (KKT) online solver re-solving within 7.7 ms of every cap change, backed by a consolidated fail-safe that power-gates drained instances when DVFS bottoms out on static power. On SGLang with production traces, \sys{} sustains 78.3\% online goodput at a 30\% cap reduction versus 47.6\% for the best of five baselines ($1.64\times$), holds latency-critical tails within $1.3\times$ of nominal (baselines: $2.3$--$6\times$, up to $12\times$), and delivers 92\% mean goodput through a replayed CAISO grid-emergency day bottoming at $0.41\times$ (54\% at the trough; every baseline below 7\%).

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 15 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yueying Li, Jiayang Chen, Yuanfan Chen, Leo Han, Haoran Qiu, Esha Choukse, Rodrigo Fonseca, Udit Gupta
- 发布：2026-08-22；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
