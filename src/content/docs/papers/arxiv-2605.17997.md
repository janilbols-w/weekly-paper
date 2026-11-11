---
title: "MARR: Module-Adaptive Residual Reconstruction for Low-Bit Post-Training Quantization"
description: "Recently, residual reconstruction-based model quantization methods have achieved promising performance in low-bit Post-Training Quantization (PTQ) by introducing cross-module residuals to reduce error accumulated from previous modules."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2605.17997) · [PDF](https://arxiv.org/pdf/2605.17997)

## 一句话摘要

Recently, residual reconstruction-based model quantization methods have achieved promising performance in low-bit Post-Training Quantization (PTQ) by introducing cross-module residuals to reduce error accumulated from previous modules.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recently, residual reconstruction-based model quantization methods have achieved promising performance in low-bit Post-Training Quantization (PTQ) by introducing cross-module residuals to reduce error accumulated from previous modules. However, these residuals may also introduce additional bias arising from the Hessian-Approximation (HA) assumption, resulting their two-sided effect and potentially leading to suboptimal quantization performance. Therefore, in this work, we propose a residual regulation strategy to mitigate the HA bias associated with residual strength, while preserving accumulated-error correction. Furthermore, we observe that this two-sided effect is module-dependent, we futher propose a Module-Adaptive Residual Reconstruction (MARR), which assigns a module-specific scaling coefficient to adaptively balance accumulated-error correction and residual-related HA bias for each module. To avoid exhaustive per-module coefficient search and obtain a stable coefficient estimate, we design an Proportional-Integral-Derivative (PID)-based update strategy that employs reconstruction error as feedback to progressively refine this coefficient. Experiments on several typical Large Language Models (LLMs) and Vision Transformers (ViTs) demonstrate the effectiveness of MARR under low-bit quantization ($\leq$4-bit), achieving up to 20.2\% perplexity reduction on LLMs and up to 4.6\% accuracy gains on ViTs over the residual reconstruction baselines. Code will be made publicly available upon acceptance.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Le Su, Xing Luo, Zhi Jin
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
