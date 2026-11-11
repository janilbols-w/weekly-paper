---
title: "ConvLUT: Rethinking Convolutional Architectures for Ultra-Low-Latency LUT-Based Inference"
description: "Lookup-table (LUT)-based neural networks (NNs) offer a compelling path to ultra-low-latency inference on FPGAs."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.11507) · [PDF](https://arxiv.org/pdf/2611.11507)

## 一句话摘要

Lookup-table (LUT)-based neural networks (NNs) offer a compelling path to ultra-low-latency inference on FPGAs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Lookup-table (LUT)-based neural networks (NNs) offer a compelling path to ultra-low-latency inference on FPGAs. However, existing LUT-based neural networks have largely been restricted to MLP-style topologies, leaving structured vision and audio tasks underexplored. We present ConvLUT, a family of fully unrolled LUT-mappable convolutional architectures targeting the MLPerf Tiny benchmarks. It is comprised of a standard convolutional model built around a hierarchical tree of LUTs and a depthwise separable model following the MobileNet design philosophy. These architectures are enabled by four key contributions: a unified LUT-based convolutional framework supporting standard, depthwise, and pointwise convolutions under explicit fan-in constraints; a LUT-tree that addresses the $k^2c$ receptive field dimensionality bottleneck; a channel-partitioned LUT pooling layer that replaces conventional spatial pooling; and a hardware-aware iterative pruning strategy for stable convergence at scale. Evaluated on CIFAR-10, Visual Wake Words, and Keyword Spotting, ConvLUT achieves competitive accuracy with fully unrolled inference latencies below $\sim 50$ ns. On CIFAR-10 it reaches at least a $8844\times$ latency reduction over non-logic-based prior implementations, and outperforms existing MLP-style LUT-based models on the same task by at least $20$ pp in test accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Marta Andronic, Olivia Weng, Danial Zuberi, Ryan Kastner, George A. Constantinides
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
