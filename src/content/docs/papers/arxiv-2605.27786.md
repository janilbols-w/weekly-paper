---
title: "Locality-Aware Redundancy Pruning for LLM Depth Compression"
description: "Large language models are known to contain representational redundancy across network depth, making depth pruning an effective approach for improving inference efficiency."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.27786) · [PDF](https://arxiv.org/pdf/2605.27786)

## 一句话摘要

Large language models are known to contain representational redundancy across network depth, making depth pruning an effective approach for improving inference efficiency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models are known to contain representational redundancy across network depth, making depth pruning an effective approach for improving inference efficiency. Existing one-shot pruning methods rely on local layer importance or fixed redundancy assumptions across architectures. We propose Locality-Aware Redundancy Pruning (LoRP), a training-free one-shot depth pruning framework guided by representation locality. We show that inter-layer redundancy can be either localized or globally distributed depending on the LLM architecture. To characterize this phenomenon, we introduce Representation Locality Score (RLS), derived from global inter-layer hidden-state similarity. Using a small calibration set, LoRP computes pairwise layer similarity, clusters layers by representational similarity, and allocates pruning according to residual intra-cluster redundancy. Experiments across diverse LLM families show improvements in both perplexity and downstream task accuracy. Official github repository: https://github.com/daniel-eai/LoRP-Locality-Aware-Redundancy-Pruning/

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Vincent-Daniel Yun, Youngrae Kim, Woosang Lim, YoungJin Heo, Minkyu Kim, Sunwoo Lee
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/daniel-eai/LoRP-Locality-Aware-Redundancy-Pruning/](https://github.com/daniel-eai/LoRP-Locality-Aware-Redundancy-Pruning/)
- 阅读深度：metadata
