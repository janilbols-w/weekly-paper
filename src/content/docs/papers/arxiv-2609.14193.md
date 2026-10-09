---
title: "Data-Free On-Policy Distillation: How Far Can We Go Without External Data?"
description: "On-policy distillation (OPD) is increasingly applied to frontier foundation model post-training."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.14193) · [PDF](https://arxiv.org/pdf/2609.14193)

## 一句话摘要

On-policy distillation (OPD) is increasingly applied to frontier foundation model post-training.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) is increasingly applied to frontier foundation model post-training. Prior work in this area has largely focused on algorithmic advances, yet it remains unclear how much OPD depends on its training questions and, in particular, how far this dependence can be reduced. Across two representative single-teacher OPD settings, we find that training on 8 real prompts yields performance comparable to training on 17k problems, while datasets differing substantially in measured difficulty and initial distillation gap yield similar outcomes. Our analyses suggest two complementary explanations: repeated sampling could allow even a few prompts to expose substantial teacher supervision, while OPD transfers generalizable reasoning capabilities beyond dataset-specific knowledge. Building on these observations, we next propose a data-free on-policy distillation (DF-OPD) setting to investigate whether the system can supply the training questions itself, eliminating the need for external data. With 64 self-generated questions obtained without seed examples, DF-OPD yields performance comparable to full-data OPD in both single-teacher settings. This finding also holds in multi-teacher OPD: across mathematics, code, and instruction following, 1k generated questions achieve performance comparable to training on approximately 7k real post-training examples. We further explore whether OPD can operate even without explicit training questions. The experiments show that this is effective only in limited cases, where the student unexpectedly generates and answers its own questions, thereby reducing the process to an implicit form of DF-OPD. Together, these findings invite a reassessment of the role of training data in on-policy distillation. Code is available at https://github.com/Ryuki661/DF-OPD

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Gengsheng Li, Mao Zheng, Mingyang Song, Jie Sun, Zeyuan Liu, Ruiqi Liu, Tianyu Yang, Qiyong Zhong, Haiyun Guo, Junfeng Fang, Shiming Xiang, Jinqiao Wang, Tat-Seng Chua
- 发布：2026-10-06；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Ryuki661/DF-OPD](https://github.com/Ryuki661/DF-OPD)
- 阅读深度：metadata
