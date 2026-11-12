---
title: "AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models"
description: "Reinforcement learning with verifiable rewards (RLVR) produces rich training experience, yet outcome rewards reduce each attempt to a single number and leave most of this information unused."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2611.14515) · [PDF](https://arxiv.org/pdf/2611.14515)

## 一句话摘要

Reinforcement learning with verifiable rewards (RLVR) produces rich training experience, yet outcome rewards reduce each attempt to a single number and leave most of this information unused.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement learning with verifiable rewards (RLVR) produces rich training experience, yet outcome rewards reduce each attempt to a single number and leave most of this information unused. Training-time scaffolds, such as strategies or hints added to the prompt during training, offer a natural way to turn this information into guidance, but their design and adaptation are largely left to humans and tailored to specific domains. We introduce AutoScaffold, a unified AI-for-AI framework that turns a student's training experience into adaptive scaffolds, with minimal domain-specific information and no human intervention during training. A frozen teacher periodically examines this experience, diagnoses bottlenecks, and designs scaffolds in two forms: (i) strategies shared across a class of tasks and (ii) hints for individual hard tasks, adjusting the content and amount of support as the student learns. The scaffolds are removed at evaluation. We apply the same framework to ALFWorld, search-based QA, mathematical reasoning, and GPU kernel generation. When evaluated without scaffolds, students trained with AutoScaffold outperform those trained with the corresponding RL baselines in all four domains, with gains of 7.2 points in ALFWorld success and 4.0 points in average QA exact match. On GPU kernel generation, AutoScaffold increases the fraction of tasks with a correct kernel that runs faster than the PyTorch reference by up to 5.0 points. On math, our student surpasses QuestA's reported accuracy using approximately one-third as many student training steps. Analyses show that the teacher identifies a different failure in each task class and shifts its scaffolds from step-by-step workflows to targeted fixes as the student improves, and that its revised scaffolds help the student learn more than keeping the previous scaffold or using no scaffold.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu kernel, kernel generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zijian Zhang, Rizhen Hu, Jiangweizhi Peng, Shiyang Li, Sujay Bhatt, Sihan Zeng, Mingyi Hong
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
