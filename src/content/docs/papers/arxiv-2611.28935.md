---
title: "STEdgeFormer: MCU and NPU Deployable Transformer Architecture"
description: "Transformer-based sequence models have achieved strong performance in language and time-series modeling, but self-attention remains computationally and memory intensive for deployment on resource-constrained edge accelerators."
---

**评分：41/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2611.28935) · [PDF](https://arxiv.org/pdf/2611.28935)

## 一句话摘要

Transformer-based sequence models have achieved strong performance in language and time-series modeling, but self-attention remains computationally and memory intensive for deployment on resource-constrained edge accelerators.

## 为什么值得关注

待编辑增强。

## 摘要原文

Transformer-based sequence models have achieved strong performance in language and time-series modeling, but self-attention remains computationally and memory intensive for deployment on resource-constrained edge accelerators. We propose STEdgeFormer, a lightweight, hardware-aware sequence architecture designed for efficient execution on embedded neural accelerators. STEdgeFormer combines polynomial mixture layers and DyT normalization with an accelerator-aware causal memory block, replacing pairwise self-attention with compact causal aggregation. On TinyStories, the fully NPU-supported STEdgeFormer (MW) achieves a perplexity of 7.39 with 4.12M parameters and 6.51 MB RAM, with an end-to-end latency of 40 ms. In comparison, the standard 4.12M-parameter configuration achieves a lower perplexity of 6.79 but requires CPU fallback for unsupported operators, resulting in 1450 ms latency. Vanilla Transformer, on the other hand, achieves a perplexity score of 5.71 using a 4.40M-parameter model, but it cannot be deployed on the hardware. On downstream tasks, STEdgeFormer achieves 94% accuracy on ECG5000 and 93% accuracy on Speech Commands with 1.39M parameters. These results demonstrate that hardware-aware architectural choices and operator compatibility can have a substantial impact on practical inference latency, beyond model size and task accuracy alone. Rather than targeting state-of-the-art accuracy on individual benchmarks, STEdgeFormer is designed to provide a deployable sequence modeling architecture under the memory, computational, and operator constraints of embedded neural accelerators.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator, hardware-aware
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sudhakar Sah
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
