---
title: "Unified Static-Dynamic Pruning for Efficient LLM Inference"
description: "The increasing deployment of large language models (LLMs) has magnified the computational and memory bottlenecks of autoregressive decoding, where low compute intensity and bandwidth-bound kernels dominate inference cost."
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.21985) · [PDF](https://arxiv.org/pdf/2607.21985)

## 一句话摘要

The increasing deployment of large language models (LLMs) has magnified the computational and memory bottlenecks of autoregressive decoding, where low compute intensity and bandwidth-bound kernels dominate inference cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

The increasing deployment of large language models (LLMs) has magnified the computational and memory bottlenecks of autoregressive decoding, where low compute intensity and bandwidth-bound kernels dominate inference cost. Weight pruning offers a promising remedy, but existing methods remain confined to either static pruning (SP), which permanently removes redundant weights but lacks adaptivity, or dynamic pruning (DP), which adapts to input sparsity but introduces runtime irregularity. This paper presents SPDP, a unified sparse-inference framework that integrates unstructured SP with input-adaptive DP for efficient LLM inference on GPUs. SPDP co-designs a new Tiled-Column-wise Bitmap Compressed (Tiled-CBC) format and two complementary GPU kernels: (1) a CUDA-core spMspV kernel featuring Hybrid Activation-aware Dynamic Shared-Memory Bitmap Decoding (HAD-SMBD) for fine-grained, runtime activation skipping, and (2) a Tensor-Core SpMM kernel optimized for prefill computation. This joint format-kernel design harmonizes static and dynamic sparsity, maintaining bandwidth-efficient memory access and high compute intensity under both phases of LLM inference. Comprehensive evaluations on inference-optimized GPUs demonstrate that SPDP achieves 1.24x-1.37x average speedup (up to 2.51x) over state-of-the-art sparse frameworks such as SpInfer, while matching perplexity with up to 25% higher sparsity. SPDP advances the inference efficiency-quality Pareto frontier, showing that unified static-dynamic pruning can deliver substantial throughput and performance-per-watt improvements in large-scale LLM serving.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jinhyeok Kim, Yejoon Lee, Jaeyoung Do
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
