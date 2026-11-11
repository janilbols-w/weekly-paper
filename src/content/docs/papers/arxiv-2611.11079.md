---
title: "When Calibration Data Matter in Sub-4-Bit Language Model Quantization"
description: "Low-bit post-training quantization reduces language-model memory but can sharply degrade downstream task accuracy."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.11079) · [PDF](https://arxiv.org/pdf/2611.11079)

## 一句话摘要

Low-bit post-training quantization reduces language-model memory but can sharply degrade downstream task accuracy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Low-bit post-training quantization reduces language-model memory but can sharply degrade downstream task accuracy. Calibration usually relies on generic text, but when task-informed data recover accuracy and which quantizers benefit remain poorly understood. We introduce FragCal-DC, which supplements generic text with training documents from task families with low retention of full-precision accuracy in a two-bit scan. We use a two- to four-bit sweep to locate functional regimes and four-seed calibration comparisons to evaluate six data-dependent methods across six dense models (1.7B-8B) and ten tasks. At their lowest tested functional bit widths, iterative SignRound V2 and OmniQuant improve at two bits, whereas single-pass GPTQ and AWQ show small mean responses at three bits. At two bits, SignRound V2 gains 1.83 percentage points in mean ten-task accuracy over generic-text calibration across six models. At 70 billion parameters, GPTQ and SignRound V2 both improve at two bits, with functional generic-calibration baselines. For two-bit SignRound V2, task-level controls show that recovery concentrates on families included in calibration, while incorrect answer designations retain about 90% of the mean accuracy gain. Changes in reconstruction error do not consistently track accuracy gains. These findings support task-informed calibration as a design principle for preserving downstream accuracy in low-bit quantization.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yehong Jiang, Yen-Kuang Chen, Xinmin Tian
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
