---
title: "LinearARD: Linear-Memory Attention Distillation for RoPE Restoration"
description: "The extension of context windows in Large Language Models is typically facilitated by scaling positional encodings followed by Continued Pre-Training (CPT)."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2604.00004) · [PDF](https://arxiv.org/pdf/2604.00004)

## 一句话摘要

The extension of context windows in Large Language Models is typically facilitated by scaling positional encodings followed by Continued Pre-Training (CPT).

## 为什么值得关注

待编辑增强。

## 摘要原文

The extension of context windows in Large Language Models is typically facilitated by scaling positional encodings followed by Continued Pre-Training (CPT). While effective, this paradigm is notoriously data-hungry and computationally expensive, requiring massive long-text corpora to recalibrate the model to the shifted positional distribution. We propose LinearARD, a restoration distillation method that restores Rotary Position Embedding (RoPE)-scaled students through attention-structure consistency with a frozen native-RoPE teacher. Rather than next-token prediction or opaque hidden-state matching, LinearARD aligns row-wise distributions of dense $Q/Q$, $K/K$, and $V/V$ self-relation matrices from the final attention layer to directly supervise attention dynamics. To remove the quadratic memory bottleneck of $n \times n$ relation maps, we introduce a linear-activation-memory kernel that stores only per-token log-sum-exp statistics and recomputes logits in the backward pass to obtain exact Kullback-Leibler divergence gradients. Across LLaMA2-7B, LLaMA3-8B, and Mistral-7B-v0.1 extended to 32K context, LinearARD recovers 93.1%/94.2%/94.3% of native short-context performance and achieves strong long-context robustness on RULER using only 4.25M tokens---amounting to just 1.6% (a $\sim$60$\times$ reduction) of the 256M-token budget required by state-of-the-art baselines. Under this severely constrained budget, CPT and LongReD remain near zero on RULER, demonstrating that relation-level restoration provides a substantially better efficiency-quality tradeoff. Our code is available at https://github.com/gracefulning/LinearARD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Ning Yang, Hengyu Zhong, Wentao Wang, Baoliang Tian, Yuan Zhou, Haijun Zhang, Jun Wang
- 发布：2026-10-27；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/gracefulning/LinearARD](https://github.com/gracefulning/LinearARD)
- 阅读深度：metadata
