---
title: "SparseForge: Beyond Spike Sparsity toward Hardware-Exploitable Neuron Pruning for Efficient SNN Acceleration"
description: "Spiking Neural Networks (SNNs) provide an event-driven paradigm for energy-efficient edge computing."
---

**评分：57/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.01611) · [PDF](https://arxiv.org/pdf/2611.01611)

## 一句话摘要

Spiking Neural Networks (SNNs) provide an event-driven paradigm for energy-efficient edge computing.

## 为什么值得关注

待编辑增强。

## 摘要原文

Spiking Neural Networks (SNNs) provide an event-driven paradigm for energy-efficient edge computing. However, operation-level sparsity in SNNs does not necessarily eliminate the hardware costs associated with redundant output neurons, including neuron-state maintenance, partial-sum (psum) accesses, and on-chip storage requirements. This paper presents SparseForge, a hardware-aware sparse SNN acceleration framework that jointly optimizes neuron pruning, sparse dataflow, and accelerator microarchitecture. At the algorithm level, we introduce a gated leaky integrate-and-fire (G-LIF) neuron to learn differentiable neuron masks with binary spike semantics. A dual regularization scheme is further developed to align pruning with both synaptic-operation reduction and psum buffer capacity reduction. At the dataflow level, we design a sparse Column-Wise Product (CWP) dataflow with a variant of incremental spike encoding to improve weight-access regularity and reduce sparse-index overhead under dynamic spike activity. At the architecture level, we develop a mask-aware sparse processing unit (SPU) that supports compressed spike decoding, sparse implicit im2col conversion, neuron-mask-gated psum updates, and decoupled sparse execution. Experimental results across multiple SNN backbones and datasets show that SparseForge retains 1.75%--77.99% of neurons and 0.16%--62.36% of synaptic operations, with a configurable accuracy--efficiency trade-off. The buffer-capacity-aware regularization reduces the required psum buffer capacity by up to 96.18\%. FPGA implementations on a Xilinx ZCU9EG achieve 296.94--619.49 GOPS/W across the evaluated workloads. Across matched network and dataset settings, SparseForge provides 1.24--4.17 higher FPS and 1.50--7.18 higher GOPS/W than representative FPGA-based SNN accelerators, while reducing EDP by 1.70--19.13, with benchmark-dependent accuracy--efficiency trade-offs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 6 |
| rigor | 15 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kainan Wang, Sanhe Fu, Aili Wang
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
