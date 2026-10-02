---
title: "Dense Is Not Enough: Hierarchical Supervision Allocation for Long-Horizon On-Policy Distillation"
description: "On-policy distillation (OPD) transfers the capabilities of a large language model to a smaller student by providing teacher supervision on the student's own rollouts."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.33409) · [PDF](https://arxiv.org/pdf/2609.33409)

## 一句话摘要

On-policy distillation (OPD) transfers the capabilities of a large language model to a smaller student by providing teacher supervision on the student's own rollouts.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) transfers the capabilities of a large language model to a smaller student by providing teacher supervision on the student's own rollouts. In long-horizon agentic tasks, however, uniform token-level matching can allocate supervision poorly: a large local discrepancy need not improve future behavior, while consequential guidance may be beyond the current student's reach or fail to persist without privileged input. We formulate long-horizon OPD as hierarchical supervision allocation and argue that productive guidance lies at the intersection of future utility and current learnability. Crucially, this intersection evolves as the student learns. Based on this principle, we propose LENS-OPD, a coarse-to-fine framework that organizes supervision through Locate, Validate, and Refine. Locate adapts trajectory exposure to the student's evolving competence and proposes a candidate decision for intervention. Validate tests whether teacher guidance at that decision improves the same student's subsequent behavior. Refine internalizes the beneficial guided behavior into the deployable policy and concentrates token-level supervision on decisive teacher-student conflicts within the validated turn. These stages are nested: each finer allocation is conditioned on the coarser decision, rather than being optimized as an independent importance score. Experiments across multiple long-horizon agent benchmarks and student-teacher configurations show that LENS-OPD consistently improves task performance over vanilla OPD and strong curriculum- and selection-based baselines. Our results suggest that effective long-horizon distillation requires teaching at the right depth, the right decision, and the right token.

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

- 作者：Yuhao Sun, Binrui Wu, Zhuoer Xu, Ming Wen, Haoxiang Xu, Bin Chen, Yan Lin, Qianzijing Zhang
- 发布：2026-09-27；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
