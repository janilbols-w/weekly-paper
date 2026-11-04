---
title: "A Cross-Domain Matrix Engine for Signal Processing and Deep Neural Net Inference"
description: "Matrix multiplication dominates both PHY signal processing and Deep Neural Network (DNN) inference, yet these domains place opposing demands on the matrix engine."
---

**评分：50/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2611.03503) · [PDF](https://arxiv.org/pdf/2611.03503)

## 一句话摘要

Matrix multiplication dominates both PHY signal processing and Deep Neural Network (DNN) inference, yet these domains place opposing demands on the matrix engine.

## 为什么值得关注

待编辑增强。

## 摘要原文

Matrix multiplication dominates both PHY signal processing and Deep Neural Network (DNN) inference, yet these domains place opposing demands on the matrix engine. Signal processing requires low-latency execution of relatively small matrix operations, whereas DNN inference, particularly at large batch sizes, prioritizes high throughput and energy efficiency for large matrix multiplications. While offering efficient memory access profile, a Systolic Array (SA) adds fill and drain delays per matrix. Those can be amortized for large matrices but not for small matrices. Conversely, a tensor unit completes the kernel in few cycles but would require repeated reads of same operand tiles over large matrices. This makes SA too slow for signal processing and tensor too inefficient for AI. We show that this need not be a choice between systolic and tensor structuring of Multiply-Accumulate (MAC) units. We propose a single engine that operates primarily as a SA and, through low-cost reconfiguration, transforms into a tensor-style engine on a per-operation basis. MUXes create both the spatial reduction adder tree and temporal reduction accumulators from the existing MACs and registers within the systolic array. The proposed reconfigurable SA simulated using modified SCALESim simulator, verified on an Zynq 702 FPGA and synthesized using ASAP 7nm FinFET library. SCALE-Sim simulations shows up to 7.5x lower latency for small complex value PHY kernels. Even on DNN workloads, it achieves up to 1.65x speedups over vanilla SA execution with trivial increase of memory accesses, retaining the systolic array's memory access advantage. Synthesis results estimate reconfigurable fabric costs only 8% power and 13.6% area overheads.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 20 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Mehdi Safarpour
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
