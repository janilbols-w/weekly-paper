---
title: "vidax: A Unified JAX Framework for Video Generative Models on Accelerator Meshes"
description: "Open-source video generative models ship almost exclusively as PyTorch/CUDA reference implementations."
---

**评分：48/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.18077) · [PDF](https://arxiv.org/pdf/2609.18077)

## 一句话摘要

Open-source video generative models ship almost exclusively as PyTorch/CUDA reference implementations.

## 为什么值得关注

待编辑增强。

## 摘要原文

Open-source video generative models ship almost exclusively as PyTorch/CUDA reference implementations. This leaves Cloud TPU pods without a production-ready inference path, despite offering large, cost-effective accelerator memory pools ideal for long-sequence spatiotemporal attention. We present vidax, an open-source JAX/Flax inference engine and zero-copy PyTorch-to-JAX weight translator for modern video generation architectures. vidax covers a diverse set of spatiotemporal models --- including Diffusion Transformers, omnimodal Mixture-of-Transformers, 3D VAEs, text encoders, and native samplers --- with zero PyTorch dependency in the execution path. The framework unifies 1D tensor parallelism with DeepSpeed-Ulysses sequence parallelism on a single JAX sharding mesh, integrates TPU flash-attention kernels, and implements per-layer weight offloading to support reference resolutions that exceed single-device memory. We benchmark compile times, latency, and peak memory utilization on TPU v4-8 hardware, and document real-world numerical bugs surfaced during checkpoint translation. vidax is released open-source as a baseline for JAX and TPU video generation research.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Congyue Deng
- 发布：2026-09-16；更新：2026-09-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
