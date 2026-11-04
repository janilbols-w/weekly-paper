---
title: "Step-dLLM: Adaptive Step-aware Sparse Attention for Efficient Diffusion LLM Inference"
description: "Diffusion large language models (dLLMs) generate tokens in parallel via iterative denoising, but their bidirectional attention prevents the KV caching used by autoregressive models and recomputes the full attention map at every step, incurring quadratic per-step cost."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.01320) · [PDF](https://arxiv.org/pdf/2611.01320)

## 一句话摘要

Diffusion large language models (dLLMs) generate tokens in parallel via iterative denoising, but their bidirectional attention prevents the KV caching used by autoregressive models and recomputes the full attention map at every step, incurring quadratic per-step cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion large language models (dLLMs) generate tokens in parallel via iterative denoising, but their bidirectional attention prevents the KV caching used by autoregressive models and recomputes the full attention map at every step, incurring quadratic per-step cost. Existing sparse attention methods for dLLMs construct a sparse mask after an initial full-attention warm-up and reuse it for the remaining steps, while allocating the sparsity budget uniformly across heads. We argue both choices ignore key structural properties of attention in dLLMs: empirically, attention patterns are only locally consistent across steps and shift abruptly at certain transitions, and different heads concentrate their attention mass to very different extents. To this end, we design Step-dLLM, which periodically refreshes a block-sparse mask at anchor steps along the denoising trajectory and reuses it within each locally consistent interval, while employing a head-adaptive global budget that more aggressively compresses heads with concentrated attention. Backed by a fused IO-aware Triton kernel for block-sparse attention, Step-dLLM applies to pre-trained LLaDA-1.5 and Dream-7B-Instruct without retraining, achieving a 2.78x end-to-end speedup over dense FlashAttention on LLaDA-1.5 at 8K context with 256 denoising steps and 90% sparsity, while improving the accuracy-latency trade-off over prior sparse-attention methods.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zhichen Zeng, Xichong Zhang, Junpan Wu, Yifei Zuo, Chi-Chih Chang, Jiayi Wang, Maohua Nie, Ji Liu, Ang Li, Banghua Zhu
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
