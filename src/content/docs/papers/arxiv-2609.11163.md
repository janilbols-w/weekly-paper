---
title: "LILA: Calibration-Free Structured Pruning of Large Language Models via Latent Spectral Geometry"
description: "Structured pruning of large language models (LLMs) offers hardware-efficient compression, yet existing methods require calibration data, gradient computation, or large auxiliary policy networks at pruning time."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.11163) · [PDF](https://arxiv.org/pdf/2609.11163)

## 一句话摘要

Structured pruning of large language models (LLMs) offers hardware-efficient compression, yet existing methods require calibration data, gradient computation, or large auxiliary policy networks at pruning time.

## 为什么值得关注

待编辑增强。

## 摘要原文

Structured pruning of large language models (LLMs) offers hardware-efficient compression, yet existing methods require calibration data, gradient computation, or large auxiliary policy networks at pruning time. LILA (\emph{Latent-Informed Layer Analysis}) scores neuron importance via the Kolmogorov--Smirnov (KS) distance between empirical singular value distributions of the full and neuron-ablated feed-forward network (FFN) weight matrix, providing a closed-form spectral rule requiring no training, calibration data, or auxiliary network. Without any fine-tuning, LILA surpasses PruneNet (45M-parameter RL policy) by 1.57~pp in zero-shot accuracy on LLaMA-2-7B at 25\% sparsity, and outperforms WikiText-2-calibrated SliceGPT by up to 6.0~pp across all sparsity levels, while preserving the original architecture. After one epoch of LoRA recovery fine-tuning, LILA achieves highly competitive performance, matching the heavily calibrated SliceGPT baseline to within a 0.48~pp margin across LLaMA-2-7B and Phi-2, despite using zero calibration data. A Neural Tangent Kernel analysis confirms a 22$\times$ reduction in functional distortion versus random pruning, providing theoretical grounding for the spectral importance criterion. Finally, extending LILA to dynamically allocate sparsity budgets via KS-scores yields state-of-the-art generative preservation at moderate compression, while uncovering fundamental single-layer architectural bottlenecks at higher compression regimes.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sankar Behera, Dhruv Singh, Anshika Agnihotri, Raj Kumar Choudhary, Satyadev Ahlawat, Yamuna Prasad
- 发布：2026-09-10；更新：2026-09-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
