---
title: "Do Dynamic Routers Need Memory? HeRo: History-Aware Routing for Efficient LLM Inference"
description: "Dynamic layer routing reduces the inference cost of Large Language Models (LLMs) by learning to skip layers for individual tokens."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2609.08189) · [PDF](https://arxiv.org/pdf/2609.08189)

## 一句话摘要

Dynamic layer routing reduces the inference cost of Large Language Models (LLMs) by learning to skip layers for individual tokens.

## 为什么值得关注

待编辑增强。

## 摘要原文

Dynamic layer routing reduces the inference cost of Large Language Models (LLMs) by learning to skip layers for individual tokens. Existing methods, however, treat each routing decision as a local operation conditioned solely on the current hidden state which is a formulation that overlooks the sequential, path-dependent nature of routing across depth: earlier decisions shape the representations seen by downstream routers, and the layer-usage objective couples all decisions jointly. We propose History-Aware Routing (HeRo), a dynamic routing framework that resolves this mismatch by introducing a router memory mechanism to maintain an explicit routing state across model depth. The memory is constructed via linear attention, incrementally aggregating preceding routing scores and their induced residual updates into a compact history representation. At each routed layer, the router conditions jointly on this accumulated state and the current hidden representation to select the executed branch. Instantiated for token-wise FFN routing, HeRo trains only lightweight routers and adapters on a frozen backbone, requiring no modification to pretrained parameters. Across Llama 3.1-8B, Llama 2-7B, and Llama 2-13B, HeRo consistently achieves the highest aggregate performance retention among ten baselines. On Llama 3.1-8B, it bypasses 26.87% of model parameters while achieving 100.24% of dense model performance across seven benchmarks, and retains 97.01% while bypassing 38.82% of model parameters under a tighter computation budget. Ablation studies confirm that removing routing history consistently degrades performance, most notably on multistep reasoning and code generation, validating that explicit routing memory enables more accurate and adaptive dynamic routing than solely conditioning on hidden state.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hongjin Lin, Wentao Wan, Keze Wang
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
