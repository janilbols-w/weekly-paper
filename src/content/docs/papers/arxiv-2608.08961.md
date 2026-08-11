---
title: "Gradient Under Microscope: Benchmarking Resource Utilization of Memory-Efficient Gradient Computation Methods"
description: "AI training's rising resource intensity is straining electricity supplies and carbon budgets, motivating systematic study of memory-efficient training on constrained hardware."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2608.08961) · [PDF](https://arxiv.org/pdf/2608.08961)

## 一句话摘要

AI training's rising resource intensity is straining electricity supplies and carbon budgets, motivating systematic study of memory-efficient training on constrained hardware.

## 为什么值得关注

待编辑增强。

## 摘要原文

AI training's rising resource intensity is straining electricity supplies and carbon budgets, motivating systematic study of memory-efficient training on constrained hardware. We benchmark five gradient optimizers (SGD, Adam, Adagrad, Adadelta, and Conjugate Gradient Descent) under three memory strategies (standard training, gradient checkpointing, and gradient accumulation) across four transformer architectures (ViT, ModernBERT, Llama 3.1 1B, and NanoVLM), measuring training loss, GPU utilization, training time, and memory usage. Gradient accumulation emerges as the most reliable strategy, cutting training loss by roughly an order of magnitude on the vision-language model and about four-fold on the language model without additional GPU memory. Contrary to common practice, Adam is not universally superior: Adadelta and SGD outperform it on the encoder and autoregressive architectures. Gradient checkpointing's effect is strongly architecture-dependent, improving vision transformer loss while severely degrading the encoder model, and it increases training time by up to 60% on memory-bound models. GPU utilization is governed primarily by architecture, ranging from 8-15% for the memory-bound language model to 96-99% for compute-bound vision models. These findings provide practical guidelines for optimizer and gradient-strategy selection in resource-efficient model training and deployment.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sarthak Mahapatra, Zihan Zhou, Khatoon Khedri, Mehdi Hosseinzadeh, Reza Rawassizadeh
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
