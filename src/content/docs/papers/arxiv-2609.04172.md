---
title: "Rethinking On-Policy Distillation of Large Language Models II: One Training Example"
description: "On-policy distillation (OPD) combines student-generated rollouts with dense token-level supervision from a teacher."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.04172) · [PDF](https://arxiv.org/pdf/2609.04172)

## 一句话摘要

On-policy distillation (OPD) combines student-generated rollouts with dense token-level supervision from a teacher.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) combines student-generated rollouts with dense token-level supervision from a teacher. Existing work has mainly studied its algorithmic behavior, leaving the role of training data unclear. We examine this role at the data-minimal limit by training on a single query. One-shot OPD keeps improving for hundreds of steps and recovers most of full-data OPD's gain across task domains and model families. We explain this result through the states visited during training and the rate at which the student aligns with the teacher. We measure \emph{state coverage}, the fraction of the states full-data OPD visits that a query set's rollouts reach. A single query already reaches \(71.5\%\), most of it within the first 100 steps. Adding semantically distinct queries raises coverage and validation accuracy together, until 16 queries reach \(98.9\%\) and match full-data training. Yet alignment slows at a similar pace whether OPD trains on one query or the whole dataset, and even a fixed set of states takes hundreds of steps to absorb. OPD is therefore data-overfed but algorithm-starved. Its rollouts quickly expose broad supervision, while the student absorbs that supervision increasingly slowly. The state-coverage result extends to multi-teacher OPD, where 16 semantically diverse queries per domain match full-data MOPD. As a further stress test, content-light templates and off-domain WildChat queries also approach the real-query baseline. Task content and induced state coverage can therefore come apart. We hope these findings direct future work toward the step efficiency of OPD, and prompt a re-examination of the data and the mechanisms behind its recent successes in frontier post-training.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zixuan Fu, Bingxiang He, Yuxin Zuo, Haohuan Huang, Jinqian Zhang, Ruhang Xiao, Cheng Qian, Qinyu Luo, Huan-ang Gao, Yudong Wang, Zhiyuan Liu, Ning Ding, Chaojun Xiao
- 发布：2026-09-03；更新：2026-09-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
