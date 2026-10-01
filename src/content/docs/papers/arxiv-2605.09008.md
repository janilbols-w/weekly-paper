---
title: "Relative Kinetic Utility: Calibrating Cross-Layer Credit for Global Structured LLM Pruning"
description: "Global structured pruning requires channels from different layers to compete under a shared sparsity budget, raising two coupled challenges: identifying which channels should be retained and making their scores comparable across layers."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.09008) · [PDF](https://arxiv.org/pdf/2605.09008)

## 一句话摘要

Global structured pruning requires channels from different layers to compete under a shared sparsity budget, raising two coupled challenges: identifying which channels should be retained and making their scores comparable across layers.

## 为什么值得关注

待编辑增强。

## 摘要原文

Global structured pruning requires channels from different layers to compete under a shared sparsity budget, raising two coupled challenges: identifying which channels should be retained and making their scores comparable across layers. Raw channel scores can contain block-common scale that leaves within-block ordering unchanged but distorts model-wide competition. Our experiment indicates that similar layer-wise allocations can retain substantially different FFN channels, so layer allocation alone does not determine channel identity. Motivated by this separation, we introduce Global Relative Kinetic Utility (Global RKU), a label-free criterion that separates channel importance estimation from cross-layer comparison. Global RKU measures channel participation using a final-hidden-state activation-gradient signal, then applies block-relative normalization to mitigate block-common scale while preserving within-block ordering, requires only unlabeled calibration inputs, and produces a static pruning topology in a single calibration stage. Under questions-only calibration on Qwen-2.5-7B, RKU-GISP Mean3 margins are -0.98, +3.79, and +8.61 points at 30%, 40%, and 50% sparsity, respectively (average +3.81). Additional Qwen evaluations cover non-mathematical reasoning, recovery, held-out transfer, and physical deployment. Separately, replacing Wiki16K with questions-only Q16K improves RKU's Mean3 at every tested sparsity on Qwen, Llama, and Gemma. Our ablation study shows relative-normalization gains of 14.42 and 5.53 Mean3 points at 40% and 50% sparsity, respectively; the common-seed audit is positive in all 27 seed-task comparisons.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tianhao Qian, Guilin Qi, Jiayu Chen
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
