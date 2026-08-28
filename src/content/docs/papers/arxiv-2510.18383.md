---
title: "MENTOR: Reinforcement Learning via Flexible Teacher-Optimized Rewards for Tool-Use Distillation"
description: "Distilling the tool-use capabilities of large language models (LLMs) into small language models (SLMs) is essential for their practical application."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2510.18383) · [PDF](https://arxiv.org/pdf/2510.18383)

## 一句话摘要

Distilling the tool-use capabilities of large language models (LLMs) into small language models (SLMs) is essential for their practical application.

## 为什么值得关注

待编辑增强。

## 摘要原文

Distilling the tool-use capabilities of large language models (LLMs) into small language models (SLMs) is essential for their practical application. The predominant approach, supervised fine-tuning (SFT), is an off-policy distillation method that suffers from poor out-of-domain (OOD) generalization because it rigidly aligns with static teacher trajectories. While reinforcement learning (RL) offers an alternative, the capacity limitations of SLMs pose a severe dilemma: sparse outcome rewards provide insufficient guidance, whereas strict trajectory matching imposes overly restrictive constraints. To bridge this capacity-driven gap, we propose MENTOR, an on-policy distillation framework that introduces a flexible yet process-aware reward structure. Instead of enforcing rigid replication, MENTOR uses the teacher's reference to guide tool-use behavior, balancing behavioral alignment with downstream performance. Extensive experiments on controlled executable-tool benchmarks demonstrate that MENTOR improves OOD tool-use performance compared to SFT and strict RL baselines. Our findings suggest that within verifiable tool-use environments, flexible tool-use alignment offers a more effective approach than strict trajectory replication for developing adaptable small models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：ChangSu Choi, Hoyun Song, Dongyeon Kim, Minkyung Cho, WooHyeon Jung, Sunjin Park, NohHyeob Bae, Seona Yu, KyungTae Lim
- 发布：2026-08-28；更新：2026-08-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
