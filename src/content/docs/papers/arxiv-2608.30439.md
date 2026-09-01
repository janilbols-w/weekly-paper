---
title: "Event-Driven Language Models with Sparse Neural Activity for Neuromorphic Hardware"
description: "Inference with transformer-based large language models (LLMs) is often limited by the memory-bound KV cache and quadratic attention cost."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.30439) · [PDF](https://arxiv.org/pdf/2608.30439)

## 一句话摘要

Inference with transformer-based large language models (LLMs) is often limited by the memory-bound KV cache and quadratic attention cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Inference with transformer-based large language models (LLMs) is often limited by the memory-bound KV cache and quadratic attention cost. State-space models (SSMs) mitigate this through linear attention and fixed-size recurrent states, but their large dense linear projections remain computationally expensive even after quantization. We introduce a method that induces sparse neural activity in heavily quantized linear-attention models with minimal performance loss. Activations below a per-projection trainable threshold ($\pm \Delta$) are nullified while preserving crucial outliers, achieving comparable performance to dense models with up to 4$\times$ fewer effective arithmetic operations. Targeting a multi-core, multi-chip neuromorphic platform, where event-driven execution converts unstructured sparsity into throughput at both the compute and communication levels, a capability GPU architectures fundamentally lack, we project up to 37$\times$ higher throughput and 16$\times$ lower power versus edge GPU inference of a comparable transformer-based model, and up to 5.4$\times$ improvements over the non-sparsified baseline. These results position sparse, quantized linear-attention models as a natural fit for deploying LLMs on event-driven multi-core platforms.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Simon Richter, Ruhai Lin, Jason Yik, Taylor Kergan, Rui-Jie Zhu, Farshad Moradi, Jason Eshraghian
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
