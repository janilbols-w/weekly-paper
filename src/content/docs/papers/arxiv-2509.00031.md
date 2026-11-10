---
title: "End-to-End On-Device Quantization-Aware Training for LLMs at Inference Cost"
description: "Quantization reduces the deployment cost of large language models (LLMs)."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2509.00031) · [PDF](https://arxiv.org/pdf/2509.00031)

## 一句话摘要

Quantization reduces the deployment cost of large language models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Quantization reduces the deployment cost of large language models (LLMs). However, post-training quantization (PTQ) cannot fine-tune model parameters and often degrades accuracy in low-bit settings, while quantization-aware training (QAT) requires backpropagation and incurs high memory overhead. We propose ZeroQAT, a zeroth-order QAT framework supporting both weight and activation quantization. By using forward-only gradient estimation, ZeroQAT removes backpropagation and substantially reduces memory and computation while retaining end-to-end optimization benefits. We further introduce a lightweight variant of ZeroQAT for quantized fine-tuning, which freezes and pre-quantizes most parameters to further cut memory usage. Experiments show that ZeroQAT consistently outperforms representative PTQ and QAT baselines while requiring significantly less memory. For example, ZeroQAT enables fine-tuning of a 13B model at extremely low bit-widths (e.g., 2-4 bits) on a single 8GB GPU, and even allows fine-tuning a 6.7B model on a OnePlus 12 smartphone, demonstrating its practicality for end-to-end QAT on resource-limited edge devices.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qitao Tan, Xiaoying Song, Ningxi Cheng, Guoming Li, Jun Liu, Lingzi Hong, Caiwen Ding, Jundong Li, Xiaoming Zhai, Shaoyi Huang, Jin Lu, Ninghao Liu, Wei Niu, Geng Yuan
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
