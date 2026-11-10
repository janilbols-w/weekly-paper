---
title: "Cross-Layer TopK: Dynamically Allocating Sparsity Across Layers in Transcoders"
description: "Cross-Layer Transcoders (CLTs) decompose the activations of large language models into human-interpretable features and trace how these features interact across layers to form circuits, making them a key tool for mechanistic interpretability."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.09233) · [PDF](https://arxiv.org/pdf/2611.09233)

## 一句话摘要

Cross-Layer Transcoders (CLTs) decompose the activations of large language models into human-interpretable features and trace how these features interact across layers to form circuits, making them a key tool for mechanistic interpretability.

## 为什么值得关注

待编辑增强。

## 摘要原文

Cross-Layer Transcoders (CLTs) decompose the activations of large language models into human-interpretable features and trace how these features interact across layers to form circuits, making them a key tool for mechanistic interpretability. However, training CLTs effectively and efficiently is hard. Beyond the usual trade-off between sparsity and reconstruction quality, a CLT has to model all layers at once, which adds a further challenge. The common JumpReLU recipe controls sparsity only indirectly through a penalty, while the direct extension of TopK selects a fixed number of latents in every layer. Yet reconstruction difficulty differs widely across layers, and intermediate layers are much harder than others, so giving every layer the same budget is suboptimal. We propose Cross-Layer TopK, which sets a single L0 budget for the whole model and dynamically allocates it across layers during training. In a comparison with JumpReLU and other TopK variants on Qwen3-8B-Base, this gives lower FVU while using 20% fewer active latents than JumpReLU. The better reconstruction carries over to circuit tracing, yielding more complete circuits with higher replacement and completeness scores. The fixed per-token budget of Cross-Layer TopK also makes it easy to pair with sparse decoding, which cuts both computation and communication and gives a 2.9x speedup per training step. We further show that Cross-Layer TopK follows scaling laws in both latent size and sparsity. We have open-sourced the weights of our CLT at https://huggingface.co/ByteDance-Seed/Cross-Layer-TopK-CLT.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Anyuan Zhuo, Shaohua Zhang, Tianle Li, Yuan Lin, Diandian Gu, Jun Wang, Pinyan Lu
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
