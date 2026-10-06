---
title: "Gefen: Optimized Stochastic Optimizer"
description: "AdamW is a default optimizer for deep learning, but its moment states add two parameter-sized buffers to training memory, increasing the cost of large-scale pretraining."
---

**评分：50/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2606.13894) · [PDF](https://arxiv.org/pdf/2606.13894)

## 一句话摘要

AdamW is a default optimizer for deep learning, but its moment states add two parameter-sized buffers to training memory, increasing the cost of large-scale pretraining.

## 为什么值得关注

待编辑增强。

## 摘要原文

AdamW is a default optimizer for deep learning, but its moment states add two parameter-sized buffers to training memory, increasing the cost of large-scale pretraining. We propose Gefen, a memory-efficient optimizer that automatically shares second-moment estimates across parameter blocks and quantizes the first moment using a learned codebook. Gefen reduces AdamW's optimizer memory footprint by up to 8x while maintaining performance, saving 6.5 GiB per billion parameters. Prior work shares second moments across parameters grouped along the Hessian's block-diagonal structure, but relies on hand-specified architectural rules and leaves unexplained why such grouping works. We prove that large mixed Hessian entries constrain the ratio of squared gradients toward one, explaining why shared second moments are accurate when the squared gradients they pool are similar. The Hessian need not be computed: its block structure is inherited by squared gradients, allowing blocks to be found directly. Gefen therefore infers block structure from initial squared gradients, requiring no architecture-specific metadata or user-tuned hyperparameters beyond AdamW defaults. Gefen learns an exact histogram-based dynamic-programming quantization codebook and reuses the blocks for first-moment scaling. Across diverse pretraining experiments, Gefen achieves the lowest peak optimizer memory among compared methods that maintain AdamW-level performance. In single-machine and distributed training, the reduced footprint enables larger microbatches and substantially improves throughput over AdamW, making Gefen a drop-in replacement that can train larger models or use larger global batch sizes. We provide the complete Python implementation, including fused CUDA kernels at https://github.com/ndvbd/Gefen

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distributed training
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Nadav Benedek, Tomer Koren, Ohad Fried
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/ndvbd/Gefen](https://github.com/ndvbd/Gefen)
- 阅读深度：metadata
