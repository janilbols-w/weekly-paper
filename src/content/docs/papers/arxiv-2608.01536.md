---
title: "Celty: SpMSpV GPU Kernel and SIMT Co-Design for Efficient Dual-Sparse LLM Inference"
description: "Large Language Models (LLMs) increasingly rely on sparsity to cut inference cost, but most prior work exploits a single sparsity source and targets batched multi-user inference."
---

**评分：55/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2608.01536) · [PDF](https://arxiv.org/pdf/2608.01536)

## 一句话摘要

Large Language Models (LLMs) increasingly rely on sparsity to cut inference cost, but most prior work exploits a single sparsity source and targets batched multi-user inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) increasingly rely on sparsity to cut inference cost, but most prior work exploits a single sparsity source and targets batched multi-user inference. Dual-sparsity, which pairs unstructured weight pruning with runtime activation sparsity, offers a compelling size-accuracy-latency tradeoff for single-user decoding, but forms a Sparse Matrix-Sparse Vector (SpMSpV) workload that existing GPU kernels handle poorly. We propose Celty, a co-designed sparse format, GPU kernel, and SIMT microarchitecture for SpMSpV in LLM inference. Celty's Run-Length Compressed CSC (RLC-CSC) format enables vectorized loading of compressed weight columns and exploits both sparsity sources to skip memory accesses, accumulating partial products in shared memory. The Celty Sparse SIMT Core then adds a pipelined RLC decoder that removes software index reconstruction and repurposes local register files for conflict-free accumulation, operating on the same compressed representation. The kernel alone achieves up to 2.8x over cuBLAS; with the Sparse SIMT Core, speedup reaches 5.3x over cuBLAS at 70% dual-sparsity.

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
- 发布：2026-08-02；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/RuokaiYin/Celty](https://github.com/RuokaiYin/Celty)
- 阅读深度：metadata
