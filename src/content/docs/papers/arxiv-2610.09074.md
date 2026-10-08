---
title: "TAP: Efficient Long-Horizon Agent Pruning via Trajectory-Anchored Recovery"
description: "Emerging long-horizon agentic tasks require repeated model calls, worsening the inference cost of already-costly language models."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.09074) · [PDF](https://arxiv.org/pdf/2610.09074)

## 一句话摘要

Emerging long-horizon agentic tasks require repeated model calls, worsening the inference cost of already-costly language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Emerging long-horizon agentic tasks require repeated model calls, worsening the inference cost of already-costly language models. While narrow agentic tasks suggest potential for aggressive model pruning without performance drop, empirical results show existing methods proposed for question answering tasks severely degrade task performance when applied to agentic models. We trace this failure to two decisions: what to prune and how to recover. For pruning, one-shot importance estimates fail to track how the pruned model adapts. For recovery, offline distillation covers only teacher prefixes, while full-trajectory on-policy distillation causes student errors to compound across turns. In this work, we propose Trajectory-Anchored Pruning (TAP), the first structural pruning framework for reinforcement learning (RL)-trained agents. TAP couples structural pruning with efficient on-policy recovery, anchoring interactions to teacher trajectories while allowing the student to generate each reasoning-action response. A frozen dense teacher supervises the student's response prefixes, addressing within-response training-inference mismatch while preventing student-induced deviations from propagating across training turns. Instead of one-shot pruning, TAP re-scores channels using gradients of the recovery objective on the recovered student, connecting iterative channel selection to the evolving policy. With 60% of FFN channels removed, TAP retains 99.2% and 88.0% of the dense 7B agents' task success rates on ALFWorld and WebShop, respectively, while reducing GPU time per successful task by approximately 22% and 17%. These results demonstrate effective structural compression of long-horizon agents under a limited recovery budget.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation, pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuanzhe Li, Pengxin Wang, Yuxin Ren, Jianing Deng, Jingtong Hu, Song Wang, Jingdi Chen, Huanrui Yang
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
