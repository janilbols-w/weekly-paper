---
title: "FINN-Tro: Exploiting Verification Gaps in Dataflow Inference Accelerators"
description: "The growing adoption of dataflow accelerators for neural network inference introduces new attack surfaces that existing verification methodologies fail to address."
---

**评分：38/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.26824) · [PDF](https://arxiv.org/pdf/2609.26824)

## 一句话摘要

The growing adoption of dataflow accelerators for neural network inference introduces new attack surfaces that existing verification methodologies fail to address.

## 为什么值得关注

待编辑增强。

## 摘要原文

The growing adoption of dataflow accelerators for neural network inference introduces new attack surfaces that existing verification methodologies fail to address. Inference ac- celeration frameworks such as FINN, which transform quantized neural networks into FPGA-deployable dataflow architectures, implicitly assume semantic equivalence between the software model and the synthesized hardware. In this work, we in- troduce the FINN-Tro attack, which identifies and exploits a critical verification gap in the FINN compilation pipeline that enables stealthy hardware Trojan insertion without modifying the original quantized model. The Trojan is placed in the last Matrix-Vector Activation Unit (MVAU) layer and supports two counter-based trigger modes, periodic and persistent, and three payload types: bias addition, logit swapping, and bias subtraction, resulting in six different configurations. FINN-Tro is evaluated on an MNIST feed-forward network and a CIFAR-10 convolutional neural network deployed on a PYNQ-Z1 board. Across the evaluated configurations, accuracy reductions range from 0.90% to 82.84%, while throughput and runtime remain close to the corresponding baseline designs. The most severe configuration, persistent Bias Addition, reduces accuracy from 92.96% to 10.12% on MNIST and from 84.19% to 10.00% on CIFAR-10. The inserted logic introduces modest implementation overhead, with maximum LUT and FF increases of 6.71% and 7.49% for MNIST, and 2.50% and 3.98% for CIFAR-10, respectively. Our findings reveal that widely used pre- and post- compilation verification flows are insufficient for detecting such temporally delayed hardware manipulations, motivating the need for stronger verification mechanisms in accelerator toolchains.

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

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qazi Arbab Ahmed, Suraj Karki, Thorsten Jungeblut
- 发布：2026-09-20；更新：2026-09-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
