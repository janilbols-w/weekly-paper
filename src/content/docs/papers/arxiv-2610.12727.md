---
title: "Zebra3D: Efficient Hybrid Foundation Models For Scalable 3D Reconstruction"
description: "Feed-forward 3D foundation models reconstruct scenes from unposed images, but the quadratic cost of global attention limits their scalability to large view sets."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.12727) · [PDF](https://arxiv.org/pdf/2610.12727)

## 一句话摘要

Feed-forward 3D foundation models reconstruct scenes from unposed images, but the quadratic cost of global attention limits their scalability to large view sets.

## 为什么值得关注

待编辑增强。

## 摘要原文

Feed-forward 3D foundation models reconstruct scenes from unposed images, but the quadratic cost of global attention limits their scalability to large view sets. We present Zebra3D, a layerwise sparse-linear hybrid attention framework that improves the efficiency of pretrained 3D foundation models without training from scratch. Across VGGT, HunyuanWorld-Mirror, and $\pi^3$, we observe a broadly consistent depth-wise pattern: early stages are relatively tolerant to linear replacement, while sensitive middle-to-late stages tend to exhibit more concentrated attention. Zebra3D exploits this structure by assigning linear-centered attention to tolerant stages and tile-sparse attention to sensitive stages, using landmark summaries to preserve unselected context. Closed-form affine fitting enables training-free conversion, while optional post-conversion training combines task supervision with output and relational feature distillation. Across all three backbones, Zebra3D achieves strong reconstruction and camera-pose accuracy at high attention sparsity, with training-free variants remaining close to their dense counterparts. End-to-end speedups increase with input view count, reaching up to $7.1\times$ at 1,024 views. After post-conversion training, Zebra3D-VGGT reaches 80.5\% RealEstate10K AUC@30 at 94\% mean attention sparsity, within 1.1 percentage points of dense VGGT fine-tuned on the same data and schedule.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Utkarsh Saxena, Ruijing Yang, Mehdi Rezagholizadeh, Akash Haridas, Vikram Appia, Emad Barsoum
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
