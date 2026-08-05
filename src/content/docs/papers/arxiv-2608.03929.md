---
title: "Latent Reward Registers for Diffusion Preference Alignment"
description: "Aligning diffusion models with human preferences usually relies on a sparse terminal reward evaluated on the final generated samples, presenting a severe temporal credit-assignment challenge across the multi-step denoising process."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.03929) · [PDF](https://arxiv.org/pdf/2608.03929)

## 一句话摘要

Aligning diffusion models with human preferences usually relies on a sparse terminal reward evaluated on the final generated samples, presenting a severe temporal credit-assignment challenge across the multi-step denoising process.

## 为什么值得关注

待编辑增强。

## 摘要原文

Aligning diffusion models with human preferences usually relies on a sparse terminal reward evaluated on the final generated samples, presenting a severe temporal credit-assignment challenge across the multi-step denoising process. We propose Latent Reward Registers, a mechanism that estimates terminal preference directly from intermediate noisy latents by prepending learnable, position-free register tokens to the input sequence of a frozen Diffusion Transformer (DiT). This independent readout mechanism extracts latent reward evidence without altering the generator's hidden states or velocity field. The resulting dense, differentiable reward signal throughout the full denoising process facilitates two alignment strategies. For training, Reward-Gradient On-Policy Distillation (RG-OPD) distills reward-guided updates along on-policy trajectories, bypassing the computationally expensive rollouts of standard policy gradients. For inference, Reward-Guided Sampling (RGS) steers trajectories via magnitude-matched reward gradients without parameter updates. Empirically, at high noise levels (u = 0.8), the registers reach the highest pairwise accuracy among the evaluated latent reward models. Furthermore, RG-OPD outperforms online reinforcement learning baselines while reducing GPU hours by up to 33x, and RGS establishes a new state-of-the-art among training-free methods, strictly enhancing both alignment and perceptual metrics. Code and weights are available at https://github.com/Guanys-dar/latent-reward-register

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
- 发布：2026-08-05；更新：2026-08-05
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Guanys-dar/latent-reward-register](https://github.com/Guanys-dar/latent-reward-register)
- 阅读深度：metadata
