---
title: "SmolWAM: A Latent World-Action Model for Robotic Manipulation on Edge Devices"
description: "World-action models (WAMs) jointly predict robot actions and future observations, but their video diffusion backbones are costly for edge deployment."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.13740) · [PDF](https://arxiv.org/pdf/2610.13740)

## 一句话摘要

World-action models (WAMs) jointly predict robot actions and future observations, but their video diffusion backbones are costly for edge deployment.

## 为什么值得关注

待编辑增强。

## 摘要原文

World-action models (WAMs) jointly predict robot actions and future observations, but their video diffusion backbones are costly for edge deployment. We introduce SmolWAM, a compact latent WAM derived from the 2B-parameter Cosmos Policy using single-frame encoding, cached text features with preserved attention sinks, depth pruning, and token compaction. With 12 of 28 transformer blocks and 1,008 tokens, SmolWAM predicts actions and future latents in one rectified-flow step. After 3.6 A100 GPU-hours of training, it achieves 95.5% success over 400 LIBERO episodes at 57ms, 2.3TFLOP, and 2.4GiB per 16-action chunk on an A100: 11x lower latency and 3.2x lower memory than the five-step teacher. Its world head predicts scene motion; joint training improves success by 6.2 percentage points over an action-only ablation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Timi Owolabi, Hikmah Olawore, Frances Adelakun, Ayotomiwa Oyewumi
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
