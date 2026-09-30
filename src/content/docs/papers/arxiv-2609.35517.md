---
title: "Reward-Aligned Reweighting for On-Policy Distillation"
description: "On-policy distillation (OPD) trains a student language model with dense feedback from a stronger teacher on student-generated trajectories."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.35517) · [PDF](https://arxiv.org/pdf/2609.35517)

## 一句话摘要

On-policy distillation (OPD) trains a student language model with dense feedback from a stronger teacher on student-generated trajectories.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) trains a student language model with dense feedback from a stronger teacher on student-generated trajectories. Yet standard OPD weights token-level distillation terms uniformly, implicitly treating local teacher preference as a proxy for correction utility. A decision's task value, however, depends on how the student completes the subsequent reasoning. This mismatch can cause imitation to suppress viable student strategies or reinforce paths the student cannot reliably execute. Verified trajectory outcomes provide complementary evidence about continuation quality, but do not directly identify the utility of individual decisions. We introduce Reward-Aligned Reweighting for On-Policy Distillation (R$^{2}$-OPD), which uses outcome agreement and the magnitude of teacher--student disagreement to continuously reallocate teacher supervision. It gives reward-aligned corrections greater relative influence while retaining dense feedback, moving beyond uniform imitation and hard filtering. Our analysis formalizes the mismatch between local teacher preference and student continuation value and establishes sufficient conditions for reallocation to improve first-order task progress over uniform OPD. Across seven mathematical reasoning benchmarks, R$^{2}$-OPD achieves the highest average accuracy among the compared training methods in both cross-size and same-size distillation. It outperforms standard OPD on all seven benchmarks, with average gains of 3.5 and 2.4 percentage points for 1.7B and 4B students, respectively. An extension to code generation yields an average gain of 1.6 percentage points over standard OPD. These results highlight outcome-guided supervision allocation as an effective way to translate dense teacher feedback into stronger student performance across model scales and task domains.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haofeng Xu, Junwei Su, Lansong Diao, Wenchao Zhou, Chuan Wu
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
