---
title: "On-Policy Residual Learning for Diffusion Language Models"
description: "Residual context is key to unlocking the speed-quality Pareto frontier of diffusion language models (DLMs) by carrying forward predictive distributions across denoising steps."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.20687) · [PDF](https://arxiv.org/pdf/2610.20687)

## 一句话摘要

Residual context is key to unlocking the speed-quality Pareto frontier of diffusion language models (DLMs) by carrying forward predictive distributions across denoising steps.

## 为什么值得关注

待编辑增强。

## 摘要原文

Residual context is key to unlocking the speed-quality Pareto frontier of diffusion language models (DLMs) by carrying forward predictive distributions across denoising steps. Yet turning this seemingly simple mechanism into an effective learning paradigm is far from simple: there is no clear recipe for how residual context should be learned. We introduce ORL, a framework for on-policy residual learning in DLMs. Algorithmically, we identify that residual learning is inherently on-policy. ORL learns from model-induced residual trajectories on the fly and introduces an entropy-contraction objective that sharpens predictions as the model revisits its own predictions. System-wise, exact residual supervision requires capturing, retaining, and reprocessing many trajectory-dependent states. ORL co-designs the algorithm with asynchronous residual capture and transport, specialized block-diffusion attention, and packed compute-balanced training, making it practical at scale. On a 4B DLM converted from Qwen3-4B, ORL improves tokens per forward (TPF) by up to 6.2x and, with our dlmrt engine, end-to-end throughput by approximately 6.9x at comparable or better quality. In single-request serving on one H100, this mode achieves a stronger speed-quality Pareto frontier than autoregressive models with EAGLE3 and DFlash speculative decoding under both strict and relaxed verification, running 1.74x faster than DFlash at matched accuracy. ORL also transfers to existing DLMs: on LLaDA-2.1-mini, 36 H100-hours and 4.2M self-generated tokens, about 10x less data than prior LLaDA recipes, yield up to 1.5x higher TPF and up to 3x higher throughput at comparable quality, and on DiffusionGemma, ORL raises TPF by 1.1-1.2x. With dlmrt and NVFP4 quantization, ORL models decode a single request at up to 5,046 tokens/s on one B200, 7,708 on eight B200s, and 2,788 on a consumer RTX 5090, with comparable quality.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yifan Yu, Yuqing Jian, Jisen Li, Yuezhou Hu, Tianyi Zhang, Xiaoxia Wu, Rui-Jie Zhu, Junxiong Wang, Zhongzhu Zhou, Fan Lai, James Zou, Chenfeng Xu
- 发布：2026-10-14；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
