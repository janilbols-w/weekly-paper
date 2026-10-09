---
title: "ReCal: Calibrating Structured Pruning for On-Policy Distillation Recovery"
description: "Structured pruning reduces the deployment cost of reasoning language models, but the resulting capability degradation can hinder subsequent on-policy distillation (OPD) recovery."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.11332) · [PDF](https://arxiv.org/pdf/2610.11332)

## 一句话摘要

Structured pruning reduces the deployment cost of reasoning language models, but the resulting capability degradation can hinder subsequent on-policy distillation (OPD) recovery.

## 为什么值得关注

待编辑增强。

## 摘要原文

Structured pruning reduces the deployment cost of reasoning language models, but the resulting capability degradation can hinder subsequent on-policy distillation (OPD) recovery. Because OPD relies on student-generated trajectories, pruning damage that persists after offline distillation can limit its effectiveness. We propose RECAL, Recovery-Aware Calibration, a simple plug-and-play approach that improves OPD recovery by adjusting calibration before pruning. RECAL uses forward KL between an unpruned teacher and a pruned probe to identify teacher-supported predictions disrupted by pruning, then reweights calibration statistics to guide existing pruning criteria toward preserving these predictions. Across multiple models and pruning methods, RECAL consistently improves mathematical reasoning after OPD, achieving gains of up to 16.7 percentage points on AIME, alongside improvements in most code-generation comparisons. Further analysis shows that RECAL reduces residual damage at heavily affected tokens and establishes performance advantages that persist through recovery. These results demonstrate the value of recovery-aware calibration for improving on-policy distillation recovery of pruned reasoning models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation, pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Houcheng Jiang, Mao Zheng, Mingyang Song, Qiyong Zhong, Jie Sun, Tianyu Zhang, Junfeng Fang
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
