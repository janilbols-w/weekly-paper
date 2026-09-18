---
title: "NCCLZ: Compression-Enabled GPU Collectives with Decoupled Quantization and Entropy Coding"
description: "Collective communication is a major bottleneck for multi-node GPU workloads in scientific computing and distributed deep learning, especially when inter-node bandwidth is limited."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2605.12396) · [PDF](https://arxiv.org/pdf/2605.12396)

## 一句话摘要

Collective communication is a major bottleneck for multi-node GPU workloads in scientific computing and distributed deep learning, especially when inter-node bandwidth is limited.

## 为什么值得关注

待编辑增强。

## 摘要原文

Collective communication is a major bottleneck for multi-node GPU workloads in scientific computing and distributed deep learning, especially when inter-node bandwidth is limited. Although NCCL provides optimized GPU-centric collectives, large messages can still dominate end-to-end performance. Existing compression-enabled collective libraries either rely on MPI-based stacks that cannot fully exploit NCCL, omit entropy coding, or tightly couple full compressors with communication primitives, limiting compression ratio, flexibility, and communication-computation overlap. This paper presents NCCLZ, a compression-enabled GPU collectives that decouples quantization and entropy coding and integrates them at different layers of the stack. NCCLZ places quantization at the interface, embeds entropy coding into NCCL primitives, uses a lightweight device-side selector to choose coding strategies, and overlaps compression with communication to reduce exposed overhead. Experiments on scientific datasets, training gradients, and synthetic workloads show up to 9.65x speedup over NCCL and up to 3.34x improvement over prior compression-assisted collective libraries.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jiamin Wang, Zhijing Ye, Xiaodong Yu
- 发布：2026-09-18；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
