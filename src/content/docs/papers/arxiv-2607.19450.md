---
title: "REGEN: Replay-recycling for Expert-to-Generalist distillation with Offline Reinforcement Learning"
description: "Large-scale online reinforcement learning (RL) is the predominant means of eliciting advanced abilities including long-term reasoning and agentic tool use in large language models (LLMs)."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.19450) · [PDF](https://arxiv.org/pdf/2607.19450)

## 一句话摘要

Large-scale online reinforcement learning (RL) is the predominant means of eliciting advanced abilities including long-term reasoning and agentic tool use in large language models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Large-scale online reinforcement learning (RL) is the predominant means of eliciting advanced abilities including long-term reasoning and agentic tool use in large language models (LLMs). However, continuing to scale it across vast task domains of interest remains challenging in both computational infrastructure and cost, especially when considering RL as merely a one-off learning stage. Recently, a widely used technique for distilling knowledge across various domains and training stages, multi-teacher on-policy distillation (MOPD), helps to decouple the RL stage, saving costs, while maintaining generality across vast domains. Nonetheless, similar to online RL, MOPD requires coupled inference and backward passes, which continues to limit its scalability and computational efficiency. To address these challenges, we propose REGEN: Replay-recycling for Expert-to-Generalist Distillation with Offline RL. Instead of distilling from multiple teacher models, REGEN trains a generalist by simply recycling the replay memory -- the free by-product of the teachers' specialized RL training -- and employing offline RL algorithms. REGEN completely decouples the rollout sampling from the backward training process and thus greatly reduces the training cost. Across mathematical reasoning, code generation, and instruction following, REGEN matches the accuracy of MOPD at substantially lower cost. It potentially turns online RL into a data synthesis process instead of a one-off learning stage, and can be extended to large-scale post-training without requiring heavy computational load. Code is available at https://github.com/yunjie-sysu/REGEN.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yunjie Chen, Zihao Chen, Xiaoxin Chen, Fang Wang
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/yunjie-sysu/REGEN](https://github.com/yunjie-sysu/REGEN)
- 阅读深度：metadata
