---
title: "Kilobyte Models: Neural Networks as a Seed and a Quantized Latent"
description: "The cost of storing and transmitting a trained neural network scales with its parameter count, a bottleneck for over-the-air updates, on-device libraries, and other bandwidth-bound deployments."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.00860) · [PDF](https://arxiv.org/pdf/2608.00860)

## 一句话摘要

The cost of storing and transmitting a trained neural network scales with its parameter count, a bottleneck for over-the-air updates, on-device libraries, and other bandwidth-bound deployments.

## 为什么值得关注

待编辑增强。

## 摘要原文

The cost of storing and transmitting a trained neural network scales with its parameter count, a bottleneck for over-the-air updates, on-device libraries, and other bandwidth-bound deployments. We study an extreme form of model compression in which the deployable artifact is not the weights but a short recipe for regenerating them. Building on Mapping Networks, which express a network's weights as a nonlinear function of a compact trainable latent and a fixed random basis, we observe that only the latent need be stored, because the basis and initialization center are reproducible from an integer seed. A model becomes a seed together with a quantized latent, whose size is set by the latent dimension and bit width rather than the parameter count. We formalize this artifact and introduce a seeded block-wise basis that scales to networks whose projection cannot be held in memory. In our experiments, a mapped model is as accurate as the same network quantized aggressively to a few bits per weight, while taking far fewer bytes to store. Reaching the most aggressive bit widths depends on fine-tuning the latent with quantization in the loop. The results do not depend on the particular random basis, and a structured basis lets the weights be regenerated almost for free even for large networks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 4 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sahil Rajesh Dhayalkar
- 发布：2026-08-01；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
