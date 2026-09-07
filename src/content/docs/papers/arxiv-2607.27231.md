---
title: "KernelGenBench: A Multi-Source and Multi-Chip Benchmark for LLM-based Kernel Generation"
description: "Modern AI systems depend on specialized accelerator kernels, whose development is complicated by increasingly diverse operators and hardware."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2607.27231) · [PDF](https://arxiv.org/pdf/2607.27231)

## 一句话摘要

Modern AI systems depend on specialized accelerator kernels, whose development is complicated by increasingly diverse operators and hardware.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern AI systems depend on specialized accelerator kernels, whose development is complicated by increasingly diverse operators and hardware. LLMs and agentic systems promise to automate this work, but existing evaluations do not show whether their performance transfers across operator sources and hardware platforms, or what such transfer costs. We present KernelGenBench, the first unified multi-source and multi-chip infrastructure for evaluating LLM- and agent-generated Triton kernels. With a common Triton target spanning six hardware platforms, it provides the broadest cross-vendor hardware coverage among existing kernel-generation benchmarks. We report two controlled analytical views: KernelGenBench-MS (Multi-Source) covers 210 operators from PyTorch ATen, production vLLM operators, and proprietary cuBLAS routines, while KernelGenBench-MC (Multi-Chip) evaluates a semantically stable 110-operator subset across six hardware platforms. Our evaluation consumed over 15 billion tokens. Agentic execution improved correctness, but no method dominated across sources and platforms: vLLM posed the strongest correctness challenge, cuBLAS set the highest performance ceiling, and AutoKernel accuracy fell from 87% on NVIDIA to 25% on Iluvatar CoreX. These improvements were costly: specialized agents averaged 4.99 million tokens per successful operator, rising to 6.25 million for CUDA Optimized Skill. The results establish operator source, hardware platform, and agentic scaffold as distinct dimensions of kernel-generation capability, and show that success in a familiar source-hardware setting is not a reliable proxy for deployment readiness.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kernel generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Peiyu Zang, Jian Tao, Jialing Zhang, Yichen Yuan, Wentao Zhang, Guang Liu, Yonghua Lin
- 发布：2026-09-07；更新：2026-09-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
