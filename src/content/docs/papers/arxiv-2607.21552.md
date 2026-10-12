---
title: "MIRROR: Learning from the Other View for Multi-Modal Reasoning"
description: "Vision-language models (VLMs) can behave very differently depending on whether the same underlying problem is presented textually or visually."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.21552) · [PDF](https://arxiv.org/pdf/2607.21552)

## 一句话摘要

Vision-language models (VLMs) can behave very differently depending on whether the same underlying problem is presented textually or visually.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision-language models (VLMs) can behave very differently depending on whether the same underlying problem is presented textually or visually. This inconsistency suggests that different views expose different reasoning paths and failure modes that standard multimodal post-training does not fully exploit. To study and exploit this phenomenon, we construct ODA-Data, a high-quality paired multimodal geometry dataset with text-dominant, image-dominant, and combined image+text views of the same problems, together with splits for training and evaluating view dependent reasoning behaviors. We then develop Modality-Informed Reciprocal Reasoning Optimization (MIRROR), a reinforcement learning approach that derives a cross-view self-distillation signal from the model's own modality-dependent capabilities. For each problem, MIRROR evaluates the model under all views, selects the best-performing view as a teacher, and trains the remaining views using a GRPO task-reward objective augmented with a reverse-KL regularizer toward that teacher. Across reasoning benchmarks that evaluate on multimodal mathematics problems, MIRROR improves over standard RL and yields more accurate and consistent behavior across different input modality representations.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Wen Ye, Yuxiao Qu, Aviral Kumar, Xuezhe Ma
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
