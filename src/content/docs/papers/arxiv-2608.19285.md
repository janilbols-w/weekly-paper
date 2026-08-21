---
title: "Clustering and Token Denoising for Faster and More Robust VLMs"
description: "Recent Visual-Language Models (VLMs) have enhanced the capabilities of pre-trained LLMs by adding vision tokens alongside text, with approaches like LLaVA showing impressive results."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.19285) · [PDF](https://arxiv.org/pdf/2608.19285)

## 一句话摘要

Recent Visual-Language Models (VLMs) have enhanced the capabilities of pre-trained LLMs by adding vision tokens alongside text, with approaches like LLaVA showing impressive results.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent Visual-Language Models (VLMs) have enhanced the capabilities of pre-trained LLMs by adding vision tokens alongside text, with approaches like LLaVA showing impressive results. However, the computational burden of processing up to 576 or 729 visual tokens makes edge deployment challenging. While various token pruning techniques require retraining, some are training-free and thus can easily adapt to architecture changes. We introduce ClustRS, a two-part, training-free algorithm for robust token pruning. Its first component is an attention-weighted, clustering algorithm that selects representative tokens from each semantic cluster. The second component, Residual Shrinkage, is a one-pass denoising step on the selected tokens. These training-free lightweight steps make LLaVA ready for real-world data, improving robustness to a wide range of image-noise types and intensities. Experimental results on the ScienceQA-IMG and MM-VET benchmarks show our method outperforms attention- and diversity-based methods by up to 20\% under extreme noise and token conditions (reducing tokens by 97\%, down to 16 tokens) on LLaVA 1.5 7b and achieves exceptional results on LLaVA-OneVision, where we match baseline performance with fewer than one-third of their tokens under mild noise conditions. Our study demonstrates a simple yet powerful alternative to both score-only and diversity-only pruning rules, paving the way for compute-efficient and noise-resilient VLM deployment.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Baptiste Rossigneux, Inna Kucher, Vincent Lorrain, Emmanuel Casseau
- 发布：2026-08-21；更新：2026-08-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
