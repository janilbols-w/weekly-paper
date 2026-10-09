---
title: "Diffu-LoRA: A Novel Low-Rank Adaptation for Personalized Diffusion Models"
description: "Personalizing text-to-image diffusion models from a few reference images requires preserving subject identity while following prompts that describe new contexts."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.10550) · [PDF](https://arxiv.org/pdf/2610.10550)

## 一句话摘要

Personalizing text-to-image diffusion models from a few reference images requires preserving subject identity while following prompts that describe new contexts.

## 为什么值得关注

待编辑增强。

## 摘要原文

Personalizing text-to-image diffusion models from a few reference images requires preserving subject identity while following prompts that describe new contexts. Full-model fine-tuning is parameter-intensive, whereas low-rank adaptation (LoRA) reduces the number of trainable parameters but leaves open how adaptation capacity should be distributed across layers. We introduce Diffu-LoRA, a parameter-efficient method that learns this allocation through gated low-rank adaptation. Diffu-LoRA inserts trainable low-rank components into the linear layers of Transformer blocks and assigns a learnable gate to each component. Bilevel optimization updates the adaptation weights and gate parameters on separate data splits, while progressive pruning removes components with the lowest gate values to meet a prescribed rank budget. This procedure allocates adaptation capacity nonuniformly across layers while keeping the pretrained backbone frozen. Experiments with Stable Diffusion on subjects from DreamBooth and additional collected datasets show improved overall subject fidelity and prompt alignment relative to the evaluated fine-tuning baselines. Ablation studies examine the contributions of bilevel optimization, progressive pruning, and adapter placement. These results support learned rank allocation as a practical approach to parameter-efficient diffusion model personalization.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 15 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tianjing Li, Wei Zhu
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
