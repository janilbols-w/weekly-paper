---
title: "Do We Really Need KL Divergence for On-Policy Distillation of Large Language Models?"
description: "Since the advent of knowledge distillation, KL divergence has been the standard loss in distillation."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.33791) · [PDF](https://arxiv.org/pdf/2609.33791)

## 一句话摘要

Since the advent of knowledge distillation, KL divergence has been the standard loss in distillation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Since the advent of knowledge distillation, KL divergence has been the standard loss in distillation. Recently, on-policy distillation (OPD) has emerged as an efficient post-training paradigm for LLMs. As a distillation method, OPD naturally inherits KL divergence as its standard loss. However, in this work, we find that KL divergence may not be necessary for OPD. We show that simply preserving the update direction is sufficient for effective OPD. As long as the update direction is toward the teacher, OPD works. More precisely, it is not the direction of every token, but the direction of a small subset of tokens where the teacher and student disagree strongly. We first show that simply assigning a reward of (+1) to tokens where the teacher probability is higher than the student probability and (-1) where it is lower, which merely encourages updates toward the teacher, reproduces almost the same training mode as OPD with reverse KL. We further show that only the direction of a small subset of tokens with large teacher-student disagreement is critical, and training works as long as their update direction is toward the teacher, even if other tokens are pulled away from the teacher. And as an application of these findings, we introduce Consensus Multi-Teacher On-Policy Distillation (C-MOPD) to improve Multi-Teacher On-Policy Distillation (MOPD). Unlike MOPD, which routes each sample to a single teacher and may cause capability conflicts across domains, C-MOPD lets every sample be supervised by all teachers. Experiments show that C-MOPD consistently outperforms MOPD on both math and code benchmarks. Our code is available at https://github.com/LeapLabTHU/KL-Free-OPD.

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

- 作者：Wenze Lin, Jiyuan Long, Jiale Zhao, Shenzhi Wang, Xitai Jiang, Ce Luo, Rui Lan, Qianli Ma, Fukang Wen, Hui Wu, Liyuan Chen, Shuoling Liu, Jiangpeng Yan, Gao Huang
- 发布：2026-09-27；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/LeapLabTHU/KL-Free-OPD](https://github.com/LeapLabTHU/KL-Free-OPD)
- 阅读深度：metadata
