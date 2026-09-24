---
title: "MicroQonv: Reshaping Convolution Tensors for Efficient Microscaling in Training and Inference"
description: "Microscaling quantization techniques are increasingly used to represent neural network parameters with 8 bits or fewer while preserving near-full precision accuracy."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.28358) · [PDF](https://arxiv.org/pdf/2609.28358)

## 一句话摘要

Microscaling quantization techniques are increasingly used to represent neural network parameters with 8 bits or fewer while preserving near-full precision accuracy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Microscaling quantization techniques are increasingly used to represent neural network parameters with 8 bits or fewer while preserving near-full precision accuracy. However, applying these methods efficiently in convolutional layers is not straightforward. A naive approach transfers full-precision weights and activations to processing units and quantizes each tensor twice, resulting in much more memory movement than expected. Additional overhead comes from the activation tensors, whose sizes grow substantially because of the im2col transformation applied before quantization. We propose MicroQonv, a way to combine microscaling with convolutional layers' forward and backward operations by quantizing each tensor only once and quantizing the activation tensor before applying a modified version of im2col: channel-batch-first im2col. MicroQonv reduces the quantization cost by a factor of $\times2$ for weights and gradients, and by up to $\times9$ for activations, at a negligible accuracy cost. It reduces memory movement and storage by up to $\times7.53$ compared to their full-precision counterparts. This way, MicroQonv reduces microscaling-quantized activation memory movement by $\times3.5$ for state-of-the-art object detection models YOLOV8nano and $\times2.2$ for YOLOV26nano. It also enables 4-bit microscaling in a quantized latent replay strategy for continual learning at the edge, improving accuracy by +5.7% to +11%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: microscaling, quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Romain Facq, Sami Ben Ali, Olivier Sentieys
- 发布：2026-09-24；更新：2026-09-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
