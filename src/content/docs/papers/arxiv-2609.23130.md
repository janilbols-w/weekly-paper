---
title: "From Inference Engine to Inference Control Plane: Connecting vLLM, llm-d, and the Evolution of Efficient Distributed LLM Serving"
description: "Large language model (LLM) inference is evolving from an engine-local optimization problem into a distributed control problem involving reusable state, phase placement, heterogeneous accelerators, networking, autoscaling, reliability, and service-level objectives."
---

**评分：49/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.23130) · [PDF](https://arxiv.org/pdf/2609.23130)

## 一句话摘要

Large language model (LLM) inference is evolving from an engine-local optimization problem into a distributed control problem involving reusable state, phase placement, heterogeneous accelerators, networking, autoscaling, reliability, and service-level objectives.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) inference is evolving from an engine-local optimization problem into a distributed control problem involving reusable state, phase placement, heterogeneous accelerators, networking, autoscaling, reliability, and service-level objectives. This paper connects that transition across peer-reviewed systems research, open-source implementations, and documented production studies. It treats vLLM and llm-d as complementary layers: model-serving engines optimize execution through mechanisms such as PagedAttention, continuous batching, kernels, quantization, and parallelism, while an inference control plane can optimize where, when, and under what policy execution occurs across a fleet. The contribution is synthesis rather than a new benchmark; all reported performance and deployment results remain attributed to their original sources. The combined evidence suggests that the scarce resource in modern inference is shifting from raw FLOPs alone toward managed state, placement, network movement, reliability, and decision quality. We propose an Inference Execution Planner that selects feasible execution plans rather than only endpoints, including aggregated versus disaggregated topology, KV source and transfer action, hardware variant, routing/admission policy, and slower scaling decisions. We also provide a source-local benchmark atlas, a bottleneck-migration taxonomy, practical deployment guidance, an evaluation framework based on SLO-goodput, and research questions for agentic, multimodal, heterogeneous, and resilient inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: inference engine, llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Twinkll Sisodia
- 发布：2026-09-19；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
