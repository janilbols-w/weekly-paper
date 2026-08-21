---
title: "APEX: A Dual-Sparsity Accelerator for Precise and Efficient SNN Inference"
description: "Spiking Neural Networks (SNNs) have emerged as an energy-efficient alternative to Artificial Neural Networks (ANNs), leveraging sparse accumulate operations in the place of power-hungry multiply-and-accumulate operations."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.19046) · [PDF](https://arxiv.org/pdf/2608.19046)

## 一句话摘要

Spiking Neural Networks (SNNs) have emerged as an energy-efficient alternative to Artificial Neural Networks (ANNs), leveraging sparse accumulate operations in the place of power-hungry multiply-and-accumulate operations.

## 为什么值得关注

待编辑增强。

## 摘要原文

Spiking Neural Networks (SNNs) have emerged as an energy-efficient alternative to Artificial Neural Networks (ANNs), leveraging sparse accumulate operations in the place of power-hungry multiply-and-accumulate operations. ANN-SNN conversion is a widely adopted approach to realize deep SNNs with accuracy comparable to that of ANNs. The Quantization-Clip-Floor-Shift (QCFS) activation minimizes conversion error, yet requires a large number of inference timesteps to match the source ANN accuracy on real-world vision datasets. PASCAL addresses this by proposing the Precise ANN-SNN Conversion Integrate-and-Fire (PASC-IF) neuron, which guarantees mathematical equivalence between the converted SNN and the source ANN, thereby achieving ANN-equivalent accuracy at significantly reduced timesteps. Despite this algorithmic advancement, the hardware implications of deploying the PASC-IF neuron remain unexplored. In this work, we present APEX, a dual-sparsity SNN inference accelerator that integrates the PASC-IF neuron into the LoAS hardware framework. The three-stage PASC-IF datapath is realized as a fully combinational circuit with no additional latency cost. APEX exploits dual sparsity in both input spikes and weights through a fully temporal-parallel dataflow, enabling efficient sparse computation and reduced memory traffic. Across all evaluated models, the PASC-IF neuron on average achieves up to 3% higher accuracy than the standard IF neuron, with a power overhead of only 1.3%-5.4%, an area overhead of 2.1%-2.7%, and 40% energy reduction for best accuracy configurations.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Devgokul Bawa Venkatesh, Sreeram Radhakrishnan, Rajshekhar Rakshit, Gopalakrishnan Srinivasan
- 发布：2026-08-19；更新：2026-08-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
