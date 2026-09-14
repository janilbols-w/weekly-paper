---
title: "LC-QAT: Data-Efficient 2-Bit QAT for LLMs via Linear-Constrained Vector Quantization"
description: "Quantization-aware training (QAT) is essential for extremely low-bit large language models (LLMs)."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2606.10531) · [PDF](https://arxiv.org/pdf/2606.10531)

## 一句话摘要

Quantization-aware training (QAT) is essential for extremely low-bit large language models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Quantization-aware training (QAT) is essential for extremely low-bit large language models (LLMs). Current QAT methods are mainly based on scalar quantization (SQ), which enables efficient optimization but suffers from severe performance degradation at 2-bit precision. On the other hand, vector quantization (VQ) provides substantially higher representational capacity, but its discrete codebook lookup prevents end-to-end training. We propose LC-QAT, a 2-bit weight-only VQ-QAT framework that represents quantized weights via a learned affine mapping over discrete vectors, which yields a high-quality PTQ initialization and enables fully differentiable end-to-end optimization without explicit codebook lookup in the training forward pass. This strong post-training initialization makes LC-QAT highly data-efficient. Experiments across diverse LLMs demonstrate that LC-QAT consistently outperforms state-of-the-art QAT methods while using only 0.1%--10% of the training data. Our results establish LC-QAT as a practical and scalable solution for extreme low-bit model deployment. Codes are publicly available at https://github.com/AI9Stars/UniSVQ.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Haoyu Wang, Xingyu Yu, Haiyan Zhao, Fengxiang Wang, Xu Han
- 发布：2026-09-14；更新：2026-09-14
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/AI9Stars/UniSVQ](https://github.com/AI9Stars/UniSVQ)
- 阅读深度：metadata
