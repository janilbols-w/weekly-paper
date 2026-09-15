---
title: "ETCInfer: An Energy-efficient Thermal-aware Cooling-joint Scheduler for LLM Inference in AI Datacenters"
description: "Large language model (LLM) inference in AI datacenters creates a coupled control problem between GPU serving and facility cooling."
---

**评分：42/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2609.15230) · [PDF](https://arxiv.org/pdf/2609.15230)

## 一句话摘要

Large language model (LLM) inference in AI datacenters creates a coupled control problem between GPU serving and facility cooling.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) inference in AI datacenters creates a coupled control problem between GPU serving and facility cooling. Raising ambient temperature setpoints can reduce cooling energy and carbon, but also shrinks thermal headroom, induces GPU throttling, and leads to Service-Level-Objective (SLO) violations. In this paper, we study joint cooling--computing control for LLM inference: minimizing per-job GPU-plus-cooling energy while satisfying thermal safety and latency SLO constraints. We present ETCInfer, an energy-efficient, thermal-aware scheduler that selects a pre-job Computer Room Air Conditioner (CRAC) setpoint and adapts per-GPU frequency and micro-batch size during execution. ETCInfer builds compact physics-informed control models by calibrating GPU heat generation, chassis heat dissipation, CRAC power, and prefill/decode latency relations from telemetry. These models estimate hidden thermal states and time-to-throttle, enabling the scheduler to evaluate energy, temperature, and latency before applying an action. We formulate this joint setpoint--frequency--micro-batch control problem as a partially observable Markov decision process and design ETCAdapter, a learning-based controller that minimizes per-job energy under thermal safety and SLO constraints. We implement ETCInfer as a coordination layer over typical inference and cluster management stacks. Evaluation across real-trace simulation and validation experiments shows that ETCInfer reduces total job energy by up to 33.1%, thermal throttle exposure by up to 92.9%, and keeps SLO violation rates below 0.7% even at ambient temperatures up to $48^{\circ}\mathrm{C}$.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: slo
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Rui Lu, Rui Ge, Huanghuang Liang, Xiaobo Zhou, Dan Wang
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
