---
title: "Revisiting On-policy Adversarial Black-Box Distillation: Calibrating Groupwise Reward Geometry for Effective Advantage Construction"
description: "Black-box distillation is a practical route for transferring capabilities from API-accessible large language models that expose only text outputs into smaller student models."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.39757) · [PDF](https://arxiv.org/pdf/2609.39757)

## 一句话摘要

Black-box distillation is a practical route for transferring capabilities from API-accessible large language models that expose only text outputs into smaller student models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Black-box distillation is a practical route for transferring capabilities from API-accessible large language models that expose only text outputs into smaller student models. Recent on-policy adversarial methods such as GAD improve over SeqKD by forming an adversarial loop between a critic and a student, where the critic provides rewards for GRPO-based student policy optimization over the student's sampled responses. However, GRPO computes advantages from the within-group relative rewards of student samples for the same prompt, whereas the critic is trained primarily to distinguish teacher responses from student responses. This objective mismatch can produce reward groups with collapsed scale or fragile margins, leading to brittle grouped optimization signals. We propose Groupwise Reward Geometry Conditioning (GRGC), a two-stage framework that improves advantage construction by shaping student-side reward groups during both critic training and policy optimization. To improve critic-side conditioning, Gaussian groupwise Optimal Transport calibration regularizes the critic during training to produce reward groups with non-collapsed spread and smooth rank-wise gaps by matching sorted prompt-wise rewards to group-centered Gaussian quantiles. Building on this conditioned reward geometry, policy-side group power modulation reshapes the prompt-wise reward groups before they are converted into advantages, preserving the critic-induced ordering while increasing optimization-relevant margin separability. Extensive experiments across diverse teachers, student model families and scales, and training datasets demonstrate the effectiveness of GRGC on both in-distribution and out-of-distribution evaluations, while introducing negligible overhead over GAD. The code is available at https://github.com/2018cx/GRGC.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Xiao Cui, Mo Zhu, Yulei Qin, Yuze Wu, Wengang Zhou, Houqiang Li
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/2018cx/GRGC](https://github.com/2018cx/GRGC)
- 阅读深度：metadata
