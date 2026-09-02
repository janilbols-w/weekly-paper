---
title: "REAL-Q: E2E LLM Quantization via Dynamic Gradient Descent"
description: "Post-training quantization (PTQ) is essential for deploying large language models (LLMs) under strict resource constraints."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.00049) · [PDF](https://arxiv.org/pdf/2609.00049)

## 一句话摘要

Post-training quantization (PTQ) is essential for deploying large language models (LLMs) under strict resource constraints.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training quantization (PTQ) is essential for deploying large language models (LLMs) under strict resource constraints. State-of-the-art PTQ methods quantize each layer with a single closed-form second-order solver: to remain analytically tractable, they heavily approximate the global loss (dropping cross-channel coupling, pooling output rows into groups), and they then freeze the resulting Hessian across the entire layer, with no way to refresh it as the loss landscape shifts column by column--a phenomenon we call information misalignment. We propose REAL-Q (Real-time E2E-loss Aligned LLM Quantization), a novel PTQ paradigm that breaks this compromise: instead of diluting the objective for the sake of analytic tractability, REAL-Q targets an end-to-end-aligned surrogate of the global loss and refines it via fine-grained, dynamic Block-wise Gradient Descent applied after every column block (128 columns). By coupling this fine-grained correction with a sliding window mechanism for smooth cross-layer transitions, REAL-Q effectively mitigates error propagation across the network. On LLaMA-3.1 (8B and 70B) and Qwen3 (0.6B-32B) at W4A16, REAL-Q reduces end-to-end KL divergence by up to ~49% relative to state-of-the-art globally-guided methods.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qian Zhang, Yaoming Li, Zhewen Tan, Yanshu Wang, Heng Lu, Kun Su, Zongwei Lv, Wenhan Yu, Yongge Ma, Yinjun Han, Ruikuang Liu, Tong Yang
- 发布：2026-09-02；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
