---
title: "Spike-Aware INT8 Execution for Spiking Language Models on Commodity CPUs"
description: "Binary spike activations allow a language-model runtime to read only active weight columns and replace multiplications by weight sums."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2606.03026) · [PDF](https://arxiv.org/pdf/2606.03026)

## 一句话摘要

Binary spike activations allow a language-model runtime to read only active weight columns and replace multiplications by weight sums.

## 为什么值得关注

待编辑增强。

## 摘要原文

Binary spike activations allow a language-model runtime to read only active weight columns and replace multiplications by weight sums. We implement this execution strategy in C++ for an 874M-parameter spike-gated language model. Sparse projections use column-major INT8 weights, integer accumulation, and one scale application per output channel; dense projections retain row-major access and FP32 activations. In a single-thread comparison using an early checkpoint, INT8 achieves 23.31 tokens/s versus 9.82 for FP32, while reducing weight storage from 3355.2 to 1087.4 MiB. A variant using INT4 on dense projections saves a further 17.4% of storage but reduces decode throughput by 46.6%. On an AMD Ryzen 7 5800X, the final INT8 checkpoint achieves 22.63 tokens/s on one thread and 47.90 on four threads; 512-token prefill reaches 94.68 tokens/s on eight threads. A separate ARM output-head case study records higher trimmed decode-window energy metrics for two candidate-verification configurations. The results characterize how activation-specific layouts and quantized kernels support CPU deployment of a spike-gated language model.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, int8, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Ting Liu
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
