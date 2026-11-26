---
title: "Is 4 Bits Enough for EEG Sleep Staging? A Subject-Level Benchmark of MXFP4, NVFP4 and FP8"
description: "Staging sleep on a wearable device keeps the raw electroencephalogram (EEG) private and saves the energy needed to transmit it."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.31436) · [PDF](https://arxiv.org/pdf/2611.31436)

## 一句话摘要

Staging sleep on a wearable device keeps the raw electroencephalogram (EEG) private and saves the energy needed to transmit it.

## 为什么值得关注

待编辑增强。

## 摘要原文

Staging sleep on a wearable device keeps the raw electroencephalogram (EEG) private and saves the energy needed to transmit it. It also requires small, energy-efficient neural networks. We benchmark 13 post-training quantization (PTQ) configurations, from FP16 to the block-scaled 4-bit formats MXFP4 and NVFP4, for five-stage sleep staging from single-channel Fpz-Cz EEG. We use Sleep-EDF-78 (78 subjects), subject-wise cross-validation, three training seeds, value-exact emulation, and per-subject paired statistics. All 8- and 16-bit formats stay within 0.45 percentage points (pp) of FP32 Macro-F1. With 4-bit weights and activations, an epoch-wise CNN loses 1.98 to 3.04 pp, and a temporal-context network loses at most 1.19 pp. A same-encoder ablation shows that temporal context explains little of this gap. At equal block size, NVFP4 outperforms MXFP4. The first layer, which quantizes the raw EEG, is the most sensitive layer in both networks. Keeping the first and last layers in FP8 brings both tested 4-bit formats within 0.48 pp of FP32. This recipe adds at most 2.1% weight storage, needs no retraining, and is equivalent to quantization-aware training (QAT) within an exploratory 1-pp margin. The 4-bit losses fall on the same subjects across architectures (Spearman correlation coefficient = 0.69 to 0.79), and they reduce N3 recall the most. On the nested Sleep-EDF-20 subset, NVFP4 with FP8 first and last layers again stays within 0.25 pp of FP32. Under MXFP4, however, the ranking of the architectures reverses, and FP8 first and last layers do not fully recover two of the three tested models. In our emulation, NVFP4 with FP8 first and last layers thus loses little accuracy without QAT in both cohorts.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Emese Batizi, Hossein Valavi
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
