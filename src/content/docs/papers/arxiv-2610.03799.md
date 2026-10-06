---
title: "StepCAD: Mesh-to-CAD Code Generation via LLM Policy and Geometry-Guided Search"
description: "Recovering executable CAD programs from 3D meshes is challenging due to the compositional nature of CAD construction and the interaction between discrete modeling choices and continuous parameters."
---

**评分：47/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2610.03799) · [PDF](https://arxiv.org/pdf/2610.03799)

## 一句话摘要

Recovering executable CAD programs from 3D meshes is challenging due to the compositional nature of CAD construction and the interaction between discrete modeling choices and continuous parameters.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recovering executable CAD programs from 3D meshes is challenging due to the compositional nature of CAD construction and the interaction between discrete modeling choices and continuous parameters. Many learning-based methods predict complete programs in a single pass and rely predominantly on sketch-extrude representations, limiting operation diversity and opportunities to correct geometric errors during reconstruction. We introduce StepCAD, a generative optimization approach that combines a state-conditioned CAD policy with geometry-guided search. Given an input mesh, the policy predicts construction actions conditioned on both target and intermediate geometry, and an IoU-guided tree search refines the resulting program through local edits. We also introduce ARCADE-1.5M, a large-scale dataset of 1.5M executable CAD programs spanning diverse operations, sequences with a maximum length of 150+ counted operations, and 12.5M intermediate state-action transitions. Experiments across multiple CAD reconstruction benchmarks show that StepCAD achieves state-of-the-art geometric reconstruction accuracy with consistently high validity, yielding up to 87.2% relative IoU improvement over the strongest evaluated baseline, with particularly large gains on complex shapes. Project page: https://ghadinehme.com/stepcad.github.io/

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 15 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ghadi Nehme, Faez Ahmed
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
