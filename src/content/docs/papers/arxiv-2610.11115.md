---
title: "Dynamics as Code: On Model Compression via Dynamic System"
description: "The escalating size of pretrained neural networks has rendered model compression a prerequisite for deployment under stringent memory and compute constraints."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.11115) · [PDF](https://arxiv.org/pdf/2610.11115)

## 一句话摘要

The escalating size of pretrained neural networks has rendered model compression a prerequisite for deployment under stringent memory and compute constraints.

## 为什么值得关注

待编辑增强。

## 摘要原文

The escalating size of pretrained neural networks has rendered model compression a prerequisite for deployment under stringent memory and compute constraints. With the irrational winding as an example, earlier work introduced a dynamic system (DS) paradigm that reconceptualizes compression as compact weight representation: high-dimensional parameters are encoded by the index of a trajectory produced by a dynamic system, from which the vector is recovered during decompression. This mechanism is fundamentally distinct from pruning, quantization, knowledge distillation, and low-rank decomposition. Along this direction, we prove that under a Diophantine condition, a finite trajectory of \(M = O(\epsilon^{-(d+\nu)})\) states in the irrational winding constitutes an \(\epsilon\)-net over the \(d\)-dimensional weight space, thereby linking state resolution, decompression error, and compression ratio in a predictable manner. Furthermore, we propose a generalized DS-based model compression framework by unifying four DS families---space-filling curves (Hilbert, Peano, Morton/Z-order, Snake), chaotic systems (Lorenz), congruential and pseudo-random generators (LCG, PCG), and low-discrepancy sequences (Halton). Also, we introduce the KD-tree and coordinate-template acceleration to scale to large models as well as outlier identification to control the error. Experiments on ResNet-18 and Qwen2.5-1.5B/Qwen1.5-7B validate that DS-based compression achieves competitive compression ratios without post-hoc retraining, with controllable decompression error and flexible state-space design, establishing it as a principled and practical compression approach.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation, pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Fan Gao, Wei Su, Juntong Fan, Renfeng Peng, Hongyu Liu, Jinqiao Duan, Feng-Lei Fan
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
