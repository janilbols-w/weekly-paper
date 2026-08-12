---
title: "Wiring Beats Blending: What Transfers Between Transformer Sizes -- and What Doesn't"
description: "Model families are typically trained size by size, each from scratch."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.02829) · [PDF](https://arxiv.org/pdf/2608.02829)

## 一句话摘要

Model families are typically trained size by size, each from scratch.

## 为什么值得关注

待编辑增强。

## 摘要原文

Model families are typically trained size by size, each from scratch. Can apretrained large model instead be converted into a smaller sibling? Wecharacterize the 1.4B->410M conversion in the Pythia family end to end.Representations align strongly across sizes (ridge R^2=0.84) while parametersalign weakly. Dense weight projection is functionally destructive, and abit-exact reconstruction control shows this is not an assembly artifact: basismixing breaks rotary, per-head, GELU, and LayerNorm structure. After the best-fitlinear operator, weight residuals are statistically indistinguishable from noiseunder shuffle controls. Conversion value therefore lives in initialization. Inmatched-budget continued pre-training we decompose conversion into twoindependent levers: least-squares compensation (a function lever, best zero-shot)and variance-preserving rescale (a dynamics lever, best endpoints). Compensationis a token-efficient, low-budget win rather than a universal one. At 30M tokens itbeats the strongest subcloning variant on both a width-reduced pair (84.0 +/- 1.8vs. 89.7 +/- 3.7, 3/3 seeds) and a held-out depth-reduced pair (109.3 vs. 117.9,3/3 seeds), reaching a given quality with fewer tokens. At a 33x larger budget thetwo converge to parity (40.0 vs. 40.0), both far ahead of from-scratch, whichtransfer initialization always beats: by up to 18x at low budget, with the marginnarrowing at convergence and at the largest scale. We also map the method'sboundary. At about 5x the donor scale (6.9B->1.4B) stacking both leversover-corrects, consistent with ill-conditioning of the compensation solve at largewidth, which points to dimension-aware regularization as a fix. At matched budgetour initialization also beats structured pruning with distillation, the standardpipeline for this task, and improves further when combined with it. Code,checkpoints, and the frozen evaluation corpus are released.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 8 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation, pruning
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Ravi Satya Durga Prasad Yenugula
- 发布：2026-08-12；更新：2026-08-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
