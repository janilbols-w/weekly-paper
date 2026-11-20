---
title: "Finetuning VLAs for Dexterous Manipulation: The Right Checkpoint Is All You Need"
description: "Vision-Language-Action models have demonstrated strong manipulation capabilities."
---

**评分：40/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2611.23676) · [PDF](https://arxiv.org/pdf/2611.23676)

## 一句话摘要

Vision-Language-Action models have demonstrated strong manipulation capabilities.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision-Language-Action models have demonstrated strong manipulation capabilities. A limitation of VLA models is that most manipulation datasets focus on parallel-jaw gripper systems, making transfer to multi-finger hands challenging, particularly as teleoperation datasets are harder to collect with multi-fingered robots. In this work, we study how to best adapt VLAs to dexterous hands by pairing supervised fine-tuning (SFT) with diffusion-steering reinforcement learning (DSRL). Using $\pi_{0.5}$ and a LEAP hand, we evaluate five fine-tuning recipes across two simulation tasks using only a handful of demonstrations. Our empirical analysis yields three key insights: (1) SFT success is poorly correlated with post-DSRL success, meaning the best SFT checkpoint is rarely the most effective to steer; (2) freezing the vision-language model (VLM) and tuning only the action expert produces the most steerable policy for both training and out-of-distribution placements; and (3) low-rank adaptation (LoRA) is the least steerable approach. Consequently, we recommend an adaptation recipe that freezes the VLM, fully trains the action expert, and eschews SFT rollout success as a checkpoint selection metric.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Artur Kuramshin, Charlotte Cloutier, Michael Przystupa, Kirsty Ellis, Mohammad S. Akhter, Glen Berseth
- 发布：2026-11-18；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
