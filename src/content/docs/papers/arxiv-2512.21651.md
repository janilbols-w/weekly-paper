---
title: "Beyond local reconstruction: Geometry-preserving output alignment for binary LLM quantization"
description: "Recent advances in post-training quantization for large language models (LLMs) have demonstrated that low-bit quantization methods can maintain most of the original model performance."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2512.21651) · [PDF](https://arxiv.org/pdf/2512.21651)

## 一句话摘要

Recent advances in post-training quantization for large language models (LLMs) have demonstrated that low-bit quantization methods can maintain most of the original model performance.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent advances in post-training quantization for large language models (LLMs) have demonstrated that low-bit quantization methods can maintain most of the original model performance. Despite such successes, 1-bit quantization remains particularly challenging. A common strategy in 1-bit quantization is to determine binary weights by matching full-precision parameters, following a weight-driven criterion. However, this objective is not directly aligned with the quantized model's objective, which is to preserve the model's output behavior under the impact of quantization. A natural alternative is to adopt output-driven criteria that minimize discrepancies in model outputs using calibration data. Surprisingly, naive output-driven approaches often perform even worse in the 1-bit regime. In this paper, we show that this failure arises from two fundamental issues: error accumulation across layers and, more critically, anisotropic distortion of the representation space. Based on this observation, we introduce a geometry-preserving output-alignment framework for 1-bit LLM quantization. First, we formulate output alignment as a constrained optimization problem that improves reconstruction while explicitly controlling changes in token similarity, preventing reconstruction gains from being achieved at the expense of representation geometry. Second, we propose a geometry-aware salient-mask selection strategy that identifies quantization configurations according to their ability to preserve token relations, rather than relying solely on reconstruction error. These components enable effective output-driven optimization while retaining the structural information lost by naive alignment. Extensive experiments across multiple LLM families and downstream tasks demonstrate consistent improvements over existing 1-bit PTQ methods.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 8 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dung Anh Hoang, Cuong Pham, Cuong Nguyen, Trung le, Jianfei Cai, Thanh-Toan Do
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
