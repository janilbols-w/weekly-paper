---
title: "X-AVDD: Cross-Attentive Audio-Visual Dataset Distillation"
description: "Audio-visual dataset distillation aims to synthesize a small dataset from a large paired audio-visual dataset, while nearly preserving the training utility for neural networks."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.13687) · [PDF](https://arxiv.org/pdf/2610.13687)

## 一句话摘要

Audio-visual dataset distillation aims to synthesize a small dataset from a large paired audio-visual dataset, while nearly preserving the training utility for neural networks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Audio-visual dataset distillation aims to synthesize a small dataset from a large paired audio-visual dataset, while nearly preserving the training utility for neural networks. Existing approaches such as DM and AVDD face two critical limitations: 1) they are memory-intensive, making them difficult to scale to complex architectures and higher samples-per-class (SPC) settings, and 2) they often fail to preserve strong cross-modal semantic correspondence. To tackle these issues, we propose X-AVDD, a cross-attention-based distillation method that explicitly captures inter-modal relationships during synthesis. By decoupling cross-modal alignment from joint optimization, X-AVDD is substantially more memory-efficient, reducing end-to-end synthesis cost by $\sim 8\times$ GPU-hours, while producing highly aligned synthetic data. Empirically, X-AVDD significantly outperforms other audio-visual distillation methods. On VGGSound, an audio-visual dataset of short YouTube clips, X-AVDD improves top-1 test accuracy from $8.2\%\rightarrow24.0\%$ at SPC=$10$ and $9.8\%\rightarrow26.5\%$ at SPC=$20$. Furthermore, X-AVDD improves cross-architecture generalization (e.g., $25.5\%\rightarrow35.3\%$ for a ViT target on AVE dataset at SPC $=50$) and successfully scales to complex architectures such as AudioCLIP, achieving $62.3\%$ accuracy using only $5.65\%$ of the full dataset, against the full dataset accuracy of $72.4\%$ while completing in $9\times$ lower training time compared to the full dataset.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Saumyaranjan Mohanty, Aravind Reddy, Konda Reddy Mopuri
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
