---
title: "HPC-Bench: A Comprehensive Benchmark for High Performance Computing Codes"
description: "Large Language Models (LLMs) have shown strong capabilities in code generation and reasoning, motivating extensive benchmarks for evaluating functional correctness."
---

**评分：48/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2611.02752) · [PDF](https://arxiv.org/pdf/2611.02752)

## 一句话摘要

Large Language Models (LLMs) have shown strong capabilities in code generation and reasoning, motivating extensive benchmarks for evaluating functional correctness.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) have shown strong capabilities in code generation and reasoning, motivating extensive benchmarks for evaluating functional correctness. However, performance optimization in High-Performance Computing (HPC) poses fundamentally different challenges that are not captured by existing evaluations: HPC performance depends on low-level code, intricate memory access patterns, and computational kernels embedded within sophisticated execution contexts. We introduce HPC-Bench, a performance-grounded benchmark for evaluating LLMs as optimizers of computational kernels in realistic HPC workloads, including 114 workloads across 16 HPC computational motifs. HPC-Bench provides a fully automated, end-to-end evaluation pipeline that combines program-level correctness verification with two correctness-gated metrics, Fast@k and Speedup@k, to characterize reliability and speedup under a fixed sampling budget. Our evaluation of three representative LLMs across serial CPU, OpenMP, and CUDA settings shows that stricter speedup requirements substantially reduce the probability of finding a correct and fast optimization. HPC-Bench is available at https://github.com/Deep-Learning-Profiling-Tools/HPC-Bench.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Bowen Cui, Junyu Yin, Tejas Ramesh, Leo Lim, Oscar Hernandez, Keren Zhou
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Deep-Learning-Profiling-Tools/HPC-Bench](https://github.com/Deep-Learning-Profiling-Tools/HPC-Bench)
- 阅读深度：metadata
