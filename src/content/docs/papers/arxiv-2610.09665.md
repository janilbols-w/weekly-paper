---
title: "SAPD: Step-Aligned Privileged Distillation"
description: "On-policy post-training can improve large language models by learning from their own trajectories, but requires costly rollout generation."
---

**评分：53/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.09665) · [PDF](https://arxiv.org/pdf/2610.09665)

## 一句话摘要

On-policy post-training can improve large language models by learning from their own trajectories, but requires costly rollout generation.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy post-training can improve large language models by learning from their own trajectories, but requires costly rollout generation. We ask whether fixed demonstrations can support competitive off-policy learning through better supervision. Our premise is that their usefulness depends not only on the training trajectories, but also on whether supervision provides informative preferences among continuations and connects this guidance to the reasoning decision being learned. We introduce Step-Aligned Privileged Distillation (SAPD), a rollout-free self-distillation method that turns demonstrations into step-aligned distributional supervision. Its key insight is to use the known progression of a reference solution to associate each reasoning transition with targeted privileged guidance, rather than treating the solution as undifferentiated context. On mathematical reasoning benchmarks, SAPD outperforms supervised fine-tuning and label smoothing on average while remaining competitive with on-policy reinforcement learning and self-distillation. Analyses support both the value of context-dependent distributional guidance and the benefit of aligning privileged information with the current step. SAPD also largely preserves out-of-domain coding performance and achieves approximately 2x training-loop speedups over the on-policy baselines. These findings suggest that carefully constructed supervision can make fully off-policy post-training a competitive and computationally efficient alternative. Our code is available at https://github.com/Miaow-Lab/SAPD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Tianle Wang, Jiayu Liu, Ruizhi Zhao, Ning Miao
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Miaow-Lab/SAPD](https://github.com/Miaow-Lab/SAPD)
- 阅读深度：metadata
