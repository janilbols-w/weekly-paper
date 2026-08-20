---
title: "GQ-FSL: Green Quantized Federated Split Learning Framework for Wireless Edge Networks"
description: "Deploying state-of-the-art deep neural networks (DNNs) at the wireless edge is severely bottlenecked by the strict energy and resource constraints of mobile devices."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2607.29659) · [PDF](https://arxiv.org/pdf/2607.29659)

## 一句话摘要

Deploying state-of-the-art deep neural networks (DNNs) at the wireless edge is severely bottlenecked by the strict energy and resource constraints of mobile devices.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deploying state-of-the-art deep neural networks (DNNs) at the wireless edge is severely bottlenecked by the strict energy and resource constraints of mobile devices. Although federated split learning (FSL) alleviates on-device computational burdens by offloading workloads to an edge server, this may introduce systemic overheads, while the continuous exchange of intermediate activations, gradients, and submodels still incurs significant energy consumption (EC). To address this, we propose a green quantized FSL (GQ-FSL) framework that incorporates stochastic quantization for both local collaborative training and wireless transmissions. Notably, GQ-FSL supports asymmetric precision levels for the client- and server-side submodels, effectively decoupling device energy constraints from global convergence degradation. To quantify these tradeoffs, we develop parameterized energy models for the split architecture and derive a theoretical convergence bound under statistically heterogeneous data. Building on that, we formulate a joint optimization problem to configure the DNN split point and precision levels, minimizing the total system EC while satisfying strict latency and target accuracy constraints. Ultimately, we demonstrate that GQ-FSL enables large-scale DNN deployment on resource-constrained devices, achieving superior energy efficiency compared to quantized federated learning and full-precision FSL.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Idan Roth, Lutz Lampe
- 发布：2026-08-20；更新：2026-08-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
