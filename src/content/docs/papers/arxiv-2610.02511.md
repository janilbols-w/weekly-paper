---
title: "Post-Training Quantization of Autoregressive Weather Models"
description: "Advancements in high-resolution numerical weather prediction (NWP) and data assimilation (DA) have shaped the developments in deep learning (DL) architectures emulating atmospheric dynamics."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.02511) · [PDF](https://arxiv.org/pdf/2610.02511)

## 一句话摘要

Advancements in high-resolution numerical weather prediction (NWP) and data assimilation (DA) have shaped the developments in deep learning (DL) architectures emulating atmospheric dynamics.

## 为什么值得关注

待编辑增强。

## 摘要原文

Advancements in high-resolution numerical weather prediction (NWP) and data assimilation (DA) have shaped the developments in deep learning (DL) architectures emulating atmospheric dynamics. Emulators for weather forecasting exhibit forecast quality comparable to physics based models at forecast horizon scaling from few days to subseasonal time scales. The emulators are driven by hardware-accelerated matrix multiplication in autoregressive inferences, significantly reducing the computation time and resources required for NWP. Optimization of the matrix multiplication processes in GPU architectures provides opportunities to scale towards high-resolution domain, and offers implementation of out of the box solutions. Post-training quantization (PTQ) has been demonstrated across multiple DL architectures to accelerate and increase the number of computations in unit time while consuming less power, enabling applications on edge hardware. In this study, we investigate the effect of PTQ on pre-trained AI emulators for global-scale weather forecasting. We implement PTQ algorithms in Deep Learning Weather Prediction (DLWP) and FourCastNet (FCN) models as a proof of concept for geophysical fluid dynamics applications. We systematically investigate the effect of PTQ on emulator inferences over short-range forecast horizons. Evaluation of PTQ configurations using simulated quantization hints at qualitatively meaningful forecasts over short-time horizons. These results provide a first benchmark of PTQ for autoregressive weather emulators and a basis for quantization-based optimization of DL models for dynamical systems.

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

- 作者：Ananyo Bhattacharya, Swastik Bhattacharya, Christiane Jablonowski
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
