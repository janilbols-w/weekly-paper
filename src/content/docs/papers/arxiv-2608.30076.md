---
title: "Budget-Aware Compression Pipeline for Single-GPU LLM Inference: Methods, Trade-offs, and Coupling Effects"
description: "Single-GPU deployment of 70B-parameter language models on an NVIDIA GPU is constrained by device memory, long-context throughput, and engineering integration cost."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.30076) · [PDF](https://arxiv.org/pdf/2608.30076)

## 一句话摘要

Single-GPU deployment of 70B-parameter language models on an NVIDIA GPU is constrained by device memory, long-context throughput, and engineering integration cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Single-GPU deployment of 70B-parameter language models on an NVIDIA GPU is constrained by device memory, long-context throughput, and engineering integration cost. We cast single-GPU inference as a budget-aware design problem over these three axes and study how pruning, quantization, and KV-cache compression interact under realistic execution. Controlled ablations show that layer-wise pruning makes weight quantization more robust. KV-cache sparsification complements INT8 KV quantization by reducing memory without hurting decoding speed, while static vector quantizers often conflict with dynamic caching. Guided by these coupling results and explicit budget tracking, we assembled a practical pipeline and compressed a 70B model to about 33 GB, sustained about 57 tokens/s on 10k token prompts on a single A40, and kept absolute accuracy within 5% on common and reasoning benchmarks. We contribute design rules and a reproducible evaluation protocol that jointly report quality, memory, and end-to-end speed, and we provide a foundation for automated pipeline search under realistic single-GPU constraints.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hongyu Yu, Yifei Shen
- 发布：2026-08-30；更新：2026-09-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
