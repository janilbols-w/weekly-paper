---
title: "Energy-Aware Agentic Orchestration for Multi-Site Service Deployment"
description: "Energy-aware orchestration across geographically distributed infrastructures is increasingly important as data centers absorb growing Artificial Intelligence (AI) workloads."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2610.14793v1) · [PDF](https://arxiv.org/pdf/2610.14793v1)

## 一句话摘要

Energy-aware orchestration across geographically distributed infrastructures is increasingly important as data centers absorb growing Artificial Intelligence (AI) workloads.

## 为什么值得关注

待编辑增强。

## 摘要原文

Energy-aware orchestration across geographically distributed infrastructures is increasingly important as data centers absorb growing Artificial Intelligence (AI) workloads. However, existing approaches often exclude the energy cost of automated decision-making from system-level sustainability assessments. This paper presents an energy-aware agentic orchestration framework that treats Large Language Model (LLM) reasoning as a measurable component of the control loop. We compare single-shot tool calling, ReAct, and plan-and-execute strategies on a multi-site Kubernetes testbed spanning two European data centers and instrumented at layers ranging from power distribution units to per-pod energy attribution. Using ten natural-language orchestration intents with varying decision complexity, we show that reasoning strategy and intent complexity strongly influence graphics processing unit (GPU) energy consumption during orchestration decisions. ReAct and plan-and-execute generated executable tool calls across all evaluated intents but required multiple LLM inferences, whereas the single-shot configuration was less costly but non-actionable. Prefix caching reduced mean ReAct GPU energy consumption by 29.4%. For the evaluated lightweight workload, the infrastructure-energy changes observed within the one-second measurement window were insufficient to offset the measured GPU decision energy. These findings demonstrate the importance of accounting for reasoning overhead when assessing the sustainability of AI-native orchestration and motivate energy-budgeted selection of agent strategies.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: prefix caching
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Rodrigo Moreira, Alisson Chaves, Larissa F. Rodrigues Moreira, Tereza Carvalho, Tiago Barros, Daniel Corujo, Rui Aguiar, David Gomez-Barquero, Flávio de Oliveira Silva
- 发布：2026-10-10；更新：2026-10-10
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
