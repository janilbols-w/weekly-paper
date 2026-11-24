---
title: "Exploring the Potential of Ultra-Low-Bit Inference on LLM Accelerators"
description: "Vector quantization (VQ) enables ultra-low-bit compression of large language models (LLMs) by encoding groups of values as compact codebook indexes."
---

**评分：38/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2611.27561) · [PDF](https://arxiv.org/pdf/2611.27561)

## 一句话摘要

Vector quantization (VQ) enables ultra-low-bit compression of large language models (LLMs) by encoding groups of values as compact codebook indexes.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vector quantization (VQ) enables ultra-low-bit compression of large language models (LLMs) by encoding groups of values as compact codebook indexes. However, reconstructing these values for computation requires frequent codebook lookups, which conflict with the dataflows of conventional LLM accelerators and limit the performance gains from VQ compression. Consequently, prior work has resorted to VQ-specific accelerator designs, which either incur substantial additional hardware overhead or support only a limited range of inference scenarios. In this work, we argue that existing systolic-array-based LLM accelerators already possess the essential hardware resources for efficient VQ inference, but lack the mechanisms to effectively exploit them. To bridge this gap, we present VQACC, an architectural enhancement that jointly redesigns the existing operand buffer's access logic and data mapping to reuse its storage and port resources for codebook lookups, seamlessly integrating dequantization into the normal operand-addressing dataflow. Evaluation shows that VQACC achieves a 2.63$\times$ speedup over the EVA baseline, with additional hardware occupying only 0.17\% of the compute array's area.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hao Wang, Yang Shi, Jiageng Shi, Qiuran Li, Yaohua Wang
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
