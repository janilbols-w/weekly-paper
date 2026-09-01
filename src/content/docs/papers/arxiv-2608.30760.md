---
title: "PRACTICE: From Experience to Expertise in Self-Evolving Embodied Agents"
description: "Recent studies have shown that multimodal large language models (MLLMs) can serve as embodied agents, translating language instructions and visual observations into executable plans."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.30760) · [PDF](https://arxiv.org/pdf/2608.30760)

## 一句话摘要

Recent studies have shown that multimodal large language models (MLLMs) can serve as embodied agents, translating language instructions and visual observations into executable plans.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent studies have shown that multimodal large language models (MLLMs) can serve as embodied agents, translating language instructions and visual observations into executable plans. However, building agents that can continually improve through interaction and rapidly adapt to their environments remains challenging. Summing up experience from past interaction trajectories provides a promising solution, but existing experience-based methods often rely on manually designed prompting workflows to extract and update skills. Such fixed procedures may struggle to learn updated skills from new and diverse experiences. We introduce PRACTICE, which trains a skill learner to discover and maintain a persistent skill library from past interaction trajectories while keeping the task executor frozen. Given the historical accumulated skills and incoming trajectories, the skill learner produces structured batch-edits that add, refine, merge, or remove skills, and then hierarchical consolidate all collected edits into a consistent updated skill library. We train the learner with a two-stage curriculum. First, it learns basic skill generation and library maintenance from oracle trajectories. Then, by contrasting successful and failed trajectories from heterogeneous executors on the same tasks, it learn to identify invalid action patterns and recovery strategies. Finally, we apply online skill-edit distillation to align the skill learner with a stronger teacher on its current edit distribution to further improves the policy. Experiments demonstrate that a compact skill learner delivers consistent performance improvements across successive library-update rounds for multiple frozen executors. On EB-ALFRED and EB-Habitat, PRACTICE further outperforms the strongest experience-based baselines. Project resources are publicly available at: https://baai-agents.github.io/PRACTICE

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
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

- 作者：Ziyi Bai, Siqi Li, Tinglei Huang, B\"orje F. Karlsson
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
