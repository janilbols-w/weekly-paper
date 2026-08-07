---
title: "CausalOPD: First-Wrong-Step Supervision for Distilling Causal Chain Reasoning"
description: "Many critical reasoning tasks, including clinical diagnosis, legal judgment, and industrial fault diagnosis, require step-dependent causal chains in which early errors propagate and correct conclusions can mask invalid reasoning."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.03673) · [PDF](https://arxiv.org/pdf/2608.03673)

## 一句话摘要

Many critical reasoning tasks, including clinical diagnosis, legal judgment, and industrial fault diagnosis, require step-dependent causal chains in which early errors propagate and correct conclusions can mask invalid reasoning.

## 为什么值得关注

待编辑增强。

## 摘要原文

Many critical reasoning tasks, including clinical diagnosis, legal judgment, and industrial fault diagnosis, require step-dependent causal chains in which early errors propagate and correct conclusions can mask invalid reasoning. Although large language models perform well on such tasks, privacy, latency, and controllability motivate distillation into locally deployable models. Standard trajectory imitation does not correct process errors on the student's own rollout distribution. We propose CausalOPD, a curriculum online process distillation framework. A knowledge-augmented teacher first provides trajectories grounded in domain-specific causal rules, entity relations, and structural constraints. The student then generates on-policy trajectories, and the teacher identifies the first wrong step, defined as the earliest transition that verifiably violates available constraints. Starting from the verified prefix, short-horizon reinforcement learning repairs this localized failure. A causal-stage curriculum advances from evidence-level to mechanism-level and conclusion-level errors, following their propagation order. Across three domains, CausalOPD improves average path correctness by 23.4 percentage points over sequence-level online process distillation and reduces the right-label-wrong-reasoning rate from 15.7% to 4.4%. The domain-specific 8B students also surpass both evaluated proprietary references in path correctness across all domains.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jian Zhang, Bingyi Wang, Yizhi Liu
- 发布：2026-08-04；更新：2026-08-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
