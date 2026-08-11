---
title: "Full-Stack FP4: Stable LLM Pretraining with Quantized Projections, Optimizers, and Attention"
description: "Recent NVFP4 pretraining work has primarily optimized Transformer linear projections, leaving persistent optimizer states, optimizer computation, and low-precision attention forward--backward paths less explored."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2607.04422) · [PDF](https://arxiv.org/pdf/2607.04422)

## 一句话摘要

Recent NVFP4 pretraining work has primarily optimized Transformer linear projections, leaving persistent optimizer states, optimizer computation, and low-precision attention forward--backward paths less explored.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent NVFP4 pretraining work has primarily optimized Transformer linear projections, leaving persistent optimizer states, optimizer computation, and low-precision attention forward--backward paths less explored. We present \textbf{Full-Stack FP4}, a modular NVFP4 framework with separate recipes for projections, AdamW states, Root/Muon computation, and attention. \textbf{LoRA-SVD} protects a compact projection subspace in BF16 while retaining full-shape NVFP4 computation, reducing the linear-only loss gap from \textbf{1.40\%} to \textbf{0.61\%}. An ordered square-root, tile-mean, and Hadamard pipeline enables stable NVFP4 AdamW momentum storage; shape-dependent coefficients and clipping stabilize direct NVFP4 Root iterations; and mixed-precision attention retains softmax-sensitive operations in BF16. On 3B pretraining with 64B tokens, BF16 and Full-Stack FP4 reach losses of \textbf{2.267} and \textbf{2.286}, a \textbf{0.838\%} gap. Their average zero-shot perplexities are 26.675 and 26.665, respectively, with Full-Stack FP4 averaging 0.10 percentage points lower in accuracy. Native four-block measurements on one RTX 5090 show 2.50--2.83$\times$ Root speedups over optimized BF16 and 37.9--42.5\% lower AdamW peak memory.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Siyu Ding, Mingchuan Ma, Jiabo Tong, Xingrun Xing, Ziming Wang, Guoqi Li
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
