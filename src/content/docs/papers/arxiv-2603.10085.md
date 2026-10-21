---
title: "KernelClaw: A Multi-Agent Framework for GPU Kernel Optimization with Dual-Memory Mechanisms"
description: "Improving GPU kernel efficiency is crucial for efficient AI systems."
---

**评分：58/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2603.10085) · [PDF](https://arxiv.org/pdf/2603.10085)

## 一句话摘要

Improving GPU kernel efficiency is crucial for efficient AI systems.

## 为什么值得关注

待编辑增强。

## 摘要原文

Improving GPU kernel efficiency is crucial for efficient AI systems. Recent work has explored leveraging large language models (LLMs) for GPU kernel generation and optimization. However, existing LLM-based kernel optimization pipelines typically rely on opaque, implicitly learned heuristics within the LLMs to determine optimization strategies. This leads to inefficient trial-and-error and weakly interpretable optimizations. Our key insight is to replace implicit heuristics with expert optimization knowledge that is aware of task trajectories. Specifically, we present KernelClaw, a multi-agent framework with a dual-level memory architecture. KernelClaw operates by coordinating agents with long-term memory of reusable expert knowledge and short-term memory to prevent repetitive backtracking. On KernelBench Levels 1-3, KernelClaw achieves a 100% success rate and average speedups of 6.98x, 7.89x, and 1.94x over Torch Eager on Levels 1, 2, and 3, respectively, outperforming prior baselines. Code is available at https://github.com/0satan0/KernelMem/.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 24 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu kernel, kernel generation, kernel optimization
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Qitong Sun, Jun Han, Tianlin Li, Zhe Tang, Sheng Chen, Fei Yang, Aishan Liu, Xianglong Liu, Yang Liu
- 发布：2026-10-20；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/0satan0/KernelMem/](https://github.com/0satan0/KernelMem/)
- 阅读深度：metadata
