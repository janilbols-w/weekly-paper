---
title: "HiCal: Offline Calibration for Hierarchical Scale Encoding in Accurate HiF4 Quantization"
description: "Block floating-point (BFP) quantization is widely adopted for efficient low-bit large language model (LLM) inference, where the choice of block scales plays a critical role in quantization accuracy."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.32624) · [PDF](https://arxiv.org/pdf/2611.32624)

## 一句话摘要

Block floating-point (BFP) quantization is widely adopted for efficient low-bit large language model (LLM) inference, where the choice of block scales plays a critical role in quantization accuracy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Block floating-point (BFP) quantization is widely adopted for efficient low-bit large language model (LLM) inference, where the choice of block scales plays a critical role in quantization accuracy. HiFloat4 (HiF4) employs a hierarchical scale encoding scheme consisting of a global E6M2 scale and two levels of binary scale extensions. However, its conventional rounding rule and fixed scale extension thresholds may not fully capture the statistical characteristics of the quantized tensors in practice, leading to suboptimal scale representations. In this work, we propose HiCal, an offline calibration approach that improves HiF4 quantization accuracy by refining the encoding decisions across all three scale levels. Specifically, we introduce a calibrated rounding bias for the Level-1 E6M2 scale and optimize the scale-extension thresholds at Levels 2 and 3 based on the empirical distributions of local group magnitudes. The resulting calibration parameters are determined offline and remain fixed during inference, while the hierarchical encoding continues to adapt to individual blocks through their local values. This design eliminates the need for per-block multi-candidate scale search while preserving the original deterministic HiF4 encoding procedure. Experiments across five synthetic and real activation distributions show that the proposed method reduces quantization MSE by 9.91%-23.50% relative to the original HiF4 scheme, including a 13.00% reduction on real Qwen3-8B activations. End-to-end evaluations across six benchmarks further show average-score improvements of 0.91 and 1.25 percentage points on Qwen3-8B and Qwen3-30B-A3B, respectively, without per-block multi-candidate search during inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhiyuan Zhang, Yanzhao Li, Hui Dong, Sifan Cheng, Mingen Zheng, Hui Wang
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
