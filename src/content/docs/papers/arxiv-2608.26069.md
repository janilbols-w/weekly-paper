---
title: "Group-Shared Low-Rank Approximation for Mobile-Efficient Pointwise Convolutions in Large-Kernel CNNs"
description: "Large-kernel Convolutional Neural Networks (CNNs) deliver remarkable performance in vision tasks by significantly expanding receptive fields, yet their quadratic parameter growth critically impedes storage-efficient edge deployment."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.26069) · [PDF](https://arxiv.org/pdf/2608.26069)

## 一句话摘要

Large-kernel Convolutional Neural Networks (CNNs) deliver remarkable performance in vision tasks by significantly expanding receptive fields, yet their quadratic parameter growth critically impedes storage-efficient edge deployment.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large-kernel Convolutional Neural Networks (CNNs) deliver remarkable performance in vision tasks by significantly expanding receptive fields, yet their quadratic parameter growth critically impedes storage-efficient edge deployment. While existing efficient architectures adopt parameter-efficient depthwise separable convolution backbones that leverage techniques like low-rank approximation and weight sharing to compress depthwise convolutions, we identify a critical oversight: pointwise convolutions dominate parameter volume (>87% in models like RepLKNet-31B) and constitute the primary deployment bottleneck on resource-constrained edge devices. This results in prohibitive storage costs and severe memory-loading constraints on resource-limited devices (e.g., smartphones with 4-12 GB Random Access Memory (RAM)). To overcome this, we propose Channel Group-Shared (CGS) low-rank approximation, a novel Singular Value Decomposition (SVD)-based parameter-sharing strategy. CGS constructs a structured low-rank paradigm isomorphic to SVD decomposition, comprising shared (high-parameter-cost) down/up-projection matrices across channel groups within a layer and channel-group-specific (low-parameter-cost) scalable diagonal matrices. This group-sharing design achieves significant parameter reduction. Extensive experiments demonstrate that large-kernel CNNs (RepLKNet, ConvNeXt, SLaK) enhanced with CGS strike an empirically favorable balance between competitive performance and substantially reduced storage costs. Crucially, by alleviating storage constraints, reducing memory bandwidth pressure during loading, and minimizing model loading latency, CGS enables the feasible deployment of pre-trained large-kernel CNN models on edge devices, thereby bridging the gap between high-performance vision models and practical edge deployment.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: weight sharing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hao Luo, Yiting Yang, Wenyi Zhao, Man Jiang, Zhijun Lin, Ghulam Mohiuddin, Ting Jiang, Kunming Luo, Zihao Zhang, Qingsen Yan, Guoqing Wang, Wei Dong, Peng Wang
- 发布：2026-08-27；更新：2026-08-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
