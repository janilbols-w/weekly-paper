---
title: "Torcalia.jl: An MPI-based Runtime System for Asynchronous Task Parallelism in Julia"
description: "Designed to address the two-language problem, the Julia programming language provides a powerful platform for developing high-performance scientific computing and machine learning applications."
---

**评分：45/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2611.30776) · [PDF](https://arxiv.org/pdf/2611.30776)

## 一句话摘要

Designed to address the two-language problem, the Julia programming language provides a powerful platform for developing high-performance scientific computing and machine learning applications.

## 为什么值得关注

待编辑增强。

## 摘要原文

Designed to address the two-language problem, the Julia programming language provides a powerful platform for developing high-performance scientific computing and machine learning applications. Such applications increasingly exhibit irregular, adaptive, or data-driven workloads for which traditional bulk-synchronous parallel (BSP) models often struggle to efficiently exploit the available parallelism. Asynchronous many-task (AMT) runtime systems offer a compelling alternative, decomposing computations into fine-grained tasks that are dynamically scheduled across the hierarchical architecture of modern HPC systems. This paper introduces Torcalia.jl, a Julia package designed to orchestrate the asynchronous execution of tasks across both shared and distributed memory environments. Built on top of MPI.jl and Julia's native multithreading, Torcalia employs a dependency-aware task scheduling scheme that combines the work-sharing and work-stealing paradigms to achieve adaptive load balancing. Tasks can be nested arbitrarily, enabling applications to exploit multiple levels of parallelism, while application-level distributed shared memory (DSM) extends task-based shared-memory programming to multi-node clusters. Beyond task-based programming, the proposed library supports skeletal programming, providing high-level abstractions that facilitate the implementation of parallel applications at scale. Evaluated on the ARIS supercomputer using four diverse workloads, Torcalia demonstrates strong scalability, reducing wall-clock time by up to 18.1% compared with Dagger, a state-of-the-art task-based engine in Julia. The source code of Torcalia.jl is publicly available at https://github.com/CEID-HPCLAB/Torcalia.jl.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: load balancing
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Argiris Sofotasios, Dimitris Metaxakis, Chrysostomos Stylios, Panagiotis Hadjidoukas
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/CEID-HPCLAB/Torcalia.jl](https://github.com/CEID-HPCLAB/Torcalia.jl)
- 阅读深度：metadata
