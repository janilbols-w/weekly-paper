---
title: "Neural Dimensional Analysis: Foundations of Dimensionless and Scale-Consistent Computation"
description: "Modern Transformers rely on many scale-control mechanisms, including normalization, residual scaling, attention temperatures, loss weighting, and adaptive updates."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2610.17969v1) · [PDF](https://arxiv.org/pdf/2610.17969v1)

## 一句话摘要

Modern Transformers rely on many scale-control mechanisms, including normalization, residual scaling, attention temperatures, loss weighting, and adaptive updates.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern Transformers rely on many scale-control mechanisms, including normalization, residual scaling, attention temperatures, loss weighting, and adaptive updates. To explain how these mechanisms maintain scale consistency, we introduce Neural Dimensional Analysis (NDA), a unified framework based on dimensional consistency. We define neural units that specify how tensors rescale and which quantities can be added, just as physical units do in physics. Our rules match residual units, nondimensionalize attention and gate inputs, combine losses across units, and convert gradient units into parameter units. We implement NDA through dimensionless Unit Violation Indices (UVI) for diagnosing scale mismatches within Transformers, a unit-consistent multi-loss objective, and the Gauge-Canonical Transformer (GCT) with normalized coordinates and orthogonalized residual additions. In language-model experiments spanning 51M to 1B parameters, GCT remains stable during training across a broad sixteenfold learning-rate range, outperforming Pre-LN, LLaMA-style, and QK-Norm in 124M validation loss at tuned learning rates. GCT's normalized residual stream also shows improved robustness to quantization. At 1B parameters, calibrated per-tensor int8 quantization increases GCT's validation loss by only 0.009 nats, compared with up to 5.51 nats for the baselines. Vision and physics-informed neural network experiments further confirm NDA's benefits beyond language modeling. These results establish dimensional consistency as a neural network design principle.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Bum Jun Kim, Makoto Kawano, Yusuke Iwasawa, Yutaka Matsuo
- 发布：2026-10-13；更新：2026-10-13
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
