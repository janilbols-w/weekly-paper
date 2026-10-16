---
title: "Task-Phase-Conditioned Expert Routing Is Not a Reliable Proxy for Quantization Sensitivity in MoE FFN Tensors"
description: "We investigate whether per-layer, per-task-phase (prompt/reasoning/response) expert-routing statistics in a Mixture-of-Experts (MoE) language model can guide layer-wise mixed-precision quantization of routed-expert FFN tensors (down/gate and up)."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2610.20826) · [PDF](https://arxiv.org/pdf/2610.20826)

## 一句话摘要

We investigate whether per-layer, per-task-phase (prompt/reasoning/response) expert-routing statistics in a Mixture-of-Experts (MoE) language model can guide layer-wise mixed-precision quantization of routed-expert FFN tensors (down/gate and up).

## 为什么值得关注

待编辑增强。

## 摘要原文

We investigate whether per-layer, per-task-phase (prompt/reasoning/response) expert-routing statistics in a Mixture-of-Experts (MoE) language model can guide layer-wise mixed-precision quantization of routed-expert FFN tensors (down/gate and up). To attain layerwise routing statistics, we build a routing-capture and profiling pipeline for Qwen-3.6-35B-A3B in ik_llama.cpp, derive a composite sensitivity score from routing entropy/decisiveness, coefficient of variation (CV), Jaccard/phase-fragility, and top-1 expert strength, and use coordinate descent to tune a layer allocation that respects a fixed average bits-per-weight budget. Notably, the profiling pipeline is applicable to standard top-k MoE architectures. Across independent experimental conditions (about 4.0 bpw flat, about 2.7 bpw steep, and about 2.7 bpw random allocation as a control), reallocation fails to outperform the uniform baseline within each quality tier. In the flat regime, reallocation is statistically neutral (z about 0.9). For the steep tier, the random reallocation performs within 1 SE of the routing-guided reallocation at the same tier, indicating a structural loss at this quality rung caused by mandatory downgrades and Kullback-Leibler Divergence (KLD) tail injection. This aggressive-budget condition shows a decisive loss (z greater than 4 SE) replicated across three independent weight vectors. We argue that the deeper issue is that routing-behavior statistics are an unvalidated proxy for true per-layer quantization cost.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: expert routing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yifan Liu
- 发布：2026-10-14；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
