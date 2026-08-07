---
title: "Celty: SpMspV GPU Kernel and SIMT Co-Design for Efficient Dual-Sparse LLM Inference"
description: "Large Language Models (LLMs) increasingly rely on sparsity to reduce inference cost, but most prior work targets a single sparsity source-either weight or activation-and optimizes for batched multi-user inference."
---

**评分：55/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2608.01536) · [PDF](https://arxiv.org/pdf/2608.01536)

## 一句话摘要

Large Language Models (LLMs) increasingly rely on sparsity to reduce inference cost, but most prior work targets a single sparsity source-either weight or activation-and optimizes for batched multi-user inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) increasingly rely on sparsity to reduce inference cost, but most prior work targets a single sparsity source-either weight or activation-and optimizes for batched multi-user inference. Dual-sparsity, which combines unstructured weight pruning with runtime activation sparsity, offers a compelling tradeoff among model size, accuracy, and latency for single-user decoding, but formulates as a Sparse Matrix-Sparse Vector (spMspV) workload that existing GPU kernels handle poorly. We propose Celty, a co-designed sparse format, GPU kernel, and SIMT microarchitecture for efficient spMspV in LLM inference. At the kernel level, Celty introduces a Run-Length Compressed CSC (RLC-CSC) format that enables vectorized loading of compressed weight columns and exploits both sparsity sources to skip unnecessary memory accesses, with shared memory used for scattered partial-product accumulation. At the microarchitecture level, the Celty Sparse SIMT Core integrates a pipelined RLC decoder to eliminate software-level index reconstruction and repurposes local register files for conflict-free accumulation-operating directly on the same RLC-CSC format without data layout changes. The Celty GPU kernel achieves up to 2.8x speedup over cuBLAS and 2.4x over Flash-LLM. With the Sparse SIMT Core, speedups reach up to 5.3x over cuBLAS at 70% dual-sparsity.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 16 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu kernel
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Ruokai Yin, Priyadarshini Panda
- 发布：2026-08-02；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/RuokaiYin/Celty](https://github.com/RuokaiYin/Celty)
- 阅读深度：metadata
