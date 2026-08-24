---
title: "Llama-Mobile: Efficient 2.7-Bit Quantization of VLMs"
description: "Deploying vision-language models (VLMs) on mobile devices is challenging due to their significant memory and compute requirements."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.21134) · [PDF](https://arxiv.org/pdf/2608.21134)

## 一句话摘要

Deploying vision-language models (VLMs) on mobile devices is challenging due to their significant memory and compute requirements.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deploying vision-language models (VLMs) on mobile devices is challenging due to their significant memory and compute requirements. We present a framework for quantizing VLMs for efficient inference on resource-constrained hardware. Our approach combines a quantization pipeline that uses the model itself to generate training data and does not require access to the training setup, with a novel 2.7-bit-per-parameter format supporting efficient execution on Arm CPUs. We validate our approach by compressing the Llama 3.2 11B Vision Instruct model to 3.7 GB with 8-bit activations, preserving strong performance on a set of standard visual question answering tasks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Luka Ribar, Jeevan Bhoot, Douglas Orr
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
