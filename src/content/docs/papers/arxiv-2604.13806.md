---
title: "Robust Ultra Low-Bit Post-Training Quantization via Stable Diagonal Curvature Estimate"
description: "Large Language Models (LLMs) are widely used across many domains, but their scale makes deployment challenging."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2604.13806) · [PDF](https://arxiv.org/pdf/2604.13806)

## 一句话摘要

Large Language Models (LLMs) are widely used across many domains, but their scale makes deployment challenging.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) are widely used across many domains, but their scale makes deployment challenging. Post-Training Quantization (PTQ) reduces memory footprint without retraining by leveraging a small calibration set. Recent Hessian-based PTQ methods compensate quantization error via cross-channel dependencies, but such approaches degrade at low bit-widths due to noisy curvature estimates from limited calibration data. We propose DASH-Q, a robust PTQ framework using diagonal Hessian approximation and iterative weighted least squares. By discarding noise-prone dependencies, DASH-Q filters sampling noise while prioritizing the preservation of salient feature power. We outperform other PTQ baselines in ultra low-bit regime, improving zero-shot accuracy by 7.01% on average and up to 14.01% over the strongest baselines across five baseline LLM models, while showing robust and stable performance with very small calibration data.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jaemin Kim, Sungkyun Kim, Junyeol Lee, Jiwon Seo
- 发布：2026-09-17；更新：2026-09-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
