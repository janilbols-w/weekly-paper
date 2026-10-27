---
title: "On Orthogonal Recurrent Neural Networks Quantization"
description: "In recent years, Orthogonal Recurrent Neural Networks (ORNNs) have gained popularity due to their ability to manage tasks involving long-term dependencies, such as the Copy-task, and their linear complexity."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2402.04012) · [PDF](https://arxiv.org/pdf/2402.04012)

## 一句话摘要

In recent years, Orthogonal Recurrent Neural Networks (ORNNs) have gained popularity due to their ability to manage tasks involving long-term dependencies, such as the Copy-task, and their linear complexity.

## 为什么值得关注

待编辑增强。

## 摘要原文

In recent years, Orthogonal Recurrent Neural Networks (ORNNs) have gained popularity due to their ability to manage tasks involving long-term dependencies, such as the Copy-task, and their linear complexity. However, existing ORNNs utilize full precision weights and activations, which prevents their deployment on compact devices. In this paper, we explore the quantization of the weight matrices in ORNNs, leading to Quantized approximately Orthogonal RNNs (QORNNs). The construction of such networks remained an open problem, acknowledged for its inherent instability. We propose and investigate two strategies to learn QORNN by combining quantization-aware training (QAT) and orthogonal projections. We also study post-training quantization of the activations for pure integer computation of the recurrent loop. The most efficient fully-quantized models are currently the only alternatives for solving the Copy-task with 1000 timesteps. They also surpass existing quantized models on tasks requiring long-term dependencies, such as permuted MNIST as well as some Internet of Things (IoT) tasks. However, they are less effective on tasks where long short-term memory (LSTMs) and other gated RNNs outperform ORNNs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Armand Foucault (IMT), Franck Mamalet (Comue de Toulouse), Fran\c{c}ois Malgouyres (IMT)
- 发布：2026-10-26；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
