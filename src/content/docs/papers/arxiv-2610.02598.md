---
title: "Activation Sparsity with Weight Approximation for Faster LLM Decoding on Offloaded Weights"
description: "Deploying LLMs on consumer-grade GPUs with insufficient memory to hold their weights can result in prohibitively slow inference, because decoding repeatedly transfers offloaded weights from system RAM or flash storage into GPU at much lower bandwidth than local GPU-memory access."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.02598) · [PDF](https://arxiv.org/pdf/2610.02598)

## 一句话摘要

Deploying LLMs on consumer-grade GPUs with insufficient memory to hold their weights can result in prohibitively slow inference, because decoding repeatedly transfers offloaded weights from system RAM or flash storage into GPU at much lower bandwidth than local GPU-memory access.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deploying LLMs on consumer-grade GPUs with insufficient memory to hold their weights can result in prohibitively slow inference, because decoding repeatedly transfers offloaded weights from system RAM or flash storage into GPU at much lower bandwidth than local GPU-memory access. Activation sparsity reduces these transfers by skipping weights associated with zero or near-zero activations. However, as more activation contributions are omitted, model quality eventually degrades rapidly, indicating that weights associated with small-magnitude activations collectively influence model quality sharply. In this work, we improve the trade-off between model quality and decoding performance when exploiting activation sparsity. Our key idea is to replace the binary choice of whether or not to read a weight with three options: fully retain it, approximate it using a compressed weight representation, or omit it entirely. SpAx skips weights associated with activations closest to zero, reads approximate weights for smaller-magnitude activations, and reads original weights for the largest-magnitude activations. Smaller-magnitude activations attenuate the errors introduced by approximate weights, while compressed weight representations require fewer bytes to be transferred. With weights offloaded to CPU memory, SpAx speeds up decoding by 3.86X on average (up to 5.57X) with 16-bit weights and 2.06X (up to 2.74X) with 4-bit weights, at a WikiText-2 perplexity increase of at most 10%. With weights offloaded to flash storage, the speedups are 3.31X on average (up to 4.81X) and 1.54X (up to 2.03X).

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：JuneHyung Kim, Sankeerth Durvasula, Nandita Vijaykumar
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
