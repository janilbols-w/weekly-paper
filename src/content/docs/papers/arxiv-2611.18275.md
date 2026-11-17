---
title: "BPU-SpikeMM:Exact Matrix Multiplication via Spatio-Temporal Spike Encoding on Real Neuromorphic Hardware"
description: "Matrix multiplication is the dominant computational kernel in deep learning, yet its growing scale strains conventional von Neumann hardware in energy efficiency and bandwidth."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2611.18275) · [PDF](https://arxiv.org/pdf/2611.18275)

## 一句话摘要

Matrix multiplication is the dominant computational kernel in deep learning, yet its growing scale strains conventional von Neumann hardware in energy efficiency and bandwidth.

## 为什么值得关注

待编辑增强。

## 摘要原文

Matrix multiplication is the dominant computational kernel in deep learning, yet its growing scale strains conventional von Neumann hardware in energy efficiency and bandwidth. Neuromorphic architectures offer a promising alternative, but mathematical equivalence between matrix multiplication and spiking computation does not guarantee direct execution on real neuromorphic hardware, as the specific hardware paradigm may still require additional data recovery, bit-weight reconstruction, or state readout after neuromorphic execution. This paper presents BPU-SpikeMM (Brain Processing Unit-based Spike Matrix Multiplication), an exact spatio-temporal spike encoding framework for matrix multiplication on real neuromorphic hardware. We prove the exact equivalence of spike-encoded matrix multiplication under the BPU execution paradigm, distinguish mathematical equivalence from native direct-readout equivalence on BPU hardware, and build a spatio-temporal offloading pipeline supporting multiple encoding schemes. Furthermore, we extend the framework to a multi-dimensional encoding design space and evaluate the applicability of different encodings on real BPU hardware in terms of correctness, temporal resource cost, spatial resource cost, and event-driven metrics. The results confirm native direct-readout equivalence across all evaluated encoding schemes and show that their applicability to BPU execution depends on joint trade-offs among temporal cost, spatial resource consumption, and event activity.

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

- taxonomy keywords: offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Rongyuan Guo, Yufeng Zhang, Haotian Wang, Canming Yao, Yuxiang Huan, Wangdong Yang, Kenli Li
- 发布：2026-11-16；更新：2026-11-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
