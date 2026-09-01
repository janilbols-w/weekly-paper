---
title: "Evaluating Tiny Recursive Models Across Training for Code Generation"
description: "Code generation increasingly relies on large transformer models, whose capability advances with scale."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2608.29376) · [PDF](https://arxiv.org/pdf/2608.29376)

## 一句话摘要

Code generation increasingly relies on large transformer models, whose capability advances with scale.

## 为什么值得关注

待编辑增强。

## 摘要原文

Code generation increasingly relies on large transformer models, whose capability advances with scale. Yet such a scale is costly, creating demand for small models, especially where data is limited. Recursive models address this by reusing a single block to add depth rather than stacking independent layers. Such models are typically evaluated by teacher-forced fit (next-token loss on ground-truth prefixes) or task accuracy, at a single checkpoint, whereas code is produced by free-running generation, where the model extends its own output. Whether a teacher-forced advantage survives free-running generation, and whether it holds across training, remains open. To study both, we compare a ~28M-parameter autoregressive Tiny Recursive Model (TRM-AR) on natural-language-to-Python code generation against parameter-matched and depth-matched controls, tracking fit and generation across 40 epochs and three seeds. The fit ranking between the recursive model and the depth-matched control reverses twice. Selecting each checkpoint by validation loss and examining the trajectory yields a consistent comparison. At equal parameters, TRM-AR fits, generates, and generalizes better than the parameter-matched control while recovering approximately 45% of the validation-loss gap and 57% of the generation-quality gap between the two controls, at roughly 175 times the per-step cost of the parameter-matched control. However, at equal effective depth, the larger transformer fits and generates better at its validation optimum, suggesting TRM-AR's advantage lies in resistance to overfitting, not greater capability. These findings suggest that recursive code generation models should be evaluated jointly on fit and generation across the training trajectory rather than at a single checkpoint.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Anjani Sirivella, Aanisha Newaz, Glaucia Melo
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
