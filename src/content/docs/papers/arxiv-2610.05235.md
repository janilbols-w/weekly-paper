---
title: "EMG-GPT: Predictive Pretraining on Residual-Quantized EMG Tokens for Hand Pose Estimation"
description: "Surface electromyography (sEMG) is a low-power, cost-effective biosignal for hand-pose estimation and gesture classification."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.05235) · [PDF](https://arxiv.org/pdf/2610.05235)

## 一句话摘要

Surface electromyography (sEMG) is a low-power, cost-effective biosignal for hand-pose estimation and gesture classification.

## 为什么值得关注

待编辑增强。

## 摘要原文

Surface electromyography (sEMG) is a low-power, cost-effective biosignal for hand-pose estimation and gesture classification. In this work, we examine whether self-supervised pretraining on sEMG can yield transferable representations for continuous hand-pose estimation. We introduce EMG-GPT, a causal transformer-based model that operates on discrete sEMG representations from a frozen residual vector quantization (RVQ) tokenizer and learns temporal dynamics through depth-autoregressive future-code prediction. The model combines within-frame integration with causal temporal modeling while preserving the geometry of the pretrained codebook. EMG-GPT shows competitive results in both Regression and Tracking tasks, supporting EMG-only pretraining as a viable approach for learning transferable sEMG representations.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ettore Magni, Rolandos Alexandros Potamias, Stefanos Zafeiriou, Konstantinos Barmpas
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
