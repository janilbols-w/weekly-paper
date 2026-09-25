---
title: "Baseline Shape Decides the Verdict: A Controlled Re-Examination of Ternary Language Models at 60K Parameters"
description: "Ternary (1.58-bit) weights are attractive for microcontroller-class language models, but the sub-1M-parameter regime rests mainly on isolated, single-seed comparisons."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.29397) · [PDF](https://arxiv.org/pdf/2609.29397)

## 一句话摘要

Ternary (1.58-bit) weights are attractive for microcontroller-class language models, but the sub-1M-parameter regime rests mainly on isolated, single-seed comparisons.

## 为什么值得关注

待编辑增强。

## 摘要原文

Ternary (1.58-bit) weights are attractive for microcontroller-class language models, but the sub-1M-parameter regime rests mainly on isolated, single-seed comparisons. One prominent example reports that a routed ternary block (convolution, diagonal SSM and sparse attention mixed by a per-token router) beats a parameter-matched full-precision transformer by 22% at 60K parameters, attributing this to inductive bias. We re-run it under one fixed recipe, three seeds per cell, 98 byte-level runs on one laptop. (i) Baseline shape dominates: at a 16M-byte budget, param-matched transformers span 22.6% in validation loss purely by depth/width choice - far more than any architecture effect we measure there - and the best-shaped transformer ties the routed model, so the published margin is at least partly a baseline-shape effect; the ordering of shapes reverses with budget, so no single fixed shape can be trusted. (ii) At 130M bytes the routed model does win, by 22.2-24.0% over the three transformer shapes we evaluate there - but a plain gated diagonal-SSM block beats it by a further 9.1%, and the routed model's own router puts most of its weight on its recurrent pathway, so the gain does not require routing. (iii) The ternary penalty differs by architecture at the larger budget (+5.3% best transformer vs. +19.5% routed, +28.1% gated SSM), but we cannot attribute that to architecture alone: our transformers keep learned positional embeddings in full precision, 11-22% of their parameters, so they are less quantized than the models they are compared with. (iv) A 90/10 full-precision-then-ternary schedule beats all-ternary training, but only at a stage-2 learning rate about 10x the pretraining peak; at a conventional fine-tuning rate it looks 15.3% worse, reversing the conclusion. The from-scratch baseline was not itself learning-rate tuned, which bounds (iii) and (iv). Code and run logs released.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Gautam Veldanda
- 发布：2026-09-24；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/veldanda/ByteLM](https://github.com/veldanda/ByteLM)
- 阅读深度：metadata
