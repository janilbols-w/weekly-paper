---
title: "What Does 4-Bit Microscaling Cost a Wearable Activity Recognizer?"
description: "Wearable sports sensors can recognize actions on the device itself, where lower-precision numbers reduce model storage and memory traffic."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.04185) · [PDF](https://arxiv.org/pdf/2611.04185)

## 一句话摘要

Wearable sports sensors can recognize actions on the device itself, where lower-precision numbers reduce model storage and memory traffic.

## 为什么值得关注

待编辑增强。

## 摘要原文

Wearable sports sensors can recognize actions on the device itself, where lower-precision numbers reduce model storage and memory traffic. Two 4-bit block-scaled formats, MXFP4 from the Open Compute Project, introduced in 2023, and NVFP4 from NVIDIA, introduced in 2025, are drawing interest. Published evaluations cover general deep-learning benchmarks and large language models; to our knowledge, nobody has yet measured what they cost a small wearable-sensor model. We train a 159,492-parameter 1D CNN to recognize four basketball actions from wrist-accelerometer data in Hang-Time HAR and test it on players it has never seen, using five-fold cross-validation grouped by player. Every comparison between number formats is made fold by fold. In full precision the model reaches 69.26\% macro-F1. Measured TFLite FP16 and INT8 models lose at most 0.16 percentage points. In simulation, 4-bit weights cost 1.45 points with MXFP4 and 0.72 points with NVFP4. When activations are quantized to 4 bits as well, MXFP4 loses 5.14 points and NVFP4 only 0.75, and NVFP4 comes out ahead in all five held-out-player folds. The ranking survives two alternative simulator settings, with NVFP4 leading by 3.49 to 4.40 points. A $2 \times 3$ ablation with 4-bit weights and activations (two block sizes and three scale rules) points to scale selection as the main source of MXFP4's loss. The reference MXFP4 conversion we simulate rounds the scale down, which can pick scales that are too small, so many blocks clip their largest values. Rounding the scale up recovers 3.18 points with 32-value blocks and 3.63 points with 16-value blocks, and switching to an 8-bit floating-point scale, as NVFP4 does, adds another 0.84 and 1.20 points. Block size matters less. Under this round-down rule, 16-value blocks score 0.44 points below 32-value blocks in all five folds; under the other two rules there is no consistent effect.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, microscaling, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Megan Healy, Hossein Valavi
- 发布：2026-11-04；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
