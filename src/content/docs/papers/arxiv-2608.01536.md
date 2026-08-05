---
title: "Celty: SpMspV GPU Kernel and SIMT Co-Design for Efficient Dual-Sparse LLM Inference"
description: "Celty 针对权重与激活双稀疏形成的 SpMspV 负载，协同设计 RLC-CSC 压缩格式、GPU Kernel 和稀疏 SIMT Core；软件 Kernel 相比 cuBLAS 最高 2.8×，专用核心在 70% 稀疏度下最高 5.3×。"
---

**评分：50/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2608.01536) · [PDF](https://arxiv.org/pdf/2608.01536)

## 一句话摘要

Celty 针对权重与激活双稀疏形成的 SpMspV 负载，协同设计 RLC-CSC 压缩格式、GPU Kernel 和稀疏 SIMT Core；软件 Kernel 相比 cuBLAS 最高 2.8×，专用核心在 70% 稀疏度下最高 5.3×。

## 为什么值得关注

单用户解码难以靠大 Batch 隐藏访存开销，双稀疏又不适配现有 GPU Kernel；该工作展示了数据格式、软件 Kernel 与微架构共同设计的潜在上限。

## 摘要原文

Large Language Models (LLMs) increasingly rely on sparsity to reduce inference cost, but most prior work targets a single sparsity source-either weight or activation-and optimizes for batched multi-user inference. Dual-sparsity, which combines unstructured weight pruning with runtime activation sparsity, offers a compelling tradeoff among model size, accuracy, and latency for single-user decoding, but formulates as a Sparse Matrix-Sparse Vector (spMspV) workload that existing GPU kernels handle poorly. We propose Celty, a co-designed sparse format, GPU kernel, and SIMT microarchitecture for efficient spMspV in LLM inference. At the kernel level, Celty introduces a Run-Length Compressed CSC (RLC-CSC) format that enables vectorized loading of compressed weight columns and exploits both sparsity sources to skip unnecessary memory accesses, with shared memory used for scattered partial-product accumulation. At the microarchitecture level, the Celty Sparse SIMT Core integrates a pipelined RLC decoder to eliminate software-level index reconstruction and repurposes local register files for conflict-free accumulation-operating directly on the same RLC-CSC format without data layout changes. The Celty GPU kernel achieves up to 2.8x speedup over cuBLAS and 2.4x over Flash-LLM. With the Sparse SIMT Core, speedups reach up to 5.3x over cuBLAS at 70% dual-sparsity.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu kernel
- quantitative claim detected
- no code link detected in metadata
- 限制：5.3× 结果依赖尚未商品化的专用 SIMT Core及 70% 双稀疏；需进一步核验稀疏化精度损失、格式转换、不同模型形状和批量负载下的端到端收益。

## 元数据

- 作者：Ruokai Yin, Priyadarshini Panda
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：abstract
