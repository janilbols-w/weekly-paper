---
title: "Distilling Drifting Transformers with Representation Autoencoders"
description: "Despite the significant training acceleration and promising performance, Representation Autoencoders (RAEs) are mainly criticized for poor distillation effectiveness."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.15553) · [PDF](https://arxiv.org/pdf/2606.15553)

## 一句话摘要

Despite the significant training acceleration and promising performance, Representation Autoencoders (RAEs) are mainly criticized for poor distillation effectiveness.

## 为什么值得关注

待编辑增强。

## 摘要原文

Despite the significant training acceleration and promising performance, Representation Autoencoders (RAEs) are mainly criticized for poor distillation effectiveness. In this work, we argue that RAE is competent at high-quality one-step generation. We achieve 1.48 FID with only 16-epoch distillation on ImageNet 256 dataset, surpassing various state-of-the-art methods. To achieve this, we quantitatively study the geometrical behavior of different underlying data spaces. We conclude that conventional distillation methods heavily rely on priors of plain teacher denoising trajectories, while RAE incurs much more complex trajectories with poor properties due to ill anisotropical latent space. We introduce the recently proposed drifting field as the distillation methodology, which makes use of semantically rich RAE latents and provides direct supervision involving no dependency. Bridging our Drift-RAE with previous generative paradigms, we propose several insightful modifications, including the first extrapolation-based guided sampling pipeline for one-step generation with barely no cost. The code will be made publicly available.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiawei Zhang, Mengfei Xia, Gen Li, Yuantao Gu
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
