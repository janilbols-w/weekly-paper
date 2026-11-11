---
title: "Distilling Graph Geometry: Knowledge Gap from GNNs to MLPs"
description: "GNN-to-MLP distillation aims to retain the predictive accuracy of a message-passing teacher while deploying a graph-free MLP at inference."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.10520) · [PDF](https://arxiv.org/pdf/2610.10520)

## 一句话摘要

GNN-to-MLP distillation aims to retain the predictive accuracy of a message-passing teacher while deploying a graph-free MLP at inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

GNN-to-MLP distillation aims to retain the predictive accuracy of a message-passing teacher while deploying a graph-free MLP at inference. Existing methods mainly transfer node-wise predictions or use confidence-based reweighting, but they do not specify where the student should preserve the teacher's graph-induced geometry. We show that this omission leads to two spectral failure modes in the student's representation space. On sparse graphs, the student suffers from spectral underfit, missing high-energy teacher directions induced by aggregation. On dense graphs, it suffers from spectral overfit, retaining spurious directions that the teacher has collapsed through aggregation. Motivated by an energy-weighted teacher-student alignment objective, we propose Graph Geometry-aware MLP (G^2MLP), a training-time distillation framework guided by Ollivier-Ricci curvature. Curvature acts as a local proxy for allocating supervision between prediction-level and representation-level alignment. The deployed model is a standard MLP with no graph access at inference. Across node-classification benchmarks, G^2MLP improves over graph-free distillation baselines in most settings, reduces the teacher-student rank gap in both regimes, and transfers to Graph Transformer teachers and link prediction.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhewei Chen, Hao Zhu, Jiaojiao Jiang, Ahad N. Zehmakan
- 发布：2026-10-08；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
