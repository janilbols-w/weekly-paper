---
title: "LACE-SVD: Loss-Aware SVD with Cumulative Error Correction for LLM Compression"
description: "The rapid growth in the parameter scale of large language models (LLMs) has created a strong demand for efficient compression techniques."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.03057) · [PDF](https://arxiv.org/pdf/2607.03057)

## 一句话摘要

The rapid growth in the parameter scale of large language models (LLMs) has created a strong demand for efficient compression techniques.

## 为什么值得关注

待编辑增强。

## 摘要原文

The rapid growth in the parameter scale of large language models (LLMs) has created a strong demand for efficient compression techniques. As a hardware-agnostic and highly compatible approach, low-rank compression has been widely adopted to reduce both memory footprint and computational cost. However, existing SVD-based methods are still largely driven by local reconstruction objectives, overlooking two critical limitations: rank budgets are often allocated without explicitly considering layer-wise loss sensitivity, and local approximation errors can propagate and accumulate through the residual stream, leading to amplified global deviations from the original model. To address these issues, we propose LACE-SVD, a Loss-Aware SVD framework with Cumulative Error correction for LLM compression. LACE-SVD first estimates the calibration negative-log-likelihood increase induced by candidate layer-wise compression ratios and solves a budget-constrained allocation problem to assign rank budgets. It then refines the compressed model with closed-form local updates and introduces a propagation-aware correction for residual-stream output modules, reducing layer-output discrepancy as a proxy for cumulative error propagation. Experimental results demonstrate that at a high compression ratio (0.6), the WikiText-2 PPL of our method on LLaMA-7B (32.57) is significantly better than that of Dobi-SVD (46.18).

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: compressed model
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhuowen Liu, Longkun Hao, Shiyu Feng, Xiaowen Chang, Ruiqun Li, Changqun Li
- 发布：2026-08-18；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
