---
title: "PACT: NVFP4 Data-Flow LoRA Fine-Tuning on Consumer GPUs"
description: "Fine-tuning language models on consumer GPUs is constrained by computation and memory."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.25048) · [PDF](https://arxiv.org/pdf/2610.25048)

## 一句话摘要

Fine-tuning language models on consumer GPUs is constrained by computation and memory.

## 为什么值得关注

待编辑增强。

## 摘要原文

Fine-tuning language models on consumer GPUs is constrained by computation and memory. Although LoRA reduces trainable parameters and optimizer state, frozen projections remain expensive, and activations retained for backward can dominate memory usage. We present PACT, a LoRA fine-tuning system that accelerates frozen projections with native NVFP4 GEMMs while reducing quantization and dequantization overhead and limiting quantization error. To reduce activation memory, PACT reuses quantized RMSNorm outputs and saves gate/up activations in NVFP4 for backward. To limit numerical error, it preserves BF16 inputs for forward nonlinear operations and calibrates frozen weights offline using GPTQ adapted to NVFP4 scales and quantized activations. Fused nonlinear kernels and cached forward and backward weight layouts reduce quantization and dequantization overhead. Evaluations across multiple models and tasks on a 16\,GB RTX~5080 show lower memory usage and faster LoRA fine-tuning with competitive accuracy, enabling model adaptation on resource-constrained consumer hardware.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Lei Gao, Hossein Entezari Zarch, Chaoyi Jiang, Murali Annavaram
- 发布：2026-10-20；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
