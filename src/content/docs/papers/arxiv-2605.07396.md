---
title: "Rethinking Black-Box On-Policy Distillation: A Rubric-based Analysis"
description: "On-policy distillation (OPD) is a powerful paradigm for LLM post-training, yet its reliance on teacher logits restricts it to white-box teachers."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.07396) · [PDF](https://arxiv.org/pdf/2605.07396)

## 一句话摘要

On-policy distillation (OPD) is a powerful paradigm for LLM post-training, yet its reliance on teacher logits restricts it to white-box teachers.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) is a powerful paradigm for LLM post-training, yet its reliance on teacher logits restricts it to white-box teachers. In this paper, we study whether rubric-based supervision can provide a text-only feedback interface for black-box OPD, and what makes it effective. Our instantiation, Rubric-based On-Policy Distillation (ROPD), induces rubrics by contrasting teacher responses with the student's current rollouts and uses them to score these rollouts for on-policy optimization. We find that, under matched settings, text-only ROPD outperforms logit-based OPD methods on four competition-math benchmarks, reaching the best AIME24 accuracy of standard logit-based OPD with 9.6x fewer training samples. Our analysis yields three findings: rubric rewards track correctness far better than teacher log-likelihood (AUC 0.90 vs. 0.35); training with them repairs more failed criteria and regresses fewer passed ones than logit-based supervision; and contrasting teacher responses with student rollouts is central to rubric quality. These results position rubric-based OPD as a flexible, black-box-compatible alternative to logit-based OPD. Our implementation is available at https://github.com/Peregrine123/ROPD_official.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 8 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Zhepei Hong, Yukai Wang, Mao Zheng, Mingyang Song, Gengsheng Li, Houcheng Jiang, Dan Zhang, Haiyun Guo, Junfeng Fang, Tat-Seng Chua
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Peregrine123/ROPD_official](https://github.com/Peregrine123/ROPD_official)
- 阅读深度：metadata
