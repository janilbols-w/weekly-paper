---
title: "Elastic Precision: Software-Hardware Co-Design of a Mixed-Precision Architecture for Long-Context LLM Inference"
description: "Low-bit quantization reduces the data movement and computation costs of large language model (LLM) inference, but uniform widths can waste precision and degrade model quality."
---

**评分：45/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2611.00915) · [PDF](https://arxiv.org/pdf/2611.00915)

## 一句话摘要

Low-bit quantization reduces the data movement and computation costs of large language model (LLM) inference, but uniform widths can waste precision and degrade model quality.

## 为什么值得关注

待编辑增强。

## 摘要原文

Low-bit quantization reduces the data movement and computation costs of large language model (LLM) inference, but uniform widths can waste precision and degrade model quality. Existing mixed-precision methods do not fully account for how the other input of the current GEMM tile affects output error when selecting one input's width. Using both inputs to guide precision introduces additional estimation and selection overheads on conventional hardware. We propose Coffee, a runtime precision allocation architecture for long-context LLM inference. Under a fixed average bit-width budget, Coffee combines statistics from both current input matrices to estimate output errors at candidate widths and select each subarray's two input widths, allocating more bits where they yield greater estimated error reductions. Its mixed-precision hardware supports the selected widths in data access and computation, while overlapping error estimation and width selection with transfers and computation to limit stalls. The same read path supports attention-guided KV reads during decoding, reducing memory traffic. Coffee achieves lower perplexity and higher average zero-shot accuracy than the evaluated quantization baselines, and higher long-context retrieval recall than PLENA. For long-context decoding, system modeling projects up to $2.55\times$ the throughput and $2.61\times$ the energy efficiency of the reconfigured PLENA baseline, and up to $4.96\times$ and $12.56\times$, respectively, compared with the B200 GPU baseline.

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

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Boyang Chen, Xiao Wu, Haoran Wu, Yiren Zhao
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
