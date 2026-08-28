---
title: "Consolidating RLVR Capabilities Across Domains: A Deep Dive into Fusion Paradigms"
description: "Reinforcement learning with verifiable rewards (RLVR) improves specific capabilities of large language models, but covering multiple capabilities often involves training separate domain experts and subsequently consolidating them."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.27409) · [PDF](https://arxiv.org/pdf/2608.27409)

## 一句话摘要

Reinforcement learning with verifiable rewards (RLVR) improves specific capabilities of large language models, but covering multiple capabilities often involves training separate domain experts and subsequently consolidating them.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement learning with verifiable rewards (RLVR) improves specific capabilities of large language models, but covering multiple capabilities often involves training separate domain experts and subsequently consolidating them. We organize three fusion paradigms by the artefacts they reuse: Merge combines expert task vectors, Mix RL pools their datasets, and multi-teacher on-policy distillation (MOPD) uses both. Because they have largely been studied in isolation, how they compare and how to choose among them remain unclear. We compare all three using shared experts and data across model scales and a multi-domain benchmark suite. Although their average performance differs by at most 1.4 points, the gap reaches 8.6 points on a single benchmark, with domain-level variation tracking cross-domain relations visible in task-vector geometry. Training dynamics expose distinct constraints: Mix RL depends on domain mixture proportions, MOPD remains bounded by its teachers, and Merge compresses all expert updates into one. All three improve single-sample accuracy without measurable gains in solution coverage or losses in held-out capabilities. These results yield a practical guideline: use Merge when experts already exist and cheap fusion is paramount; Mix RL when training a unified model without experts, with domain proportions adjusted for cross-domain transfer; and MOPD when preserving domain-specific gains matters more than surpassing teachers or minimizing end-to-end cost.

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

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Siye Wu, Kai Yang, Yuchen Cai, Xin Xu, Peng-Yuan Wang, Jiaxuan Wang, Jiashun Liu, Jiafei Lyu, Yangkun Chen, Saiyong Yang, Yanghua Xiao
- 发布：2026-08-27；更新：2026-08-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
