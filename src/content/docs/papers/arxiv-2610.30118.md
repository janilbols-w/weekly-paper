---
title: "The role of locality and weight sharing in convolutional neural networks"
description: "The success of convolutional neural networks is often attributed to locality and weight sharing."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.30118) · [PDF](https://arxiv.org/pdf/2610.30118)

## 一句话摘要

The success of convolutional neural networks is often attributed to locality and weight sharing.

## 为什么值得关注

待编辑增强。

## 摘要原文

The success of convolutional neural networks is often attributed to locality and weight sharing. However, how these two properties separately shape learning, and how their effects depend on the spatial correlations of natural images, remain poorly understood. We address these questions in a teacher-student model with a convolutional teacher acting on $P$ input positions with correlation $c$ between positions. We compare convolutional and locally connected students trained by online stochastic gradient descent, and derive ordinary differential equations that describe their dynamics exactly in the limit of large feature dimension $D$. For uncorrelated positions ($c = 0$), the two students follow the same learning trajectory, with the convolutional student learning exactly $P$ times faster. We also find that locality affects the sample complexity: a student that matches the kernel size of the teacher recovers it from $\mathcal{O}_{D}(D)$ samples, whereas $\mathcal{O}_{D}(D\log(D))$ samples are needed with a larger kernel. For $c > 0$, spatial correlations can reduce the advantage of weight sharing. The asymptotic error of the convolutional student grows with $c$, whereas that of the locally connected student is independent of $c$ and overall lower when evaluated at the same learning rate. When the learning rate is instead tuned to the training horizon, however, the locally connected student wins at early times and the convolutional student at late times, with a transition that we predict analytically.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: weight sharing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Francesco Mori, Melanie Weber
- 发布：2026-10-22；更新：2026-10-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
