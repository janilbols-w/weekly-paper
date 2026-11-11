---
title: "TSFFormer: A Frequency-Domain Spike Transformer for Green Human Activity Recognition"
description: "Wearable Inertial Measurement Units (IMUs) enable pervasive Human Activity Recognition (HAR), but traditional Deep Neural Networks (DNNs) suffer from an \"arithmetic-latency deadlock\" due to dense floating-point MAC operations."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2611.12090) · [PDF](https://arxiv.org/pdf/2611.12090)

## 一句话摘要

Wearable Inertial Measurement Units (IMUs) enable pervasive Human Activity Recognition (HAR), but traditional Deep Neural Networks (DNNs) suffer from an "arithmetic-latency deadlock" due to dense floating-point MAC operations.

## 为什么值得关注

待编辑增强。

## 摘要原文

Wearable Inertial Measurement Units (IMUs) enable pervasive Human Activity Recognition (HAR), but traditional Deep Neural Networks (DNNs) suffer from an "arithmetic-latency deadlock" due to dense floating-point MAC operations. While Spiking Neural Networks (SNNs) offer ultra-low power, existing ones face spatial blind spots, rigid neurons, and gradient degradation. To address these, we propose TSFFormer, a purely spiking Fourier Transformer for Green HAR. It introduces two key innovations: (1) a MultiHeadFourier attention that performs frequency-domain global mixing, reducing complexity from \(O(V^2)\) to \(O(V\log V)\), eliminating spatial blind spots, and saving \(\sim\)50% GPU memory; and (2) a dual-compartment Temporal Spiking LIF (TSLIFNode) that utilizes dynamic thresholds to adapt to non-stationary rhythms and mitigate gradient degradation. Extensive experiments on 8 public IMU benchmarks demonstrate that TSFFormer surpasses state-of-the-art SNNs and even the classic DeepConvLSTM, achieving a \(\sim\)3\(\times\) faster training speed with an energy footprint of 0.1 pJ. Ablation studies confirm the synergistic effect of our modules, providing a highly accurate, ultra-low-power event-driven paradigm for wearable sensing.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiale Deng, Shuiying Xiang
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
