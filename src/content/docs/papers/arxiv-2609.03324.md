---
title: "DE-Venus: A Data-Efficient RLVR Framework for Large Language Models"
description: "Reinforcement learning with verifiable rewards (RLVR) improves large language model reasoning, but its practical scaling is constrained by expensive on-policy rollouts and the cost of obtaining reliable targets at scale."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.03324) · [PDF](https://arxiv.org/pdf/2609.03324)

## 一句话摘要

Reinforcement learning with verifiable rewards (RLVR) improves large language model reasoning, but its practical scaling is constrained by expensive on-policy rollouts and the cost of obtaining reliable targets at scale.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement learning with verifiable rewards (RLVR) improves large language model reasoning, but its practical scaling is constrained by expensive on-policy rollouts and the cost of obtaining reliable targets at scale. Existing methods address sample selection, incomplete supervision, or noisy labels separately, often entangling supervision logic with distributed training and hindering controlled comparison and reuse. We present DE-Venus, a unified framework for data-efficient RLVR that treats supervision as evolving state across data preparation and policy optimization. It organizes this lifecycle into three modules: Active Data Selection allocates training and annotation budgets; Weak Supervision Construction derives learning signals from unlabeled examples; and Training-Time Supervision Refinement filters or corrects unreliable supervision. DE-Venus supports seven representative methods and a data-selection pipeline by expressing method-specific decisions as offline dataset transitions or online transformations of targets, rewards, batches, and advantages while preserving verl's distributed execution contracts. Across public benchmarks and three business scenarios, separate configurations preserve or improve model quality with only 10% of labels or as little as 13% of relevant data; selected business configurations also reduce observed convergence steps by 63%--75%. DE-Venus thus reduces annotation and training costs without sacrificing scalable RL execution.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distributed training
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shenzhi Yang, Guangcheng Zhu, Kai Tang, Zhengqing Zang, Xing Zheng, Haobo Wang, Yingfan Ma, Bowen Song, Bo Han, Bo An, Lei Feng, Weiqiang Wang, Junbo Zhao, Gang Chen
- 发布：2026-09-03；更新：2026-09-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
