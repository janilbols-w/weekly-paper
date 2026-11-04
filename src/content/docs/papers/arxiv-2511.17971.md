---
title: "Beyond MACs: Deployment-Constrained Design Space Exploration for Tensorized Neural Networks"
description: "Tensor-train (TT) compression reduces neural-network parameters, but the latency of a tensorized layer is set by its contraction order and its mapping onto hardware: a contraction path with fewer multiply-accumulate operations (MACs) is not necessarily faster on a systolic array."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2511.17971) · [PDF](https://arxiv.org/pdf/2511.17971)

## 一句话摘要

Tensor-train (TT) compression reduces neural-network parameters, but the latency of a tensorized layer is set by its contraction order and its mapping onto hardware: a contraction path with fewer multiply-accumulate operations (MACs) is not necessarily faster on a systolic array.

## 为什么值得关注

待编辑增强。

## 摘要原文

Tensor-train (TT) compression reduces neural-network parameters, but the latency of a tensorized layer is set by its contraction order and its mapping onto hardware: a contraction path with fewer multiply-accumulate operations (MACs) is not necessarily faster on a systolic array. We present a deployment-constrained, latency-guided design space exploration (DSE) framework for fixed-rank tensorized neural networks (TNNs) under a fixed processing-element (PE) budget. Using MAC-guided path pruning, it evaluates feasible combinations of contraction paths, three PE-array partitions, and input-, output-, and weight-stationary dataflows. By minimizing the sum of inference and training latency estimates, it selects a single physical PE partition shared across layers and both modes, while allowing layer- and mode-specific paths and dataflows. On ResNet-18 and ViT-Ti/4, 25%-50% of the layers select a path other than the minimum-MAC one, the best dataflow varies across layers and models, and on a representative ViT layer the latency-selected candidate reduces simulated latency by 23.5% relative to the minimum-MAC candidate. Deployed on a Xilinx VU9P FPGA accelerator that supports both inference and training, the complete TT+INT8 system achieves 3.28x-4.00x inference and 3.42x-3.85x training speedups over dense implementations with the same PE budget.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jinsong Zhang, Minghe Li, Jiayi Tian, Jinming Lu, Zheng Zhang
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
