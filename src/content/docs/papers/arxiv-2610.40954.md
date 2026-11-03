---
title: "CAMEL: Cross-Architecture Masked Embedding Learning for Ultra-Lightweight Retinal Foundation Models"
description: "Recent progress in deep learning has substantially advanced automated grading of ophthalmologic pathologies, supported by large annotated datasets and improved representation learning."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.40954) · [PDF](https://arxiv.org/pdf/2610.40954)

## 一句话摘要

Recent progress in deep learning has substantially advanced automated grading of ophthalmologic pathologies, supported by large annotated datasets and improved representation learning.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent progress in deep learning has substantially advanced automated grading of ophthalmologic pathologies, supported by large annotated datasets and improved representation learning. However, a significant gap remains between state-of-the-art performance and clinical scalability. In particular, foundation models have reshaped image-based medical screening and diagnosis. These large-scale architectures trained on extensive datasets learn rich, generalizable feature representations that can be adapted to a wide range of downstream tasks. In ophthalmology, RETFound, one of the most relevant foundation models for retinal images, performs strongly across classification, segmentation, and risk prediction tasks. Despite their effectiveness, foundation models are often computationally prohibitive, hindering their deployment in real-world clinical environments where hardware constraints and latency are critical. To bridge this gap, we introduce CAMEL (Cross-Architecture Masked Embedding Learning), a novel cross-architecture distillation framework that uses an asymmetric masking strategy during embedding learning to effectively transfer knowledge from massive teacher foundation models to compact, lightweight student models. Our experimental evaluation across four datasets shows that CAMEL preserves accuracy while drastically reducing computational complexity, enabling lightweight yet highly accurate models suitable for resource-limited clinical settings.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Andre Guarnier De Mitri, Giovani Decico Lucafo, Miller Matheus Lima Anacleto Rocha, Diego Furtado Silva
- 发布：2026-11-02；更新：2026-11-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
