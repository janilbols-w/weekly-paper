---
title: "Input-Layer Starvation: Why Per-Layer Pruning Breaks IoT Intrusion Detectors"
description: "Intrusion detectors for small Internet-of-Things (IoT) devices are usually compressed by pruning and judged by overall accuracy."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.30729) · [PDF](https://arxiv.org/pdf/2609.30729)

## 一句话摘要

Intrusion detectors for small Internet-of-Things (IoT) devices are usually compressed by pruning and judged by overall accuracy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Intrusion detectors for small Internet-of-Things (IoT) devices are usually compressed by pruning and judged by overall accuracy. We show that this hides a severe class-level failure, find its cause, and give low-overhead prevention and repair. On CICIoT2023, a two-layer convolutional detector pruned with uniform layer-wise magnitude pruning at 80% sparsity loses 16 points of accuracy but half of its macro-F1, the mean per-class F1 (0.542 to 0.271 over five independently trained models); 17 of 34 classes are materially damaged. Remaining weight count does not explain it: a perceptron and a transformer pruned to the same or fewer weights lose at most 0.096. The first layer does. It has 192 weights; uniform pruning leaves 38, 46% of its 64 filters lose every input weight, and fine-tuning under that starvation leaves the running means of the first normalisation layer displaced by up to 0.8 standard deviations in a few surviving channels, on which the deployed model collapses. Protecting those 192 weights, or pruning globally at the same sparsity, prevents the collapse (loss 0.013); recomputing the normalisation statistics on unlabelled training data, with no weight changed, repairs it (loss 0.039) and returns the false-alert rate to 33% (dense 29%). Damage shows a strong increasing dose-response in first-layer sparsity, starving a perceptron's input layer reproduces the collapse, and the pattern holds on TON_IoT. The failure is misattribution and false alerts, not silent evasion: on validation-selected blind spots, uniformly pruned detectors misattribute 72% of the traffic, against 50% with the first layer protected and 47% for the dense model.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Md Anas Biswas
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
