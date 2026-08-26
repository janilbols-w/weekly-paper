---
title: "The Impact of Temporal Context Length and Encoding Strategies on Self-Supervised ECG Representation Learning"
description: "Self-supervised electrocardiogram (ECG) models are often trained on a few seconds of ECG signal and, increasingly, on discretized token sequences."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.12695) · [PDF](https://arxiv.org/pdf/2608.12695)

## 一句话摘要

Self-supervised electrocardiogram (ECG) models are often trained on a few seconds of ECG signal and, increasingly, on discretized token sequences.

## 为什么值得关注

待编辑增强。

## 摘要原文

Self-supervised electrocardiogram (ECG) models are often trained on a few seconds of ECG signal and, increasingly, on discretized token sequences. It remains unclear whether these choices sacrifice information needed for rhythm inference and longitudinal consistency in real-world ambulatory recordings. We present a controlled study on the Icentia11k single-lead dataset that varies (i) the input horizon (16 seconds, 1 minute, 5 minutes, and 10 minutes) and (ii) the front-end representation (continuous convolutional patch embeddings vs. fixed vector-quantized tokens), while holding the Transformer backbone and training protocol constant. Representations are assessed by downstream abnormal rhythm detection and by patient-level retrieval that probes cross-session stability. Our results show that increasing temporal context beyond 16-second snapshots yields stronger transfer and higher retrieval accuracy, with the strongest performance achieved by the 5- and 10-minute models, indicating improved capture of slow-varying rhythm dynamics and individual-specific structure. Across all evaluated horizons, continuous patch embeddings outperform discretized tokens, suggesting that quantization can discard clinically relevant waveform detail. These findings motivate ECG foundation models that emphasize extended context and continuous encoders for clinical prediction and similarity-based applications. Our code and pretrained models are publicly available at https://github.com/muha-0/ecg-ssl-representation-learning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Ahmed Sameh, Ramzi Al-Sharawi, Yogatheesan Varatharajah
- 发布：2026-08-13；更新：2026-08-26
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/muha-0/ecg-ssl-representation-learning](https://github.com/muha-0/ecg-ssl-representation-learning)
- 阅读深度：metadata
