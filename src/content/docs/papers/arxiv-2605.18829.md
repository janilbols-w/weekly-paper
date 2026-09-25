---
title: "Lossless Anti-Distillation Sampling"
description: "Frontier commercial generative models face a growing threat from distillation, whereby a distiller harvests generated responses and trains a competing model at drastically lower cost."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.18829) · [PDF](https://arxiv.org/pdf/2605.18829)

## 一句话摘要

Frontier commercial generative models face a growing threat from distillation, whereby a distiller harvests generated responses and trains a competing model at drastically lower cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Frontier commercial generative models face a growing threat from distillation, whereby a distiller harvests generated responses and trains a competing model at drastically lower cost. Existing defenses either modify the generation to degrade distillation performance, sacrificing response quality, or rely on behavioral detection mechanisms that can be readily bypassed through multi-account querying. In this work, we propose Lossless Anti-Distillation Sampling (LADS), which leaves the generation itself unchanged while substantially reducing the effectiveness of distillation. Concretely, LADS controls the latent randomness underlying inference through a coupling mechanism that preserves within-account generation independence while inducing cross-account dependence. By construction, each benign user, who typically holds only a single account, receives the same experience under LADS as they would without any defense, thereby enjoying a lossless experience. However, for a multi-account task-specific distiller, semantically similar queries submitted across different accounts are assigned coupled randomness, inducing dependence in the harvested data and thereby degrading the generalization performance of the distilled model. Using uniform convergence theory, we show that LADS provably degrades the distiller's generalization gap relative to standard i.i.d. sampling. Experiments on image generation, mathematical reasoning, and code generation confirm that LADS substantially degrades the performance of distilled students while preserving exact statistical fidelity for individual users.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zibo Diao, Jingchu Gai, Xinyue Ai, Zhang Zhang, Zhenyu He, Di He
- 发布：2026-09-25；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
