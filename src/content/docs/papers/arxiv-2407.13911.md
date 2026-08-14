---
title: "Continual Distillation Learning for Rehearsal-Free Class-Incremental Learning via Decoupled Prompting"
description: "Prompt-based continual learning has shown strong performance in rehearsal-free class-incremental learning by adapting learnable prompts while freezing a pre-trained Vision Transformer (ViT) backbone."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2407.13911) · [PDF](https://arxiv.org/pdf/2407.13911)

## 一句话摘要

Prompt-based continual learning has shown strong performance in rehearsal-free class-incremental learning by adapting learnable prompts while freezing a pre-trained Vision Transformer (ViT) backbone.

## 为什么值得关注

待编辑增强。

## 摘要原文

Prompt-based continual learning has shown strong performance in rehearsal-free class-incremental learning by adapting learnable prompts while freezing a pre-trained Vision Transformer (ViT) backbone. However, the effect of backbone scale remains underexplored. We observe that larger ViT backbones consistently yield better continual learning performance, which motivates us to study how to transfer such capability from a larger model to a smaller one. In this paper, we introduce Continual Distillation Learning (CDL), a new setting for knowledge distillation in rehearsal-free prompt-based continual learning. We show that conventional distillation methods provide only limited gains in CDL, mainly because task-specific prompts are forced to encode both continual adaptation and distillation knowledge, while lacking a persistent mechanism for cross-task knowledge transfer. To address this problem, we propose Decoupled Continual Distillation Learning (D-CDL), which introduces persistent Knowledge-Distillation prompts (KD-prompts) and a dedicated KD branch to explicitly decouple distillation from task adaptation. The proposed KD-prompts are propagated across tasks as a global carrier of teacher knowledge, while the original prompts remain responsible for continual learning. D-CDL is simple, general, and can be integrated into various prompt-based continual learning frameworks. Extensive experiments on Split CIFAR-100 and Split ImageNet-R across four representative continual learning methods show that D-CDL consistently outperforms existing distillation baselines and substantially improves student performance under different teacher-student settings.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qifan Zhang, Yunhui Guo, Yu Xiang
- 发布：2026-08-14；更新：2026-08-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
