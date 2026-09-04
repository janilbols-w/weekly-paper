---
title: "KernelFoundry: Hardware-aware evolutionary GPU kernel optimization"
description: "GPU kernel optimization challenges LLMs beyond standard coding tasks, as it requires an understanding of hardware architecture, parallel computing optimization strategies, and profiling outputs."
---

**评分：53/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2603.12440) · [PDF](https://arxiv.org/pdf/2603.12440)

## 一句话摘要

GPU kernel optimization challenges LLMs beyond standard coding tasks, as it requires an understanding of hardware architecture, parallel computing optimization strategies, and profiling outputs.

## 为什么值得关注

待编辑增强。

## 摘要原文

GPU kernel optimization challenges LLMs beyond standard coding tasks, as it requires an understanding of hardware architecture, parallel computing optimization strategies, and profiling outputs. However, most existing approaches leveraging LLMs for kernel generation apply standard prompting and feedback loops, considering hardware only through profiling feedback. We introduce KernelFoundry, an evolutionary framework that efficiently explores the space of GPU kernels through (1) MAP-Elites quality diversity search with kernel-specific behavioral dimensions to sustain exploration; (2) meta-prompt evolution that co-evolves prompts with kernels to uncover task-specific optimization strategies, and (3) a template-based parameter optimization approach to tune kernels to inputs and hardware. We evaluate this framework on Kernel-Bench, robust-kbench and custom tasks, generating SYCL kernels as a cross-platform GPU programming paradigm, and CUDA kernels for comparison to prior work. Our approach consistently outperforms the baseline methods and achieves an average speedup of 2.3 on KernelBench for SYCL. Moreover, KernelFoundry is implemented as a distributed framework with remote access to diverse hardware, allowing quick benchmarking and featuring a flexible user input layer to support kernel generation for a wide range of real use cases beyond benchmarking.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 24 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu kernel, kernel generation, kernel optimization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Nina Wiedemann, Quentin Leboutet, Michael Paulitsch, Diana Wofk, Benjamin Ummenhofer
- 发布：2026-09-04；更新：2026-09-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
