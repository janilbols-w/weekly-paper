---
title: "Decomposition-Guided Diffusion Language Models for Inertial Confinement Fusion Prediction"
description: "Inertial confinement fusion (ICF) is a leading pathway toward clean energy, but each shot at the National Ignition Facility costs on the order of one million dollars, making accurate AI surrogates a high-value target."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.07756) · [PDF](https://arxiv.org/pdf/2609.07756)

## 一句话摘要

Inertial confinement fusion (ICF) is a leading pathway toward clean energy, but each shot at the National Ignition Facility costs on the order of one million dollars, making accurate AI surrogates a high-value target.

## 为什么值得关注

待编辑增强。

## 摘要原文

Inertial confinement fusion (ICF) is a leading pathway toward clean energy, but each shot at the National Ignition Facility costs on the order of one million dollars, making accurate AI surrogates a high-value target. We study exogenous-driven ICF waveform prediction, where a 512-step neutron-rate diagnostic must be inferred directly from a laser pulse and target design parameters, with no historical response observed. The regime stresses standard time-series predictors with temporal sparsity (picosecond peak in a nanosecond window), input-output scale mismatch (under 300 real shots), and peak sensitivity (picosecond timing). We propose ICF-DLM, to our knowledge the first LM-based ICF predictor, combining (i) a physics-typed decomposition into yield $Y_{DT}$, peak timing $t_{\mathrm{peak}}$, and local waveform $w_{\mathrm{local}}$; (ii) bidirectional denoising that defers commitment to peak location; and (iii) a physics-driven PPO reward re-injecting metric structure across numeric tokens. On ICFBench (50K simulations + 232 experimental shots), ICF-DLM cuts peak-timing error from 11.6 to 9.2 steps over a matched autoregressive LLaMA-3-8B and outperforms classical sequence models and LLM-based time-series predictors. Beyond ICF, the recipe shows potential to address science domains with low data and sparse events.

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

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xiang Zhang, Varchas Gopalaswamy, Rahman Ejaz, Riccardo Betti, Dongfang Liu
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
