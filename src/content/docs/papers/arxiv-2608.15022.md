---
title: "Gathered, Not Admitted: How Attention Brings a Latent Variable into Verbalizable Form"
description: "Language models hold latent quantities in a form they can report on, and more of a quantity is present in that form when the task requires reusing it flexibly."
---

**评分：42/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](http://arxiv.org/abs/2608.15022v1) · [PDF](https://arxiv.org/pdf/2608.15022v1)

## 一句话摘要

Language models hold latent quantities in a form they can report on, and more of a quantity is present in that form when the task requires reusing it flexibly.

## 为什么值得关注

待编辑增强。

## 摘要原文

Language models hold latent quantities in a form they can report on, and more of a quantity is present in that form when the task requires reusing it flexibly. What causes a representation to enter that form is open, and the word workspace invites an admission story: a gate that decides what gets in. Testing it on open-weight models with Jacobian lenses, over a benchmark whose five arms share an identical context, we find no gate where it predicts one. Demand raises a concept's lens visibility beyond what applying an operator to a supplied value produces: +0.050 [+0.045, +0.057] in percentile rank on our primary checkpoint, positive on all four we measure, though that arm answers at ceiling and the accuracymatched contrast is stronger under that readout. At the same time one shared linear map decodes the variable from every arm, the control included, at 6.4-9.0x its selection-corrected floor. What produces the later readable form at the queried position is attention-mediated gathering inside a mid-depth window: separating patch depth from readout depth puts transport there at least 17x above anywhere shallower under non-saturating readouts, with no tested MLP output contributing positively inside it. Under the saturating percentile rank the same grid does not localise the window, which is a fact about that measure. An arm that needs the variable for nothing concentrates sevenfold less, so the window is demand-specific. That window has two measured edges, a survival failure below and destruction above, and it falls at the same fractional depth in a 64-layer hybrid and a 62-layer dense model from another family. We localise where the variable is installed and read, not the route from the passage, which transports nothing. But the readout is not a calibrated measure of use: three components move it to within 12% of one another and differ 7.4x in what they do to the answer.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 8 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Parsa Mazaheri
- 发布：2026-08-15；更新：2026-08-15
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/parsa-mz/innerj](https://github.com/parsa-mz/innerj)
- 阅读深度：metadata
