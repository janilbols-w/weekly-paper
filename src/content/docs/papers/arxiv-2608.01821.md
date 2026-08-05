---
title: "DAVET: Denoising-Aware Visual Evidence Trajectory Allocation for Diffusion Vision-Language Models"
description: "Diffusion vision-language models (dVLMs) iteratively denoise masked responses while conditioning each denoising step on visual evidence, making visual conditioning a substantial recurring inference cost."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.01821) · [PDF](https://arxiv.org/pdf/2608.01821)

## 一句话摘要

Diffusion vision-language models (dVLMs) iteratively denoise masked responses while conditioning each denoising step on visual evidence, making visual conditioning a substantial recurring inference cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion vision-language models (dVLMs) iteratively denoise masked responses while conditioning each denoising step on visual evidence, making visual conditioning a substantial recurring inference cost. Unlike autoregressive decoding, diffusion generation repeatedly revisits the entire response as uncertainty evolves. Our analysis reveals that visual evidence demand is strongly step-dependent, motivating adaptive allocation across denoising steps. Existing inference acceleration methods operate through decoding-side strategies or visual token compression via pruning and merging, but do not explicitly treat visual evidence as a resource whose demand evolves across the diffusion process. Therefore, we present Denoising-Aware Visual Evidence Trajectory Allocation (DAVET), a training-free framework that allocates visual evidence according to the evolving generation state. Starting from a phase-conditioned evidence trajectory, the proposed allocation policy uses operation demand to set an evidence reserve whose allocation at each denoising step is modulated by trajectory risk. DAVET realizes the resulting budgets through a hierarchy of evidence views constructed from a single visual encoding, separating when and how much evidence is needed from how the evidence views are constructed. Evaluated on two representative dVLMs, LLaDA-V and LaViDa, across multiple visual-understanding benchmarks, DAVET achieves an average speedup of 1.55$\times$ with an average relative performance drop of 1.86\%, showing that denoising-aware visual evidence allocation can reduce visual conditioning cost while largely preserving generation quality.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yongkang Zhou, Xiang Xia, Cheng Yan, Fan Xu, Wuyang Zhang
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
