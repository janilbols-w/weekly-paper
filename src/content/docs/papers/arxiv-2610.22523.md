---
title: "Learning the Shared Latent Structure of Cryo-EM Inverse Problems"
description: "Understanding biomolecular function requires characterizing three-dimensional structure and conformational variability, for which cryogenic electron microscopy (cryo-EM) is a powerful tool."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.22523) · [PDF](https://arxiv.org/pdf/2610.22523)

## 一句话摘要

Understanding biomolecular function requires characterizing three-dimensional structure and conformational variability, for which cryogenic electron microscopy (cryo-EM) is a powerful tool.

## 为什么值得关注

待编辑增强。

## 摘要原文

Understanding biomolecular function requires characterizing three-dimensional structure and conformational variability, for which cryogenic electron microscopy (cryo-EM) is a powerful tool. Cryo-EM produces noisy two-dimensional particle images in which molecular structure, particle pose, and imaging conditions are jointly encoded. Recovering biological information from these observations spans inverse problems including pose estimation, heterogeneity analysis, and reconstruction. These tasks are usually addressed independently despite shared protein structure and image formation, motivating a common representation across inverse problems. Since biologically meaningful differences may be spatially localized, we study self-distillation with complementary global and masked patch objectives. Because experimental dataset discrimination can reflect acquisition-specific cues, we develop controlled synthetic and experimental evaluations and find that structural discrimination benefits from dense spatial features. We introduce the EMber family of vision transformers, pre-trained on >50 million experimental particle images from 214 EMPIAR datasets together with simulated projections from 268,000 molecular assemblies. EMber improves upon existing methods at conformational and compositional discrimination by 14.85 and 14.26 percentage points, estimates conformational populations to within 1.59pp error with a linear probe, and produces particle assignments yielding reference-quality reconstructions in fewer epochs. We demonstrate how to learn representations that capture biological information for use across multiple cryo-EM inverse problems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Nithin Chalapathi, Theo Sternlieb, Ethan Han, Sonya M. Hanson, Pilar Cossio, Aditi S. Krishnapriyan, Ritwik Gupta
- 发布：2026-10-19；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
