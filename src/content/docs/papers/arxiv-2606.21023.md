---
title: "Demystifying Numerical Instability in LLM Inference: Achieving Reproducible Inference for Mission-Critical Tasks with HEAL"
description: "As Large Language Models (LLMs) deploy into mission-critical domains (e.g., finance, medicine, and law), output reproducibility has become a strict system requirement."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2606.21023) · [PDF](https://arxiv.org/pdf/2606.21023)

## 一句话摘要

As Large Language Models (LLMs) deploy into mission-critical domains (e.g., finance, medicine, and law), output reproducibility has become a strict system requirement.

## 为什么值得关注

待编辑增强。

## 摘要原文

As Large Language Models (LLMs) deploy into mission-critical domains (e.g., finance, medicine, and law), output reproducibility has become a strict system requirement. While practitioners use greedy decoding to eliminate algorithmic stochasticity, empirical deployments with 16-bit precisions still exhibit catastrophic output divergence across heterogeneous GPUs. Through SASS-level profiling, we reveal that this inconsistency is fundamentally driven by truncation errors introduced during downcasting at kernel boundaries. However, achieving reproducibility via a global FP32 pipeline incurs prohibitive system penalties: bypassing 16-bit hardware accelerators hurts compute efficiency, while upcasting the KV cache doubles memory overhead. To bridge this gap, we propose Hybrid Error ALleviation (HEAL), a targeted intervention that approximates FP32 precision while resolving hardware constraints through two targeted mechanisms. First, recognizing that floating-point formats underutilize their bit-width for Q, K, V tensors, HEAL applies INT16 quantization that preserves numerical stability without expanding the KV cache footprint. Second, HEAL synthesizes high-precision matrix multiplications via an algebraic error compensation strategy, executing entirely on high-throughput 16-bit Tensor Cores. To evaluate our approach practically, we introduce MCR-Bench, a benchmark targeting reproducibility in mission-critical tasks. HEAL achieves the same level of reproducibility on downstream tasks as the FP32 baseline while reducing the performance overhead by up to 6.0$\times$.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhenting Zhu, Lucas Thai, Shan Yu, Yicheng Liu, Yifan Qiao, Chenxi Wang, Harry Xu, Junyi Shu
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
