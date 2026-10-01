---
title: "ReSAIL: Mitigating Collapse in Iterative Agent Self-Distillation"
description: "Iterative self-distillation enables LLM agents to learn from successive deployments, offering a path toward recursive self-improvement (RSI)."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.39306) · [PDF](https://arxiv.org/pdf/2609.39306)

## 一句话摘要

Iterative self-distillation enables LLM agents to learn from successive deployments, offering a path toward recursive self-improvement (RSI).

## 为什么值得关注

待编辑增强。

## 摘要原文

Iterative self-distillation enables LLM agents to learn from successive deployments, offering a path toward recursive self-improvement (RSI). Yet our experiments with existing methods reveal a collapse in deployment performance across cycles, while task performance with privileged information (PI) also declines. We address this collapse by prioritizing informative interaction steps for distillation and preserving PI-conditioned behavior as the student becomes the next teacher. We introduce Retentive and Selective Augmentation for Iterative Self-Distillation (ReSAIL), a plug-in augmentation for iterative PI-based self-distillation. ReSAIL selects interaction steps where PI most strongly changes the teacher's predictions and balances the resulting distillation losses across trajectories. It also regularizes the student's PI-conditioned output distributions toward those of the frozen teacher at selected and unselected steps to preserve PI-conditioned behavior for supervision in the next cycle. On ALFWorld and TextCraft, ReSAIL sustains substantial gains across model scales over three cycles, with an average absolute gain of 22.5% in final-cycle success rates when added to self-distillation baselines. Sensitivity-guided selection of offline data also improves action prediction accuracy for multimodal GUI agents on AITZ. These findings provide the first evidence that a more robust learning mechanism can effectively mitigate performance collapse in iterative agent self-distillation over deployment trajectories.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shengjie Jin, Hengbo Xu, Zelong Sun, YuJie Guo, Zhiwu Lu
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
