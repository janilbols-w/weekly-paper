---
title: "CoS-VQ: Coordinated Shared-Scale Vector Quantization for Large Language Models"
description: "Large language models (LLMs) require substantial memory, motivating low-bit weight quantization for efficient deployment."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.37336) · [PDF](https://arxiv.org/pdf/2610.37336)

## 一句话摘要

Large language models (LLMs) require substantial memory, motivating low-bit weight quantization for efficient deployment.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) require substantial memory, motivating low-bit weight quantization for efficient deployment. Existing vector quantization (VQ) methods often improve accuracy by increasing the effective coding dimension, which can complicate independent lookup and local codeword updates. We propose CoS-VQ (Coordinated Shared-Scale Vector Quantization), which preserves low-dimensional codewords while jointly optimizing hard indices and their shared scale across positions. The key challenge is scale-induced coupling: the optimal scale depends on the entire codeword combination and, in turn, changes candidate rankings across positions, so pointwise updates can stall even after scale re-optimization. CoS-VQ collects candidates at multiple probe scales and constructs a tangent separable upper bound for the residual-aware quadratic objective. By reducing candidate comparisons to lower envelopes of lines over positive scales, it identifies finitely many representative intervals for joint index--scale updates without exhaustively enumerating codeword combinations. On Qwen3.8-27B, CoS-VQ outperforms QTIP and LLVQ on the evaluated language modeling, coding, and reasoning benchmarks. Ablations from the same initialization further show larger gains from joint updates than from scale-only refinement, highlighting joint selection as an alternative to increasing codeword dimensionality. The code is available at https://github.com/xzktx003/Cos_VQ.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zukang Xu, Zhixiong Zhao, Xing Hu, Zhe Jiang, Xin Si, Dawei Yang
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/xzktx003/Cos_VQ](https://github.com/xzktx003/Cos_VQ)
- 阅读深度：metadata
