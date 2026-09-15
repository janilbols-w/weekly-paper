---
title: "Self-Evolving AI for Humanoids: Mechanisms, Safety, and Evaluation of Post-Deployment Self-Improvement"
description: "Humanoid robots are becoming an important part of embodied artificial intelligence, driven by advances in reinforcement learning for locomotion, world models for prediction, and vision-language-action models for general control."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.13236) · [PDF](https://arxiv.org/pdf/2609.13236)

## 一句话摘要

Humanoid robots are becoming an important part of embodied artificial intelligence, driven by advances in reinforcement learning for locomotion, world models for prediction, and vision-language-action models for general control.

## 为什么值得关注

待编辑增强。

## 摘要原文

Humanoid robots are becoming an important part of embodied artificial intelligence, driven by advances in reinforcement learning for locomotion, world models for prediction, and vision-language-action models for general control. However, most of these systems remain static after deployment. A policy is trained offline for a fixed objective and then frozen, even though the tasks, environments, and robot bodies keep drifting over time. An emerging paradigm of self-evolving agents aims to address this problem by allowing systems to improve from their own post-deployment experience. Since most existing studies focus on disembodied software agents, this survey examines how self-evolution changes when an agent has a physical body. We first define self-evolution for humanoids and represent a deployed robot using a state tuple that includes its policy, perception, memory, workflow, and body. This state is updated by an evolution operator in a slow outer loop with a lifelong objective. We then organize the literature into four complementary mechanisms of self-evolution, presented in increasing order of autonomy: self-learning, self-adaptation, self-optimization, and self-generation. Since changes to a humanoid can introduce physical hazards, we treat safety and uncertainty as key design dimensions of the evolution operator, and further formulate admissible evolution as a constraint enforced by a world-model verification gate within a human-oversight envelope. Finally, we present that evaluation should track the robot's evolving trajectory rather than a fixed checkpoint, and we identify the lack of a benchmark designed specifically for self-evolving humanoids. Moreover, we outline open challenges spanning AI algorithms, on-board systems, and governance.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Loc X. Nguyen, Avi Deb Raha, Huy Q. Le, Eui-Nam Huh, Dusit Niyato, Choong Seon Hong
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
