---
title: "Channel-Adaptive Edge AI: Maximizing Inference Throughput by Adapting Computational Complexity to Channel States"
description: "\\emph{Integrated communication and computation} (IC$^2$) has emerged as a new paradigm for enabling efficient edge inference in sixth-generation (6G) networks."
---

**评分：38/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2603.03146) · [PDF](https://arxiv.org/pdf/2603.03146)

## 一句话摘要

\emph{Integrated communication and computation} (IC$^2$) has emerged as a new paradigm for enabling efficient edge inference in sixth-generation (6G) networks.

## 为什么值得关注

待编辑增强。

## 摘要原文

\emph{Integrated communication and computation} (IC$^2$) has emerged as a new paradigm for enabling efficient edge inference in sixth-generation (6G) networks. However, the design of IC$^2$ technologies is hindered by the lack of a tractable theoretical framework for characterizing \emph{end-to-end} (E2E) inference performance. The metric is highly complicated as it needs to account for both channel distortion and artificial intelligence (AI) model architecture and computational complexity. In this work, we address this challenge by developing a tractable analytical model for E2E inference accuracy and leveraging it to design a \emph{channel-adaptive AI} algorithm that maximizes inference throughput, referred to as the edge processing rate (EPR), under latency and accuracy constraints. Specifically, we consider an edge inference system in which a server deploys a backbone model with early exit, which enables flexible computational complexity, to perform inference on data features transmitted by a mobile device. The proposed accuracy model characterizes high-dimensional feature distributions in the angular domain using a Mixture of von Mises (MvM) distribution. This leads to a desired closed-form expression for inference accuracy as a function of quantization bit-width and model traversal depth, which represents channel distortion and computational complexity, respectively. Building upon this accuracy model, we formulate and solve the EPR maximization problem under joint latency and accuracy constraints, leading to a channel-adaptive AI algorithm that achieves full IC$^2$ integration. The proposed algorithm jointly adapts transmit-side feature compression and receive-side model complexity according to channel conditions to maximize overall efficiency and inference throughput. Experimental results demonstrate its superior performance as compared with fixed-complexity counterparts.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: edge inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jierui Zhang, Jianhao Huang, Kaibin Huang
- 发布：2026-09-02；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
