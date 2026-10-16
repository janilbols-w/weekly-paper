---
title: "SARATHI: Decoupled Data-Free Probing and Adaptive Reconstruction for Structured LLM Pruning"
description: "Structured pruning reduces the inference cost of large language models (LLMs) by permanently removing neurons and weight rows, yielding dense, hardware-agnostic speedup."
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](http://arxiv.org/abs/2610.15514v1) · [PDF](https://arxiv.org/pdf/2610.15514v1)

## 一句话摘要

Structured pruning reduces the inference cost of large language models (LLMs) by permanently removing neurons and weight rows, yielding dense, hardware-agnostic speedup.

## 为什么值得关注

待编辑增强。

## 摘要原文

Structured pruning reduces the inference cost of large language models (LLMs) by permanently removing neurons and weight rows, yielding dense, hardware-agnostic speedup. Existing post-training methods couple neuron selection and weight reconstruction through a shared calibration dataset, introducing domain bias and out-of-memory failures at high sparsity. We propose SARATHI, a framework that decouples these two stages. A data-free \emph{NMF Residual Subspace Probe} scores neurons using intrinsic weight geometry, without accessing any calibration data, and carries a formal connection to Robust PCA. \emph{Adaptive OBS} then reconstructs the pruned weights with a localized calibration batch, operating in $\mathcal{O}(d^2)$ peak memory per layer and eliminating the global memory bottleneck of coupled methods. A \emph{Bias Shift Compensation} step corrects systematic activation drift in post-LayerNorm architectures that would otherwise cause perplexity collapse at high sparsity. Experiments across six models from two architecture families (gated and non-gated FFN) at 15--40\% sparsity show that SARATHI achieves competitive perplexity and matches or exceeds existing structured pruning baselines on zero-shot accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sankar Behera, Dhruv Singh, Satyadev Ahlawat, Yamuna Prasad
- 发布：2026-10-11；更新：2026-10-11
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
