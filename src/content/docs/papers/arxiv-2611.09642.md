---
title: "NAVE: A Normalized, Adaptive Conformer for Antarctic Whale Vocalization Detection"
description: "Antarctic whale vocalization detection requires temporally localizing call boundaries in long underwater recordings and classifying them into predefined call types."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.09642) · [PDF](https://arxiv.org/pdf/2611.09642)

## 一句话摘要

Antarctic whale vocalization detection requires temporally localizing call boundaries in long underwater recordings and classifying them into predefined call types.

## 为什么值得关注

待编辑增强。

## 摘要原文

Antarctic whale vocalization detection requires temporally localizing call boundaries in long underwater recordings and classifying them into predefined call types. Training reliable machine learning models for this task is difficult due to the variability and sparsity of whale calls in passive acoustic monitoring datasets. These difficulties are further amplified by time-varying noise that can mask whale calls and by site-specific ambient sound characteristics to which a trained model may not generalize. In this work, we present NAVE, a Conformer-based detector that improves whale-call detection via three components. First, its input representation combines per-bin complex mean subtraction, which suppresses constant site-specific ambient sound characteristics, with an additional per-channel energy normalization (PCEN) channel that adapts to temporal variations in the noise floor. Second, a frequency-dynamic stem processes these noise-aware representations with convolutions that adapt across the characteristic frequency bands of the target call types. Third, we use a Conformer backbone with a convolution kernel matched to the duration of the target calls that adds an inductive bias and improves temporal localization. We evaluate NAVE on BioDCASE 2026 Task 2 using leave-one-site-out cross-validation across the validation sites, which approximates deployment on unseen recording sites. A single NAVE model with a tuned per-class threshold exceeds the stronger WhaleVAD-BPN baseline, using no boundary-proposal network and no search over post-processing parameters. A controlled ablation study shows that the normalized front-end and a duration-matched convolutional kernel each contribute substantially to recovering the D downsweep, the hardest class for previous detectors, with the wide kernel giving the largest aggregate gain.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Matthias Nagl, Paul Primus, Gerhard Widmer
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
