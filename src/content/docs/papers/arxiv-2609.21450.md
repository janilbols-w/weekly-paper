---
title: "Understanding LLM Quantization through Activation-Guided Compensation and Orthogonal Residuals"
description: "Post-training weight-activation quantization reduces the memory and inference costs of large language models, but aggressive W4A4 quantization remains difficult because activation outliers degrade effective quantization resolution."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.21450) · [PDF](https://arxiv.org/pdf/2609.21450)

## 一句话摘要

Post-training weight-activation quantization reduces the memory and inference costs of large language models, but aggressive W4A4 quantization remains difficult because activation outliers degrade effective quantization resolution.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training weight-activation quantization reduces the memory and inference costs of large language models, but aggressive W4A4 quantization remains difficult because activation outliers degrade effective quantization resolution. Although weight optimization, channel-wise scaling, and orthogonal rotation mitigate this problem, the error components they address and their relationship remain unclear. Using an exact decomposition of local weight-activation quantization error into an activation-guided weight compensation term and an orthogonal residual, we bound the residual using persistent channel-wise outlier and regular activation quantities. This decomposition clarifies which error components can be addressed by weight compensation and which require transformation design. We then use the residual bounds to derive practical guidelines for applying randomized Hadamard rotation, sign selection, and channel scaling. In particular, the analysis explains how random signs suppress constructive interference among persistent outlier channels, how sampling multiple sign patterns can improve transformation selection, and how second-moment balancing leads to an $L_2$ scaling rule while a further relaxation recovers SmoothQuant-style $L_\infty$ scaling. We evaluate these guidelines through backpropagation-free configurations across eight Llama and Mistral models, obtaining performance competitive with gradient-trained SpinQuant.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yamato Narita, Issei Sato
- 发布：2026-09-21；更新：2026-09-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
