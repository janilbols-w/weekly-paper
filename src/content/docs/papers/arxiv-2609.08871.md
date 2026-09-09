---
title: "Towards Standardized Evaluation of GPU Memory Safety with GMSBench"
description: "As GPUs become increasingly integral to high-performance computing and machine learning, ensuring memory safety in GPU programs has become crucial for reliable and secure execution."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2609.08871) · [PDF](https://arxiv.org/pdf/2609.08871)

## 一句话摘要

As GPUs become increasingly integral to high-performance computing and machine learning, ensuring memory safety in GPU programs has become crucial for reliable and secure execution.

## 为什么值得关注

待编辑增强。

## 摘要原文

As GPUs become increasingly integral to high-performance computing and machine learning, ensuring memory safety in GPU programs has become crucial for reliable and secure execution. However, evaluating GPU memory safety techniques remains challenging due to the lack of comprehensive and standardized benchmarks. In this paper, we present GMSBench, a GPU memory safety benchmark designed to evaluate a broad range of memory safety violations across different GPU memory spaces and execution scenarios. GMSBench comprises 149 self-contained CUDA tests spanning spatial, temporal, and concurrency errors. The suite provides a standardized foundation for the evaluation and comparative analysis of GPU memory safety mechanisms and helps expose gaps in their detection coverage. We demonstrate the utility of GMSBench by evaluating Compute Sanitizer, a widely used GPU memory error detection tool across multiple GPU architectures.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Saurabh Singh (Georgia Institute of Technology), Jaewon Lee (Microsoft), Seonjin Na (NVIDIA), Hyesoon Kim (Georgia Institute of Technology)
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
