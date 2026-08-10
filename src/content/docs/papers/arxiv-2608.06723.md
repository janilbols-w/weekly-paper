---
title: "Multi-Level Modeling of Large Language Model Inference Latency and Energy via Hybrid Analytical--Machine-Learning Predictors"
description: "The rapid scaling of Large Language Models (LLMs) has significantly increased computational cost, energy consumption, and inference latency, making accurate estimation essential for sustainable artificial intelligence deployment and hardware-aware design."
---

**评分：41/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2608.06723) · [PDF](https://arxiv.org/pdf/2608.06723)

## 一句话摘要

The rapid scaling of Large Language Models (LLMs) has significantly increased computational cost, energy consumption, and inference latency, making accurate estimation essential for sustainable artificial intelligence deployment and hardware-aware design.

## 为什么值得关注

待编辑增强。

## 摘要原文

The rapid scaling of Large Language Models (LLMs) has significantly increased computational cost, energy consumption, and inference latency, making accurate estimation essential for sustainable artificial intelligence deployment and hardware-aware design. In this work, we introduce Hybrid Modeling for Energy and Latency of LLMs (HYMELL), a hybrid three-level framework for estimating LLM inference latency and energy by combining analytical modeling with machine learning (ML). HYMELL models LLM execution through a three-level hierarchy: analytical estimation of primitive operations, ML prediction of higher-level components, and an end-to-end model that captures system-level overheads across both prefill and decode phases. The framework supports diverse architectures, including dense and mixture-of-experts (MoE) feed-forward networks (FFNs), as well as multi-head attention (MHA) and grouped-query attention (GQA) mechanisms. Evaluated on an NVIDIA H100 graphics processing unit (GPU), HYMELL achieves high predictive accuracy; notably, for LLaMA 3 8B, it attains less than 5% error for both prefill and decode phases. By predicting execution costs directly from architectural parameters, it enables fast, hardware-free design space exploration and energy-efficient optimization.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: hardware-aware
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Saeid Shokoufa, Mohammad Erfan Sadeghi, Mehdi Kamal, Massoud Pedram
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
