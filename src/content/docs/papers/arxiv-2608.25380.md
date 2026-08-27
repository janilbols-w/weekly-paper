---
title: "APT: Accelerating Diffusion Transformers via Attention Probability-Guided Pruning and Quantization"
description: "Recent advances in generative AI have significantly increased the demand for high-resolution image and video generation, positioning diffusion models as a core technology."
---

**评分：54/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.25380) · [PDF](https://arxiv.org/pdf/2608.25380)

## 一句话摘要

Recent advances in generative AI have significantly increased the demand for high-resolution image and video generation, positioning diffusion models as a core technology.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent advances in generative AI have significantly increased the demand for high-resolution image and video generation, positioning diffusion models as a core technology. Among them, Diffusion Transformers (DiTs) have emerged as the state-of-the-art (SOTA) models due to their scalability and output quality. However, self-attention in DiTs incurs significant computational overhead, leading to excessively long latency as the complexity grows with the fourth power of the output resolution. While prior works have attempted to mitigate this cost using sparsity and quantization techniques, they fall short of effectively reducing the computational cost in high-resolution DiTs. In this paper, we present APT, a software-hardware co-designed accelerator for high-resolution DiTs. APT leverages attention probabilities as a unified importance metric to jointly optimize computation through fine-grained pruning and adaptive precision scaling. At the algorithm level, we propose Attention Probability-guided Adaptive Dual Thresholding (APDT), which dynamically performs element selection and precision assignment using dual thresholds. To ensure compatibility with memory-efficient FlashAttention, we introduce Timestep-Aware FlashAttention (TAFA), which predicts attention probabilities across timesteps by exploiting temporal similarity. At the architecture level, we co-design a specialized accelerator that efficiently supports irregular sparsity and dual-precision execution, featuring dynamic mask management, address translation, dual-precision compute units, and a tile-based dataflow. Finally, we evaluate APT on SOTA DiT models, including PixArt-$\alpha$, Stable Diffusion 3, and FLUX. APT achieves up to 8.16$\times$ speedup and 14.98$\times$ higher energy efficiency over NVIDIA A100, and up to 3.01$\times$ speedup and 2.04$\times$ higher energy efficiency over EXION, a SOTA diffusion model accelerator.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 17 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sungyeob Yoo, Seeyeon Kim, Joonyong Park, Seunghee Han, Joo-Young Kim
- 发布：2026-08-27；更新：2026-08-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
