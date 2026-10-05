---
title: "Adaptive Mutual Distillation for Balanced Multi-Task Post-Training of Large Language Models"
description: "Multi-task post-training of large language models (LLMs) aims to improve performance across tasks with unequal amounts of training data."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.02856) · [PDF](https://arxiv.org/pdf/2610.02856)

## 一句话摘要

Multi-task post-training of large language models (LLMs) aims to improve performance across tasks with unequal amounts of training data.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multi-task post-training of large language models (LLMs) aims to improve performance across tasks with unequal amounts of training data. Existing methods focus primarily on balancing task contributions during single-model training. Different task-balancing strategies can produce models with complementary strengths, creating opportunities for mutual distillation. However, the usefulness of cross-model supervision can vary across tasks, transfer directions, and stages of training. We propose Adaptive Mutual Distillation (AMD), a collaborative post-training framework that jointly trains two models with different task-balancing strategies. AMD evaluates candidate adjustments to distillation weights through short training probes shared across tasks, then uses task-wise validation scores to select an adjustment for each task and transfer direction. Across six benchmarks and three LLM backbones, both AMD models achieve higher average benchmark scores than supervised fine-tuning (SFT) baselines trained with the same sampling strategies. They also outperform the task-balancing methods evaluated in our experiments. Merging the two trained models can further improve their average benchmark score while yielding a single model for inference. The merged models outperform multi-task SFT by an average of 2.91 points across the three backbones.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Baohang Li, Xiaocheng Feng, Yichong Huang, Chengpeng Fu, Wenshuai Huo, Zekun Zhou, Zekun Yuan, Tingjia Zhang, Bing Qin
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
