---
title: "DREvo: Distilling Recalibrated Historical Experience for Harness Self-Evolution"
description: "Harness plays a critical role in large language model agent performance, and building a high-performing harness requires substantial expert effort."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.26722) · [PDF](https://arxiv.org/pdf/2607.26722)

## 一句话摘要

Harness plays a critical role in large language model agent performance, and building a high-performing harness requires substantial expert effort.

## 为什么值得关注

待编辑增强。

## 摘要原文

Harness plays a critical role in large language model agent performance, and building a high-performing harness requires substantial expert effort. Therefore, recent research has increasingly explored harness self-evolution, which iteratively proposes, evaluates, and improves harnesses using historical trial experience. However, accumulated historical experience does not always translate into stable search guidance, and performance often fluctuates substantially across evolution iterations, making it difficult to reliably discover high-performing harnesses under a limited evolution budget. We identify two limitations in how existing harness self-evolution methods leverage historical experience: (1) Lack of dynamic reassessment of whether historical experience remains valid for the current harness, and (2) Lack of explicit mechanisms for translating valid historical experience into actionable search directions. To address these limitations, we propose a new harness self-evolution method, named DREvo, which integrates function-level evidence anchoring, state-dependent evidence recalibration, and role-conditioned search intent distillation to determine which historical evidence remains valid and where the harness should evolve next. Under limited evolution budgets, DREvo exhibits smoother evolution trajectories, achieves the highest accuracy on all five benchmarks, and delivers average gains of 16.2% and 14.2% over the evaluated baselines on domain reasoning and agentic tasks, respectively.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
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

- 作者：Hanghui Guo, Weijie Shi, Zhangze Chen, Shengxiang Xu, Yishu Wang, Yimei Zhang, Wangze Ni, Jia Zhu, Shimin Di
- 发布：2026-08-13；更新：2026-08-13
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
