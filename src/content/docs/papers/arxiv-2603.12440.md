---
title: "KernelFoundry: Hardware-aware evolutionary GPU kernel optimization"
description: "KernelFoundry 用进化搜索优化 GPU kernel：以 MAP-Elites 保持行为多样性，让提示词与 kernel 共同演化，并用模板化参数搜索适配输入与硬件。框架覆盖跨平台 SYCL 与 CUDA，在 KernelBench、robust-kbench 和自定义任务上评估；摘要报告其 SYCL kernel 在 KernelBench 上获得平均 2.3 倍加速。"
---

**评分：53/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2603.12440) · [PDF](https://arxiv.org/pdf/2603.12440)

## 一句话摘要

KernelFoundry 用进化搜索优化 GPU kernel：以 MAP-Elites 保持行为多样性，让提示词与 kernel 共同演化，并用模板化参数搜索适配输入与硬件。框架覆盖跨平台 SYCL 与 CUDA，在 KernelBench、robust-kbench 和自定义任务上评估；摘要报告其 SYCL kernel 在 KernelBench 上获得平均 2.3 倍加速。

## 为什么值得关注

高性能 kernel 生成的难点不只是写出正确代码，还要持续探索并针对具体硬件调参。将多样性搜索、提示演化和实机测量结合，有助于自动化发现算子优化策略，也适合扩展为异构硬件基准基础设施。

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
- 限制：摘要没有给出具体 GPU、基线构成、正确性容差、搜索预算或所用模型成本，因此尚不能判断 2.3 倍收益在不同硬件和真实工作负载上的稳定性。分布式远程评测还会引入设备一致性与调度开销。

## 元数据

- 作者：Nina Wiedemann, Quentin Leboutet, Michael Paulitsch, Diana Wofk, Benjamin Ummenhofer
- 发布：2026-09-04；更新：2026-09-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：abstract
