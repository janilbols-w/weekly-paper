---
title: "Pushing Toward the Simplex Vertices: A Simple Remedy for Code Collapse in Smoothed Vector Quantization"
description: "Vector quantization, which discretizes a continuous vector space into a finite set of representative vectors (a codebook), has been widely adopted in modern machine learning."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2509.22161) · [PDF](https://arxiv.org/pdf/2509.22161)

## 一句话摘要

Vector quantization, which discretizes a continuous vector space into a finite set of representative vectors (a codebook), has been widely adopted in modern machine learning.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vector quantization, which discretizes a continuous vector space into a finite set of representative vectors (a codebook), has been widely adopted in modern machine learning. Despite its effectiveness, vector quantization poses a fundamental challenge: the non-differentiable quantization step blocks gradient backpropagation. Smoothed vector quantization addresses this issue by relaxing the discrete selection of a codebook vector into a weighted combination of codebook entries, represented as the matrix product of a simplex vector and the codebook. Effective smoothing requires two properties: (1) smoothed code-selection vectors should remain close to a onehot vector, ensuring tight approximation, and (2) all codebook entries should be utilized, preventing code collapse. Existing methods typically address these desiderata separately. By contrast, the present study introduces a simple and intuitive regularization that promotes both simultaneously by minimizing the distance between each simplex vertex and its $K$-nearest smoothed code-selectors. Representative benchmarks on image encoding demonstrate that the proposed method achieves more effective codebook utilization and improves performance over prior approaches.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Takashi Morita
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
