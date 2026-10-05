---
title: "AdaptViT: Runtime-Adaptive Vision Transformer Deployment on Custom RISC-V"
description: "Deploying Vision Transformers (ViTs) on low-power edge devices is challenging due to high computational demands."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.02288) · [PDF](https://arxiv.org/pdf/2610.02288)

## 一句话摘要

Deploying Vision Transformers (ViTs) on low-power edge devices is challenging due to high computational demands.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deploying Vision Transformers (ViTs) on low-power edge devices is challenging due to high computational demands. Conventional pruning frameworks require a separate compiled binary for each sparsity level, increasing storage overhead and limiting runtime adaptability. This paper presents an end-to-end deployment pipeline that transforms pretrained ViTs into a single runtime-configurable binary, enabling dynamic compute-budget switching on embedded CPUs. This is achieved by restructuring generated C kernels with modified loop bounds and binary-mask control logic, allowing execution to switch across discrete sparsity levels via compact external configuration files. Compared to multi-binary deployment, the proposed runtime-adaptive approach reduces on-device storage by up to 4.86x, requiring only 163 MB for ViT-Base instead of nearly 800 MB. To maximize pruning efficiency, we introduce a hardware-aligned block pruning strategy for Multi-Layer Perceptron (MLP) layers. In addition, a custom ISA extension is proposed to exploit input-reuse patterns in linear projection kernels. On a Synopsys TRV32P3FX RISC-V processor, the full system achieves up to 2.8x speedup at 65% MLP and 50% attention-head pruning for ViT-Base. The ISA extension alone provides a 1.56x speedup and 33% lower inference energy, with a 24.7% area overhead in a TSMC 28 nm implementation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Vishnu PS (University College Dublin, Ireland), Ajay Kumar M (University College Dublin, Ireland), Yike Li (University College Dublin, Ireland), Robert Bogdan Staszewski (University College Dublin, Ireland), Deepu John (University College Dublin, Ireland)
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
