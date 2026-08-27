---
title: "DataKernelBench: Can LLMs Optimize Database Queries on GPUs?"
description: "GPUs increasingly accelerate database systems, but query-specific peak performance still often relies on hand-written kernels."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2608.25061) · [PDF](https://arxiv.org/pdf/2608.25061)

## 一句话摘要

GPUs increasingly accelerate database systems, but query-specific peak performance still often relies on hand-written kernels.

## 为什么值得关注

待编辑增强。

## 摘要原文

GPUs increasingly accelerate database systems, but query-specific peak performance still often relies on hand-written kernels. Existing LLM kernel benchmarks focus on machine learning operators, leaving irregular, heterogeneous, data-movement-heavy database-style operators untested. We introduce DataKernelBench, which translates SQL into validated PyTorch TorchPlan programs and evaluates LLMs that optimize either the core tensor-bounded snippet or the full query in CUDA or Triton through execution-guided repair. Across ten proprietary and open-weight models on TPC-H SF10 with an H100 GPU, the strongest full-query CUDA configuration achieves $2.11\times$ speedup over torch.compile at full pass rate. We find that higher-performing implementations commonly use kernel fusion and execution-strategy changes, stronger models benefit most from full-query specialization, and workload context matters more than hardware context. To handle data larger than GPU memory, we extend TorchPlan with Dask-cuDF for on-demand partition loading on TPC-H SF100 with four H100 GPUs, achieving $2.54\times$ speedup

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Gokul Karthik Kumar, Yotam Perlitz, Corey Lammie, Andrea Giovannini, Katja Hose
- 发布：2026-08-27；更新：2026-08-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
