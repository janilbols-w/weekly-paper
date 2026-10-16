---
title: "FidelityQ: Preserving Predictive Fidelity in Ultra-Low-Bit Language Model Quantization"
description: "Ultra-low-bit scalar quantization offers a regular arithmetic structure for efficient deployment of large language models, but preserving predictive behavior at extreme precision remains challenging: with only a few reconstruction levels, accurate weight representation must translate into consistent predictions from a small calibration set."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2610.14934v1) · [PDF](https://arxiv.org/pdf/2610.14934v1)

## 一句话摘要

Ultra-low-bit scalar quantization offers a regular arithmetic structure for efficient deployment of large language models, but preserving predictive behavior at extreme precision remains challenging: with only a few reconstruction levels, accurate weight representation must translate into consistent predictions from a small calibration set.

## 为什么值得关注

待编辑增强。

## 摘要原文

Ultra-low-bit scalar quantization offers a regular arithmetic structure for efficient deployment of large language models, but preserving predictive behavior at extreme precision remains challenging: with only a few reconstruction levels, accurate weight representation must translate into consistent predictions from a small calibration set. We propose FidelityQ, a scalar quantization framework that preserves predictive fidelity at weight precisions down to 2 bits. For accurate quantization, we introduce Information-Aligned Analytic Coding (IAC), which shapes each weight row toward a centered symmetric source via randomized Hadamard mixing and fits a mirrored four-level minimum-distortion quantizer to its empirical weights. Every level set in this family decomposes exactly into two sign-valued bases with associated scales, combining source-adaptive reconstruction with lookup-free decoding compatible with scaled integer arithmetic. Our analysis further shows that residual predictive discrepancies are heavy-tailed and concentrate on tokens the teacher predicts confidently, motivating Knowledge-Intensive Calibration (KIC) for consistent quantization. KIC ranks sequences by the tail of token-wise teacher-student divergence, allocates a limited calibration budget to the highest-scoring samples, and restores predictive agreement by updating only quantization levels and scales under teacher supervision, keeping pretrained weights frozen. Experiments on the LLaMA and Qwen families demonstrate the effectiveness of FidelityQ in weight-only and joint quantization settings. On LLaMA-2-7B, FidelityQ achieves a WikiText2 perplexity of 6.62 at W2A16 and improves the prior state-of-the-art W2A4KV4 result from 8.31 to 6.96, while reducing linear-layer weight memory by 8.0x relative to FP16.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yujie Chen, Weiyan Zheng, Yiwu Yao, Tianchi Hu, Bo Wang, Jiyu Guo, Wenzhan Li, Jingcai Guo, Michele Magno, Haotong Qin
- 发布：2026-10-10；更新：2026-10-10
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
