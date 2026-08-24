---
title: "DeepStack: Facilitating Co-Design Exploration of 3D DRAM-Stacked Accelerators for Distributed LLM Inference"
description: "Advances in hybrid bonding and packaging have driven growing interest in 3D DRAM-stacked AI accelerators."
---

**评分：51/100** · LLM 高效推理 > Serving 与分布式推理 > 并行与通信

[论文原文](https://arxiv.org/abs/2604.04750) · [PDF](https://arxiv.org/pdf/2604.04750)

## 一句话摘要

Advances in hybrid bonding and packaging have driven growing interest in 3D DRAM-stacked AI accelerators.

## 为什么值得关注

待编辑增强。

## 摘要原文

Advances in hybrid bonding and packaging have driven growing interest in 3D DRAM-stacked AI accelerators. As large language models (LLMs) scale to hundreds of billions or trillions of parameters, distributed inference across multiple 3D chips has become essential for AI serving. This trend makes cross-stack co-design critical because system-level parallelization and scheduling choices are tightly coupled with hardware characteristics such as memory organization, interconnects, and thermal constraints. We present DeepStack, an accurate performance model and efficient design space exploration (DSE) framework for distributed 3D-stacked LLM inference. At the hardware level, DeepStack captures transaction-aware memory bandwidth, bank activation constraints, buffering limitations, and thermal and power behavior. At the system level, it incorporates comprehensive parallelization strategies and execution scheduling. Through a dual-stage network abstraction and tile-level compute-communication overlap modeling, DeepStack achieves up to 100,000x faster evaluation than state-of-the-art simulators at comparable accuracy. We cross-validate DeepStack against our in-house 3D designs, an NS-3 backend with 2.12% error, and vLLM serving on eight B200 GPUs with 12.92% error. Combined with hierarchical search, DeepStack efficiently explores about 2.5 x 10^14 design points spanning the number of stacked DRAM layers, DRAM vertical connectivity, interconnects, compute-memory allocation, and distributed scheduling under thermal and area constraints. A search-space ablation shows that restricted DSE baselines can miss up to 9.5x modeled throughput. Beyond modeling and DSE, DeepStack derives design implications for distributed 3D AI systems and guides performance optimization across the stack. Source code and artifacts are available at https://github.com/tile-ai/DeepStack/tree/ae.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 12 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distributed inference
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Zhiwen Mo, Guoyu Li, Hao Mark Chen, Yu Cheng, Zhengju Tang, Qianzhou Wang, Lei Wang, Shuang Liang, Lingxiao Ma, Xianqi Zhou, Yuxiao Guo, Wayne Luk, Jilong Xue, Hongxiang Fan
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/tile-ai/DeepStack/tree/ae](https://github.com/tile-ai/DeepStack/tree/ae)
- 阅读深度：metadata
