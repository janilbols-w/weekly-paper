---
title: "FluxMoE: Decoupling Expert Residency for High-Performance MoE Serving"
description: "Mixture-of-Experts (MoE) models have become mainstream for scaling language models to hundreds of billions of expert parameters."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2604.02715) · [PDF](https://arxiv.org/pdf/2604.02715)

## 一句话摘要

Mixture-of-Experts (MoE) models have become mainstream for scaling language models to hundreds of billions of expert parameters.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) models have become mainstream for scaling language models to hundreds of billions of expert parameters. Despite sparse expert activation, existing inference engines keep all experts GPU-resident, crowding out the key-value cache in large-batch, long-output offline workloads. We present FluxMoE, which decouples experts from physical GPU residency and adapts their footprint to available memory through a new \emph{expert paging} abstraction. FluxMoE combines PagedTensor for transparent remapping, a bandwidth-balanced hierarchy spanning losslessly compressed GPU memory and host DRAM, and a budget-aware residency planner. Unlike CPU-GPU co-inference and whole-layer offloading, FluxMoE streams weights on demand while keeping expert computation on GPUs. We implement FluxMoE atop vLLM and evaluate it on three MoE models. For GLM-4.5 on 8$\times$H20 GPUs, FluxMoE delivers up to 7.2$\times$ vLLM's throughput and 79.0\% lower average Time-Per-Output-Token (TPOT), without measurable model-quality loss using lossless compression. For Mixtral-8$\times$7B-Instruct on 2$\times$L40S GPUs, where weight-resident vLLM cannot fit, FluxMoE delivers 4.3$\times$ KTransformers's throughput and 29.1\% lower average TPOT.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory, offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qingxiu Liu, Yongchao He, Runhan Jiang, Zion Wang, Bohan Zhao, Mi Zhang, Patrick P. C. Lee
- 发布：2026-09-11；更新：2026-09-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
