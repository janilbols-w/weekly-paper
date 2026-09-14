---
title: "DASH-OPD: Discrepancy-Aware Switching with Hysteresis for On-Policy Distillation"
description: "While on-policy distillation (OPD) reduces exposure bias by training student language models on their own rollouts, early student errors in long-horizon agentic scenarios can lead to contexts unfamiliar to the teacher."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.29078) · [PDF](https://arxiv.org/pdf/2607.29078)

## 一句话摘要

While on-policy distillation (OPD) reduces exposure bias by training student language models on their own rollouts, early student errors in long-horizon agentic scenarios can lead to contexts unfamiliar to the teacher.

## 为什么值得关注

待编辑增强。

## 摘要原文

While on-policy distillation (OPD) reduces exposure bias by training student language models on their own rollouts, early student errors in long-horizon agentic scenarios can lead to contexts unfamiliar to the teacher. To improve trajectory quality, recent work on agentic OPD introduces teacher intervention into training rollouts by switching the executor between the student and the teacher. However, existing methods determine how much teacher intervention is needed---but not when. To address this limitation, we propose DASH-OPD (Discrepancy-Aware Switching with Hysteresis for OPD), the first agentic OPD method to perform adaptive, bidirectional executor switching. At each turn, DASH-OPD measures teacher--student discrepancy using a mean log-probability ratio over action tokens. Student-to-teacher ratios on student turns serve as drift signals, while teacher-to-student ratios on teacher turns serve as recovery signals. These signals are accumulated over multiple turns to form drift and recovery evidence, respectively. DASH-OPD switches executors when either type of evidence exceeds its corresponding switching threshold, introducing hysteresis that prevents rapid switching triggered by transient discrepancy fluctuations. Across three benchmarks and two student model sizes, DASH-OPD outperforms five baselines in all 14 task performance comparisons, while requiring the fewest interaction turns in nine of ten efficiency comparisons. Code, models, and training logs are available at https://github.com/Lucian1115/DASH-OPD

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yuchen Xia, Qianguo Sun, Chao Song, Junlong Wu, Yiyan Qi, Yunjian Xu
- 发布：2026-09-14；更新：2026-09-14
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Lucian1115/DASH-OPD](https://github.com/Lucian1115/DASH-OPD)
- 阅读深度：metadata
