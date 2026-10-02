---
title: "The Devil Is in the Reconstruction Loss Scale: Rethinking Optimization in LLM Quantization"
description: "Post-training quantization (PTQ) methods typically use sequential quantization that partitions a pre-trained LLM into a series of units (e.g., transformer blocks), with one unit quantized at each stage."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.00983) · [PDF](https://arxiv.org/pdf/2610.00983)

## 一句话摘要

Post-training quantization (PTQ) methods typically use sequential quantization that partitions a pre-trained LLM into a series of units (e.g., transformer blocks), with one unit quantized at each stage.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training quantization (PTQ) methods typically use sequential quantization that partitions a pre-trained LLM into a series of units (e.g., transformer blocks), with one unit quantized at each stage. State-of-the-art PTQ methods are predominantly learning-based, optimizing auxiliary quantization parameters (e.g., scaling factors, rotation matrices, clipping thresholds, and adapters) via gradient descent to minimize a reconstruction loss. A common practice is to use mean squared error (MSE) as the reconstruction loss function, yet its induced optimization behavior remains largely unexplored. In this work, we take a holistic view of sequential quantization and systematically investigate how optimization evolves from the first quantization stage to the last, aiming for a deep understanding of optimization in learning-based PTQ schemes. Through extensive empirical studies spanning representative learning-based PTQ methods, LLM families, model scales, architectures, quantization settings and various tasks, we consistently uncover Optimization Imbalance: reconstruction loss magnitudes vary dramatically across stages, accompanied by highly uneven gradient magnitudes and parameter updates under MSE. We term the cross-stage range of loss magnitudes the reconstruction loss scale, and reveal that MSE translates the unexpectedly large reconstruction loss scale into highly uneven gradient magnitudes, which in turn lead to uneven optimization strength across quantization stages. This finding suggests a general principle for improving learning-based PTQ: optimization strength across stages should be decoupled from the reconstruction loss scale. Theoretically, we show that root mean squared error (RMSE) variants defined at the sample, channel, token, and element levels naturally realize this principle through implicit gradient normalization, outperforming MSE significantly as a drop-in replacement.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Chao Li, Shigeng Wang, Anbang Yao
- 发布：2026-10-01；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/IntelChina-AI/RMSE](https://github.com/IntelChina-AI/RMSE)
- 阅读深度：metadata
