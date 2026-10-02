---
title: "ShatterQuant: Breaking Uniform Precision with Block-Wise Mixed-Precision on a Systolic Transformer Hardware Accelerator"
description: "Due to limited support for intra-tensor heterogeneous precision in conventional accelerators, neural network quantization remains largely restricted to per-tensor precision assignment."
---

**评分：43/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2610.00207) · [PDF](https://arxiv.org/pdf/2610.00207)

## 一句话摘要

Due to limited support for intra-tensor heterogeneous precision in conventional accelerators, neural network quantization remains largely restricted to per-tensor precision assignment.

## 为什么值得关注

待编辑增强。

## 摘要原文

Due to limited support for intra-tensor heterogeneous precision in conventional accelerators, neural network quantization remains largely restricted to per-tensor precision assignment. We present ShatterQuant, a hardware-software co-designed framework enabling mixed-precision quantization within each tensor by assigning independent bit-widths to blocks of a weight projection. ShatterQuant couples precision granularity with PE configuration, such that each precision determines an effective block height. We introduce (1) a hardware-aware post-training method that assigns intra-tensor precision based on block-level standard deviation and weight sensitivity; (2) the ShatterQuant Transformer Accelerator supporting 1/2/4/8-bit weight precision, precision-dependent PE configuration, block rescaling, and integrated softmax and piecewise-linear nonlinearities; and (3) an evaluation of model-hardware tradeoffs using an implementation in the TSMC 16nm PDK operating at 1 GHz, achieving 1.5 TOPS, 760 GOPS/$mm^2$ area efficiency, and 2.8 TOPS/W energy efficiency. On DeiT and ImageNet-1K, ShatterQuant achieves accuracy within $3.3\%$ of state-of-the-art mixed-precision techniques while using a 2 bit lower effective bitwidth, while for PixelDiT demonstrates comparable generation quality. ShatterQuant demonstrates how fine-grained intra-tensor mixed-precision can be realized through hardware-software co-design.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator, hardware-aware
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mikolaj Walczak, Edward Humes, Chao Fang, Marian Verhelst, Tinoosh Mohsenin
- 发布：2026-10-02；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
