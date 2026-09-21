---
title: "ArenaFlow: From Trajectory Ranking to Hierarchical Credit Propagation for Open-Ended Agent RL"
description: "Reinforcement learning has substantially improved large language model (LLM) agents in verifiable domains, but remains difficult to apply to open-ended agent tasks, where solutions are diverse and reliable scalar rewards are hard to obtain."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.21378) · [PDF](https://arxiv.org/pdf/2609.21378)

## 一句话摘要

Reinforcement learning has substantially improved large language model (LLM) agents in verifiable domains, but remains difficult to apply to open-ended agent tasks, where solutions are diverse and reliable scalar rewards are hard to obtain.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement learning has substantially improved large language model (LLM) agents in verifiable domains, but remains difficult to apply to open-ended agent tasks, where solutions are diverse and reliable scalar rewards are hard to obtain. Recent pairwise evaluation methods alleviate reward discrimination collapse by replacing pointwise scoring with relative preferences. However, they still compress rich comparative feedback into a single trajectory-level reward, obscuring decisive intermediate steps and preventing successful behaviors from being consolidated into reusable skills. We propose ArenaFlow, a hierarchical credit propagation framework for open-ended agent reinforcement learning. ArenaFlow leverages tournament-based relative ranking to derive trajectory-level reward signals. Each comparison is further equipped with structured reflective evaluation, which reveals three types of supervision: pivotal success steps, reusable strategy skills, and usage attribution of retrieved skills. At the step level, ArenaFlow propagates trajectory-level advantages to high-confidence pivotal steps according to tournament survival depth, enabling more targeted optimization of local reasoning behaviors. At the skill level, ArenaFlow estimates skill utility from group-level usage attribution and maintains a global skill memory through utility-aware updating, pruning, and retrieval. The resulting high-utility skills further serve as policy priors for future exploration. Extensive experiments validate ArenaFlow's effectiveness on open-ended agent tasks.

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

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qiang Zhang, Ruixue Ding, Fanrui Zhang, Xi Chen, Boli Chen, Shihang Wang, Yinfeng Huang, Yi Zheng, Pengjun Xie, Kaipeng Zhang, Jiawei Liu, Zheng-Jun Zha
- 发布：2026-09-21；更新：2026-09-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
