---
title: "HRTF Upsampling and Personalization via Neural Operators"
description: "Head-related transfer function (HRTF) spatial upsampling from sparse measurements is a fundamental challenge in personalized binaural audio."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.20400) · [PDF](https://arxiv.org/pdf/2610.20400)

## 一句话摘要

Head-related transfer function (HRTF) spatial upsampling from sparse measurements is a fundamental challenge in personalized binaural audio.

## 为什么值得关注

待编辑增强。

## 摘要原文

Head-related transfer function (HRTF) spatial upsampling from sparse measurements is a fundamental challenge in personalized binaural audio. We formulate HRTF upsampling as an operator learning problem and introduce SPARO, a neural operator that maps sparse measurements at a set of spatial directions to the HRTF field, a continuous representation that can be queried at arbitrary positions. SPARO projects the measurements onto a learned set of spherical latent modes, processes the latent modes with Transformer blocks, and decodes the resulting representations at query directions. On SONICOM, using the LAP24 measurement configuration, SPARO attains the best log-spectral distortion (LSD) and interaural level difference (ILD) error at every sparsity level from 3 to 100 measurements (18% lower LSD and 43% lower ILD error than the strongest baseline at 100 measurements) while remaining competitive in interaural time difference (ITD) error. It reconstructs a dense HRTF 15 to 373 times faster than the leading neural-field method RANF. We further validate the approach on HUTUBS, demonstrating its effectiveness across HRTF datasets.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Meenakshi Krishnan, You Zhang, Ramani Duraiswami, C. Phillip Brown
- 发布：2026-10-15；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
