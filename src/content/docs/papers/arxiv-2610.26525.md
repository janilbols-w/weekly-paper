---
title: "A Fisher-Geometric View of Multi-Teacher On-Policy Distillation"
description: "Consolidating specialized foundation models into a unified generalist is a central goal of post-training."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.26525) · [PDF](https://arxiv.org/pdf/2610.26525)

## 一句话摘要

Consolidating specialized foundation models into a unified generalist is a central goal of post-training.

## 为什么值得关注

待编辑增强。

## 摘要原文

Consolidating specialized foundation models into a unified generalist is a central goal of post-training. Two approaches are in common use: model merging, which is fast but treated as a heuristic, and multi-teacher on-policy distillation, which matches distributions but demands heavy rollout compute and suffers from cross-task gradient conflict. We show that the two are one objective seen at different orders. Within a shared basin of homologous specialists, the multi-teacher on-policy distillation objective is, to second order, exactly the Fisher-merging objective. Its minimizer is therefore the Fisher merge, a classic model-merging method given by a closed-form combination of the specialists, so merging is optimal, to second order, as a closed-form stage of distillation. Building on this identification, we propose Residual-Governed Branch-and-Merge(RGBM), a two-phase consolidation procedure. Concretely, a full-parameter Fisher merge is intractable on foundation models, so Phase~1 restricts the merge to the task-vector subspace. Extending tangent-space analyses of merging, we show that the same coefficients that mix task vectors also mix implicit rewards, which lets a residual program on unlabelled prompts solve for them. The program minimizes the worst per-domain residual and reports its energy-normalized values as the domain residual spectrum. Phase~2 lets this spectrum govern what may be added: RGBM passivates domains with low normalized residuals, trains isolated branches only for domains above the spectral gap, and writes back the admitted updates with calibrated shrinkage. On two open-source consolidation suites, the Phase~1 merge alone matches or outperforms fully trained multi-teacher distillation, and RGBM improves on it further with zero extra joint-training steps, whereas every un-gated write-back, including continued joint distillation from the merge, falls below it.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Liu Kaiyuan, Zhuang Ziyuan, Ma Haoxuan, Gu Yannian, Song Mingfei, Weng Rongxiang, Ye Jieping
- 发布：2026-10-20；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
