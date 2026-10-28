---
title: "Self-Regularized Flow Language Models"
description: "We introduce SERF (Self-Regularized Flow Language Models), a simple self-supervised framework for improving continuous diffusion language models by exploiting the denoising trajectory itself."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.37115) · [PDF](https://arxiv.org/pdf/2610.37115)

## 一句话摘要

We introduce SERF (Self-Regularized Flow Language Models), a simple self-supervised framework for improving continuous diffusion language models by exploiting the denoising trajectory itself.

## 为什么值得关注

待编辑增强。

## 摘要原文

We introduce SERF (Self-Regularized Flow Language Models), a simple self-supervised framework for improving continuous diffusion language models by exploiting the denoising trajectory itself. While continuous flow-based language models offer a promising alternative to autoregressive generation, their training objectives typically rely on supervision from clean target tokens, leaving the denoising trajectory underexploited as a learning signal. SERF addresses this limitation through noisy-to-clean self-distillation: an exponential moving average (EMA) teacher receives a cleaner version of the student's noisy input along the same interpolation path and provides additional supervision. We investigate two variants: SERF-L, which aligns the student's intermediate representations with deeper teacher representations, and SERF-P, which aligns their output token distributions, either at the student's output or at an early student layer. All variants augment the standard training objective without requiring external pretrained models or modifying the inference procedure. Experiments across three continuous language-model paradigms (one-hot FLM, latent ELF, and hyper-spherical S-FLM) demonstrate substantial improvements in training efficiency, generation quality, and few-step generation. In particular, SERF achieves up to 7.7x wall-clock training acceleration on OpenWebText, improves MAUVE by 24.3% and GSM8K accuracy by up to 28.8%, and matches baseline performance with up to 64x fewer sampling steps. These results establish noisy-to-clean self-distillation as an effective approach to improving continuous diffusion language models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Theodoros Kouzelis, Spyros Gidaris, Nikos Komodakis
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
