---
title: "A Recipe for Long-Context Reasoning in Large Language Models via On-Policy Optimization and Distillation"
description: "Existing approaches to post-train models for long-context tasks face complementary limitations: (i) supervised fine-tuning (SFT) provides stable supervision but suffers from exposure bias; (ii) reinforcement learning methods such as Group Relative Policy Optimization (GRPO) train on model-generated trajectories but struggle with long-horizon credit assignmen"
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.12227) · [PDF](https://arxiv.org/pdf/2605.12227)

## 一句话摘要

Existing approaches to post-train models for long-context tasks face complementary limitations: (i) supervised fine-tuning (SFT) provides stable supervision but suffers from exposure bias; (ii) reinforcement learning methods such as Group Relative Policy Optimization (GRPO) train on model-generated trajectories but struggle with long-horizon credit assignmen

## 为什么值得关注

待编辑增强。

## 摘要原文

Existing approaches to post-train models for long-context tasks face complementary limitations: (i) supervised fine-tuning (SFT) provides stable supervision but suffers from exposure bias; (ii) reinforcement learning methods such as Group Relative Policy Optimization (GRPO) train on model-generated trajectories but struggle with long-horizon credit assignment and sparse rewards; and (iii) on-policy distillation (OPD) provides dense token-level guidance but does not directly optimize task rewards. We study these complementary strategies for long-context alignment and derive a recipe that combines GRPO with OPD-style teacher guidance: the student learns from its own rollouts using outcome-level rewards, while a stronger teacher provides dense token-level regularization in place of the standard reference policy. This is especially useful when process-level supervision is difficult to obtain. To support this study, we introduce LongBlocks, a synthetic multilingual dataset spanning multi-hop reasoning, contextual grounding, and long-form generation. Through controlled ablations, we isolate the roles of cold-start initialization, teacher anchoring, and data mixing, showing that our recipe yields a more stable and effective path to long-context reasoning than GRPO or OPD while preserving short-context capabilities.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Miguel Moura Ramos, Duarte M. Alves, Andr\'e F. T. Martins
- 发布：2026-09-11；更新：2026-09-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
