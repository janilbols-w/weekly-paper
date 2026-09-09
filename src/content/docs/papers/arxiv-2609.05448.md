---
title: "Damage-Aware Bandit Pruning for Vision and Language Transformers"
description: "Structured post-training pruning of transformers requires selecting complete functional units whose suppression causes limited degradation."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.05448) · [PDF](https://arxiv.org/pdf/2609.05448)

## 一句话摘要

Structured post-training pruning of transformers requires selecting complete functional units whose suppression causes limited degradation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Structured post-training pruning of transformers requires selecting complete functional units whose suppression causes limited degradation. We formulate structured-unit selection for language and vision transformers as a damage-aware multi-armed bandit problem under a fixed candidate-evaluation budget. Attention heads and MLP channel groups are temporarily masked on calibration batches. Paired damage is the masked loss minus the base loss on the same batch, reducing batch-to-batch variation. A smooth bounded reward drives either a UCB-style policy or fractional-Beta Thompson Sampling, and the final mask is constructed sequentially by adding one unit at each step. The selected units are functionally zeroed in the original dense checkpoint; therefore, the reported parameter effects represent effective structural suppression rather than physical compression or measured speedup. Experiments on WikiText-2, LAMBADA, and Imagenette cover GPT-2, OPT, Pythia, Qwen2.5, SmolLM2, ViT-B/16, DeiT-Tiny, and Swin-Tiny, with comparisons against random, magnitude, static-saliency, and budgeted-greedy selection. Across five seeds, the bandit methods usually reduce degradation relative to budgeted greedy in the paired language-model comparisons. Of 28 comparisons highlighted in the paper, 23 bootstrap confidence intervals exclude zero and 11 paired tests have p < 0.05; six have q < 0.05 after Benjamini-Hochberg correction across the full family of 116 dataset-wise tests. Matched-evaluation results for ViT-B/16 and Swin-Tiny indicate that their gains are not explained solely by a larger candidate-evaluation budget.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Salem Ameen, Sunil Vadera
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
