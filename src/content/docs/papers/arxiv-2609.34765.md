---
title: "Beyond Reconstruction Loss in Post-Training Quantization: Balanced Fitting for Large Vision-Language Models"
description: "Post-training quantization (PTQ) enables efficient deployment of large vision-language models (LVLMs), but is typically calibrated on a small set while expected to generalize across diverse downstream tasks."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.34765) · [PDF](https://arxiv.org/pdf/2609.34765)

## 一句话摘要

Post-training quantization (PTQ) enables efficient deployment of large vision-language models (LVLMs), but is typically calibrated on a small set while expected to generalize across diverse downstream tasks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training quantization (PTQ) enables efficient deployment of large vision-language models (LVLMs), but is typically calibrated on a small set while expected to generalize across diverse downstream tasks. Although recent PTQ methods for LVLMs incorporate sensitivity signals, they still minimize reconstruction loss with respect to the full-precision model, potentially over-preserving FP behavior and calibration-specific bias. Rather than treating quantization solely as an error to be minimized, we observe that it can also provide beneficial regularization for certain layers and modalities. Motivated by this observation, we propose Balanced Fitting, a quantization effect-based framework that balances precision and regularization beyond reconstruction-based optimization. By measuring layer- and component-wise quantization effects for weights, vision activations, and text activations, Balanced Fitting combines fine-grained fitting for sensitive components with coarser fitting to exploit potential regularization benefits. Experiments on multiple LVLMs show that our method consistently outperforms prior PTQ approaches under both weight-only and weight-activation quantization, while lower reconstruction loss does not reliably translate into better downstream performance. The source code is publicly available at https://github.com/kmc3661/BFQ

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Minchan Kang, Kyeonghye Park, Seungyeon Sa, Seoyoung Cho, Daeshik Kim, Yucheol Cho
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/kmc3661/BFQ](https://github.com/kmc3661/BFQ)
- 阅读深度：metadata
