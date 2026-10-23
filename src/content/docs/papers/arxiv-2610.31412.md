---
title: "SQuAT: Spherical Lattice Vector Quantization-Aware Training"
description: "Vector quantization (VQ), in particular lattice-based methods, offer strong rate-distortion trade-offs for low-bit large language models (LLMs), yet their behavior under quantization-aware training (VQ-QAT) remains poorly understood."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.31412) · [PDF](https://arxiv.org/pdf/2610.31412)

## 一句话摘要

Vector quantization (VQ), in particular lattice-based methods, offer strong rate-distortion trade-offs for low-bit large language models (LLMs), yet their behavior under quantization-aware training (VQ-QAT) remains poorly understood.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vector quantization (VQ), in particular lattice-based methods, offer strong rate-distortion trade-offs for low-bit large language models (LLMs), yet their behavior under quantization-aware training (VQ-QAT) remains poorly understood. We scale lattice VQ-QAT to billion-parameter LLMs and multi-billion-token training regimes, and introduce SQuAT, a shape-gain VQ-QAT approach trained with a separate straight-through estimator (STE) for the shape and gain. SQuAT decomposes weights into direction and magnitude: normalized directions are quantized using an $E_8$-derived spherical codebook, while gains are quantized independently with low-bit scalar quantizers. We show that, unlike a standard STE applied to the full quantizer, which ignores the shape-gain structure, these separate STEs induce tangent-space updates for directions, yielding an implicit form of spherical (Riemannian) optimization. To enable scalability, we develop a distributed exact nearest-neighbor assignment scheme, in which workers quantize disjoint weight blocks and communicate only discrete indices, reducing VQ-QAT training time by 12.8$\times$ and allowing us to scale it to 10B tokens. Across instruction-tuned LLaMA-3.2-1B/3B, Qwen3-4B, and base Qwen3-1.7B, SQuAT consistently outperforms standard VQ-QAT STE under identical quantizers and initialization, and achieves SOTA VQ-QAT accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sebastian Loeschcke, Ivan Koryakovskiy, Tycho F. A. van der Ouderaa, Riccardo Del Chiaro, Mart van Baalen, Paul N. Whatmough, Markus Nagel
- 发布：2026-10-23；更新：2026-10-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
