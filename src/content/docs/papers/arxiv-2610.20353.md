---
title: "Beyond Expert Rankings: Contrast Calibration for Mixed-Precision MoE Quantization"
description: "Mixture-of-experts (MoE) language models activate only a few experts per token, yet all expert weights must be stored."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.20353) · [PDF](https://arxiv.org/pdf/2610.20353)

## 一句话摘要

Mixture-of-experts (MoE) language models activate only a few experts per token, yet all expert weights must be stored.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-experts (MoE) language models activate only a few experts per token, yet all expert weights must be stored. Mixed-precision quantization reduces this storage cost by assigning higher bit-widths to sensitive experts and lower bit-widths to resilient ones, but expert rankings alone do not determine how strongly to weight their errors. To address this gap, we propose NatScale, a contrast-calibrated allocation framework for mixed-precision MoE quantization. It uses a model-specific power transformation to calibrate gradient-based expert weights to an information-theoretic contrast target while preserving rankings. We jointly evaluate each expert's gate, up and down configurations to estimate its output error. We then combine these errors and calibrated weights with an existing prior based on weight spectra, variance and precision decay to select configurations under a storage budget. Across three models, NatScale achieves the lowest native-to-quantized KL divergence and the highest top-token agreement in all nine settings against five allocation baselines. It also yields the lowest perplexity in seven settings. These findings highlight the importance of objective-aware precision allocation.

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

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Renjie Xie, Juncheng Yang, Aoting Hu, Yan Liang, Mingxi Zhang, Zheheng Hong, Wei Xu, Yanzhi Chen
- 发布：2026-10-14；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
