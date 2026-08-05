---
title: "Studying quantization trade-offs for efficient inference deployment in machine translation"
description: "Deploying large language models in realistic server environments poses challenges, as the system needs to provide high-quality responses with low latency."
---

**评分：53/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2607.29397) · [PDF](https://arxiv.org/pdf/2607.29397)

## 一句话摘要

Deploying large language models in realistic server environments poses challenges, as the system needs to provide high-quality responses with low latency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deploying large language models in realistic server environments poses challenges, as the system needs to provide high-quality responses with low latency. Quantization is a common approach to reduce the memory footprint and improve inference efficiency, yet its impact on latency and throughput is rarely evaluated under controlled, orchestration-level workloads. In this work we study the quantization trade-offs of two translation model families, EuroLLM \citep{martins2025eurollm} and Hy-MT2 \citep{zheng2026hy} across five models ranging from 1.7B to 22B for efficient deployment on a single A100 or H100 GPU. We demonstrate that combining a document-chunking strategy with W4A8 or W8A8 quantization improves the latency-throughput Pareto-curve under a wide range of workloads. Furthermore, since standard machine translation (MT) benchmarks rely on isolated sentences and fail to capture long-context dynamics, we introduce a document-level evaluation from WMT24++ to assess how text chunking strategies affect translation quality under quantization. Our results reveal that standard segment-level evaluation can fail to predict the interaction between quantization and long-context document translation. While Hy-MT2 remains robust under quantization, EuroLLM shows strong sensitivity and translation quality collapses rapidly for all considered quantization formats. Overall, our experiments show that the trade-off between inference efficiency and translation quality depends not only on the quantization format, but also on the choice of text chunking strategy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 15 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jim Zhao, Sohir Maskey, Koen Oostermeijer, Douglas Orr, Teryn Jones
- 发布：2026-08-05；更新：2026-08-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
