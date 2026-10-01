---
title: "Efficient Expert-Parallel Communication on PCIe-Connected Consumer GPUs"
description: "Expert parallelism (EP) enables inference of large Mixture-of-Experts (MoE) models by placing their experts across multiple GPUs, but requires substantial communication between GPUs at every MoE layer."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2609.40093) · [PDF](https://arxiv.org/pdf/2609.40093)

## 一句话摘要

Expert parallelism (EP) enables inference of large Mixture-of-Experts (MoE) models by placing their experts across multiple GPUs, but requires substantial communication between GPUs at every MoE layer.

## 为什么值得关注

待编辑增强。

## 摘要原文

Expert parallelism (EP) enables inference of large Mixture-of-Experts (MoE) models by placing their experts across multiple GPUs, but requires substantial communication between GPUs at every MoE layer. As contemporary MoE models activate more experts per token, this communication accounts for a growing fraction of inference time. The cost becomes particularly pronounced on PCIe-based consumer GPU systems, where all inter-GPU transfers traverse CPU memory. However, existing MoE-specialized EP communication libraries assume that direct GPU-to-GPU access is available, largely overlooking consumer GPUs. Therefore, most LLM frameworks instead rely on NCCL, whose CPU-staged communication incurs redundant PCIe transfers and competes with expert computation for GPU resources, limiting their overlap. We present ThunderEP, a novel communication design for such systems that removes the relay hops of traditional ring algorithm, moves data through DMA engines to avoid compute resource contention, and minimizes synchronization latency by reducing the polling overhead of completion flags in CPU memory. We integrate the proposed design into vLLM and evaluate it on three widely used MoE models. Experiments on two PCIe systems equipped with RTX 4090 and RTX 5090 GPUs show that ThunderEP achieves average speedups of 2.00$\times$ and 1.53$\times$ over NCCL for dispatch and combine, respectively, and up to 1.66$\times$ end-to-end speedup over state-of-the-art MoE inference frameworks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: moe inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jaehwan Lee, Sangmin Lee, Chaewon Kim, Junsik Shin, Jaejin Lee
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
