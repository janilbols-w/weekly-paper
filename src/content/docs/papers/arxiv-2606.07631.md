---
title: "Trait-space Monitoring for Emergent Misalignment During Supervised Finetuning"
description: "Emergent misalignment (EM) occurs when narrow finetuning induces dangerous behavior outside the finetuning task."
---

**评分：40/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2606.07631) · [PDF](https://arxiv.org/pdf/2606.07631)

## 一句话摘要

Emergent misalignment (EM) occurs when narrow finetuning induces dangerous behavior outside the finetuning task.

## 为什么值得关注

待编辑增强。

## 摘要原文

Emergent misalignment (EM) occurs when narrow finetuning induces dangerous behavior outside the finetuning task. Detecting this shift through repeated behavioral evaluation is costly, motivating our checkpoint-level monitoring from internal representations. We define a fixed coordinate system from seven alignment-relevant activation directions and use it to track representational drift during LoRA finetuning of four open-source 7-9B language models. Finetuning drift in this space exhibits a dominant axis that explains 78.6% of variance and remains stable across datasets, extraction choices, and parameter-update capacities. Across 468 checkpoints from three EM-relevant held-out datasets, the resulting monitors attain 1.8% FNR, 2.0% FPR, and 0.989 AUROC, outperforming semantic, random, PCA, and SAE feature baselines. On a fourth dataset, a matched benign-dangerous control shows that substantial representational drift can also occur under benign finetuning, while changes across the 7D profile still distinguish dangerous from benign runs. Stress tests across two 14B models, full finetuning, longer training horizons, and misaligned starting states show that the signal can persist across shifts in training configuration, while reliable deployment may require recalibration.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Huy Nghiem, Sy-Tuyen Ho, Sarah Wiegreffe, Hal Daum\'e III
- 发布：2026-10-02；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
