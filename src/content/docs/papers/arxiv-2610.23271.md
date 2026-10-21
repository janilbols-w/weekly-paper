---
title: "NestedVLA: Learning to Consolidate and Generate Skills for Vision-Language-Action Models"
description: "Vision-language-action (VLA) models can learn a wide range of robotic skills, but combining separately trained skills remains challenging."
---

**评分：45/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.23271) · [PDF](https://arxiv.org/pdf/2610.23271)

## 一句话摘要

Vision-language-action (VLA) models can learn a wide range of robotic skills, but combining separately trained skills remains challenging.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision-language-action (VLA) models can learn a wide range of robotic skills, but combining separately trained skills remains challenging. The original training data may be unavailable for joint retraining, while directly merging model weights can cause interference. We propose NestedVLA, which consolidates independently fine-tuned VLA policies without access to their original training data. Instead of merging all updates into one checkpoint, a hypernetwork embedded in the VLA generates action-expert weight updates for a selected task. Each task's compressed vision-language model update is stored separately, and both updates are added to a frozen base VLA to instantiate the corresponding policy. We evaluate NestedVLA by consolidating three policies fine-tuned with reinforcement learning on MetaWorld, ManiSkill, and CALVIN. It achieves 66.7% average success, improving on the strongest model-merging baseline by 41.1 percentage points. It performs within 1 percentage point of per-task fine-tuning on ManiSkill and substantially narrows the gap on CALVIN. In this three-policy setting, total storage is 1.5x that of a single full checkpoint. Code is available at https://github.com/WanyuGroup/NeurIPS2026-NestedVLA.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Guodong Du, Wanyu Lin
- 发布：2026-10-21；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/WanyuGroup/NeurIPS2026-NestedVLA](https://github.com/WanyuGroup/NeurIPS2026-NestedVLA)
- 阅读深度：metadata
