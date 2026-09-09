---
title: "Toward Sustainable Distributed LLM Inference: A Systems Synthesis and Research Agenda for an Energy-, Carbon-, and Cache-Aware llm-d Control Plane"
description: "Large language model (LLM) sustainability is increasingly a serving-systems problem, not only a training problem."
---

**评分：47/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.05565) · [PDF](https://arxiv.org/pdf/2609.05565)

## 一句话摘要

Large language model (LLM) sustainability is increasingly a serving-systems problem, not only a training problem.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) sustainability is increasingly a serving-systems problem, not only a training problem. In production, energy and carbon impact depend on more than model size: workload shape, batching, key-value (KV) cache reuse, prefill/decode placement, model and accelerator choice, power state, geographic carbon intensity, and service-level objectives (SLOs) all matter. Recent systems papers study many of these factors separately. This paper connects those results and asks a practical engineering question: what do they imply when the decision point is a distributed inference control plane such as llm-d? The contribution here is synthesis, not a new set of benchmark results. Reported performance, energy, carbon, and cost improvements remain the results of the cited papers and systems. I group the literature into recurring design patterns and use those patterns to sketch a Sustainable Inference Control Plane (SICP) for llm-d. The proposed control plane would consider latency, energy, carbon, cache reuse, serving cost, and quality when routing and scaling, while keeping TTFT/TPOT SLOs as hard constraints. I also outline an evaluation framework based on SLO-satisfied goodput per joule and per gram CO2e, together with a reproducible experimental plan. The main observation from connecting the literature is that sustainable LLM inference is unlikely to come from one "green" model or one accelerator; it is more naturally treated as a control problem across model, phase, cache, hardware, replica, region, and time.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 11 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Twinkll Sisodia
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
