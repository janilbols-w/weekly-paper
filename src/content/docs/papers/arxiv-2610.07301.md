---
title: "A Pipelined FPGA Architecture for Banded Sparse Matrix Dense Matrix Multiplication in Longformer"
description: "Sparse attention mechanisms have become increasingly important for transformer models processing long input sequences due to their lower computational and memory complexity compared to full self-attention."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.07301) · [PDF](https://arxiv.org/pdf/2610.07301)

## 一句话摘要

Sparse attention mechanisms have become increasingly important for transformer models processing long input sequences due to their lower computational and memory complexity compared to full self-attention.

## 为什么值得关注

待编辑增强。

## 摘要原文

Sparse attention mechanisms have become increasingly important for transformer models processing long input sequences due to their lower computational and memory complexity compared to full self-attention. Longformer achieves this through a sliding-window attention mechanism that produces a structured banded sparse attention matrix. However, existing sparse transformer accelerators primarily target attention generation or unstructured sparsity, leaving sparse matrix--dense matrix multiplication (SpMM) for structured sparse attention largely unexplored. This paper presents a pipelined FPGA architecture for accelerating banded SpMM in Longformer. The proposed design exploits the predictable sparsity pattern of Longformer's attention matrix through a custom row-wise storage scheme with implicit indexing, eliminating the overhead of conventional sparse matrix formats while enabling regular memory accesses. The architecture employs parallel processing elements, pipelined adder trees, and a dual-path computation strategy to maximize throughput and hardware utilization. Implemented in Verilog and evaluated on an RFSoC platform using Vivado 2024.2, the accelerator sustains one complete dot-product result per clock cycle after an initial latency of 11 cycles while maintaining power consumption below 2.9 W. Operating at 100 MHz, the design achieves over 100 million dot-product outputs per second, demonstrating the effectiveness of directly exploiting structured sparsity for sparse transformer acceleration.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Phillip Pramberger, Athanasios Tziouvaras, Shreejith Shanker, George Floros
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
