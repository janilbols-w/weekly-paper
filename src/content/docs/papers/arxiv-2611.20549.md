---
title: "RoShift: Lazy Shift and Weight-aware Rotation for Activation Sparsity in LLM Inference"
description: "Activation sparsity accelerates LLM decoding by skipping unnecessary weight reads and computation."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.20549) · [PDF](https://arxiv.org/pdf/2611.20549)

## 一句话摘要

Activation sparsity accelerates LLM decoding by skipping unnecessary weight reads and computation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Activation sparsity accelerates LLM decoding by skipping unnecessary weight reads and computation. However, SiLU-based LLMs exhibit little natural sparsity, and imposing high sparsity can substantially degrade accuracy. We propose RoShift, a training-free method that transforms activations into sparsity-friendly representations. RoShift introduces lazy shift, which recenters SiLU activation distributions around zero and defers correction to the end of the FFN to obtain additional sparsity. It also reduces sparsification-induced output error through rotation that jointly accounts for activation and weight information. By fusing the corrections required for shifting and rotation, RoShift translates these gains into decoding speedup. At 50% and 60% sparsity, RoShift improves average accuracy over TEAL by 1.60 and 3.29 percentage points, respectively, across five models. It achieves up to $1.72\times$ decoding speedup over the dense model on an RTX 5090 at 50% sparsity and yields a better accuracy-speedup Pareto frontier than TEAL. Code is available at https://github.com/hulahula3247/RoShift

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Geunsoo Song, Jiwon Seo, Hoeseok Yang, Youngmin Yi
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/hulahula3247/RoShift](https://github.com/hulahula3247/RoShift)
- 阅读深度：metadata
