---
title: "KernelZero: Co-Evolving Proposer and Coder for Continuously Improved GPU Kernel Generation"
description: "High-performance GPU kernels are essential to modern machine learning systems, yet automatically generating kernels that are both correct and efficient remains challenging."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2609.33074) · [PDF](https://arxiv.org/pdf/2609.33074)

## 一句话摘要

High-performance GPU kernels are essential to modern machine learning systems, yet automatically generating kernels that are both correct and efficient remains challenging.

## 为什么值得关注

待编辑增强。

## 摘要原文

High-performance GPU kernels are essential to modern machine learning systems, yet automatically generating kernels that are both correct and efficient remains challenging. Existing LLM-based approaches face two major limitations: the scarcity of high-quality training data aligned with the model's current capabilities, and the inherent trade-off between kernel correctness and performance. To address these challenges, we propose KernelZero, a co-evolution framework that continuously improves GPU kernel generation through two specialized models: a Proposer that generates Torch modules from API sets and a Coder that translates them into CUDA or Triton kernels. KernelZero uses a frontier-driven module generation mechanism to continuously produce capability-aligned training modules based on the Coder's current weaknesses. It further introduces Correctness-Aware Group Relative Policy Optimization (CA-GRPO), which optimizes performance only after correctness becomes sufficiently reliable. By alternating the optimization of the Proposer and Coder, KernelZero forms an automatic curriculum that enables targeted and training-efficient capability improvement. Empirically, KernelZero-7B surpasses Claude-4.5-Sonnet on CUDA and DeepSeek-V4-Pro on Triton. On KernelBench Level 1 and 2, it achieves CUDA pass@1 scores of 75.8% and 69.6%, respectively, with pass@10 reaching 100% and 97%. On Triton, it achieves pass@1 scores of 77.2% and 72.5%, respectively.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu kernel, kernel generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Changxin Ke, Rui Zhang, Zixiang Fang, Zhenghong Li, Yuanbo Wen, Jiashuo Shen, Shuo Wang, Jiaming Guo, Ling Li, Qi Guo, Yunji Chen
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
