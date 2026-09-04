---
title: "Lot Machine: Multimodal Lot Extraction from Auction Catalogs"
description: "For provenance research and art market studies, auction catalogs are an essential resource to trace specific objects over time and space."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2608.30510v2) · [PDF](https://arxiv.org/pdf/2608.30510v2)

## 一句话摘要

For provenance research and art market studies, auction catalogs are an essential resource to trace specific objects over time and space.

## 为什么值得关注

待编辑增强。

## 摘要原文

For provenance research and art market studies, auction catalogs are an essential resource to trace specific objects over time and space. While historical auction catalogs follow established domain conventions, their internal formatting remains highly variable, and their large-scale analysis is currently restricted by the lack of machine-readable representations of the auction lots. We propose a pipeline to automatically extract structured lot-level metadata from German Sales, a large database of historical auction and sales catalogs from the 19th and 20th centuries. Using a manually annotated test set of representative catalog pages, we evaluate Vision-Language Models (VLMs) under varying prompt strategies and constrained decoding frameworks. To reflect the practical constraints faced by cultural heritage institutions, including budget, compute resources, and data privacy requirements, we benchmark the methods across different deployment modes ranging from commercial providers to locally hosted, quantized models. We find that commercial endpoints establish the performance ceiling, while institutional gateways offer a viable, privacy-preserving alternative. Local deployments remain feasible, but strictly require enforcing the output structure during generation to guarantee a valid JSON format. While varying degrees of human-in-the-loop correction are still necessary, this work demonstrates that a VLM-based pipeline can successfully unlock historical auction catalogs for large-scale automated analysis.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Mathias Zinnen, Alisha Mund, Sabine Lang, Lukas Hüttner, Thomas Gorges, Vincent Christlein
- 发布：2026-08-31；更新：2026-09-01
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/mathiaszinnen/auction-lot-extraction](https://github.com/mathiaszinnen/auction-lot-extraction)
- 阅读深度：metadata
