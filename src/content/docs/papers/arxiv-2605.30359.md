---
title: "Kernel Foundry: A Diagnosis-driven Evolutionary Kernel Optimizer with Multi-Experts"
description: "Generating high-performance GPU kernels remains challenging due to the need for both correctness and hardware-aware optimization."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2605.30359) · [PDF](https://arxiv.org/pdf/2605.30359)

## 一句话摘要

Generating high-performance GPU kernels remains challenging due to the need for both correctness and hardware-aware optimization.

## 为什么值得关注

待编辑增强。

## 摘要原文

Generating high-performance GPU kernels remains challenging due to the need for both correctness and hardware-aware optimization. While large language models (LLMs) show promise in code generation, they often fail to produce kernels that are both correct and efficient. We propose Kernel Foundry, a diagnosis-driven evolutionary framework for automatic GPU kernel optimization. Our method combines expert-guided, retrieval-augmented initialization with a multi-island evolutionary search, where candidate kernels are iteratively refined using structured diagnostic feedback. A centralized experience library accumulates reusable optimization knowledge to guide subsequent evolution, while explicit mechanisms prevent cheating behaviors that bypass kernel-level computation. Experiments on KernelBench show that our method consistently improves both correctness and performance over strong baselines, achieving up to 100% correctness on Level~2.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu kernel, kernel optimization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zixuan Huang, Da Chen, Kecheng Huang, Lihao Yin, Xing Li, Huiling Zhen, Mingxuan Yuan, Zili Shao
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
