---
title: "SAF3R: Dynamic Sparse Attention for Feed-Forward 3D Reconstruction Transformers"
description: "Feed-forward 3D reconstruction (F3R) transformers have recently achieved remarkable success."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.03612) · [PDF](https://arxiv.org/pdf/2607.03612)

## 一句话摘要

Feed-forward 3D reconstruction (F3R) transformers have recently achieved remarkable success.

## 为什么值得关注

待编辑增强。

## 摘要原文

Feed-forward 3D reconstruction (F3R) transformers have recently achieved remarkable success. However, scaling them to long image sequences remains challenging, as the quadratic complexity of cross-view global attention quickly becomes the dominant computational bottleneck. While recent efforts attempt to improve efficiency through compressed or sparse attention, they fail to fully exploit the inherent sparsity and dynamic behavior of global attention. In this work, we present a comprehensive analysis of global attention across multiple F3R transformers and reveal that attention patterns are highly heterogeneous, dynamic, and extremely sparse across layers and attention heads. Motivated by these findings, we propose SAF3R, a training-free dynamic sparse attention framework tailored to F3R transformers. SAF3R integrates tailored sparse attention mechanisms with offline head profiling and an efficient online adaptation strategy to match input-dependent attention behaviors. Extensive experiments demonstrate that SAF3R achieves high sparsity ratios while preserving camera pose estimation and 3D reconstruction quality, translating into substantial end-to-end speedup on F3R transformers compared to existing methods. Code is available at https://github.com/jndeng/SAF3R

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Jianing Deng, Yuanzhe Li, Jialu Wang, Song Wang, Tianlong Chen, Huanrui Yang, Jingtong Hu
- 发布：2026-08-14；更新：2026-08-14
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/jndeng/SAF3R](https://github.com/jndeng/SAF3R)
- 阅读深度：metadata
