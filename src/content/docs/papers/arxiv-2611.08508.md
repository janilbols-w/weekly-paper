---
title: "MeshRT: Compile-Time Governed Wafer-Scale Runtime for Low-Latency High-Throughput Inference"
description: "Wafer-scale accelerators promise ultra-low-latency AI inference, but current system stacks still carry an unsustainably high cost premium."
---

**评分：40/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2611.08508) · [PDF](https://arxiv.org/pdf/2611.08508)

## 一句话摘要

Wafer-scale accelerators promise ultra-low-latency AI inference, but current system stacks still carry an unsustainably high cost premium.

## 为什么值得关注

待编辑增强。

## 摘要原文

Wafer-scale accelerators promise ultra-low-latency AI inference, but current system stacks still carry an unsustainably high cost premium. The reason is that many current and emerging inference techniques, such as batching and MoE, introduce runtime dynamism that existing wafer-scale systems cannot support efficiently. As a result, they must choose between two unsatisfactory options: accept suboptimal latency, or preserve low latency by restricting dynamic techniques, thereby limiting the models they can support and reducing aggregate throughput. This tradeoff significantly increases the cost of low-latency serving. We present MeshRT, the first wafer-scale system to achieve both ultra-low latency and high throughput for LLM inference. MeshRT achieves this via a novel system architecture, which we call compile-time governance of runtime dynamism. This architecture features new system abstractions and mechanisms that enable MeshRT to compile dynamic events arising from LLM inference directly into per-core schedules, enabling asynchronous and decentralized execution with low runtime overhead. Implemented on a commodity wafer-scale accelerator, MeshRT preserves ultra-low latency while improving throughput by up to 56$\times$ over the state-of-the-art system for wafer-scale accelerators. Against measured single-instance SGLang results on H200, MeshRT achieves 4.5-7.0$\times$ lower latency. Under ideal linear scaling of those GPU measurements to an approximately power-matched H200 cluster, MeshRT achieves 1.7-13.0$\times$ higher decode system throughput in the low-latency regime.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Congjie He, Le Xu, Zhan Lu, Yeqi Huang, Haocheng Xiao, Cheng Deng, Lingxiao Ma, Ziming Miao, Fan Yang, Luo Mai
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
