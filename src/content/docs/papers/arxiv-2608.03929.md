---
title: "Latent Reward Registers for Diffusion Preference Alignment"
description: "Aligning diffusion models with human preferences usually relies on a sparse terminal reward evaluated on the final generated samples, which creates a severe temporal credit-assignment problem across the denoising process."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.03929) · [PDF](https://arxiv.org/pdf/2608.03929)

## 一句话摘要

Aligning diffusion models with human preferences usually relies on a sparse terminal reward evaluated on the final generated samples, which creates a severe temporal credit-assignment problem across the denoising process.

## 为什么值得关注

待编辑增强。

## 摘要原文

Aligning diffusion models with human preferences usually relies on a sparse terminal reward evaluated on the final generated samples, which creates a severe temporal credit-assignment problem across the denoising process. We propose Latent Reward Registers, a mechanism that estimates terminal preference directly from intermediate noisy latents. Learnable, position-free register tokens are appended as an auxiliary read path to a frozen Diffusion Transformer (DiT), extracting preference signals without altering the generator's hidden states or velocity field. The resulting dense, differentiable reward field spans the full denoising trajectory and supports two alignment strategies. For training, Reward-Gradient On-Policy Distillation (RG-OPD) converts this dense reward field into per-step targets at states visited by the current generator, replacing rollout-intensive policy gradients with direct on-policy distillation. For inference, Reward-Guided Sampling (RGS) steers trajectories with magnitude-matched reward-gradient corrections and no parameter updates. Empirically, at high noise levels (t=0.8) the registers reach the highest pairwise accuracy among the evaluated latent reward models. RG-OPD outperforms online reinforcement learning baselines while reducing GPU hours by up to 33x. RGS achieves significant reward improvement with a favorable reward-quality balance against training-free baselines. Code and weights are to be available at https://github.com/Guanys-dar/latent-reward-register

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Yuanshen Guan, Zipeng Feng, Zhiwei Xiong, Peiqin Sun
- 发布：2026-08-05；更新：2026-08-17
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Guanys-dar/latent-reward-register](https://github.com/Guanys-dar/latent-reward-register)
- 阅读深度：metadata
