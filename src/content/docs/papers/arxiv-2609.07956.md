---
title: "Streaming Hierarchical Inference with Tabular Foundation Models"
description: "Tabular Foundation Models (TFMs) have recently demonstrated strong predictive performance through in-context learning, but their deployment in high-throughput data streams remains challenging due to communication overhead and latency."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2609.07956) · [PDF](https://arxiv.org/pdf/2609.07956)

## 一句话摘要

Tabular Foundation Models (TFMs) have recently demonstrated strong predictive performance through in-context learning, but their deployment in high-throughput data streams remains challenging due to communication overhead and latency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Tabular Foundation Models (TFMs) have recently demonstrated strong predictive performance through in-context learning, but their deployment in high-throughput data streams remains challenging due to communication overhead and latency. We propose \textit{HINT}, a hierarchical inference framework that combines edge-based retrieval with cloud-based TFM inference. A graph-based approximate nearest neighbor memory maintained over a sliding window provides local predictions and uncertainty estimates, allowing confident samples to be processed locally while uncertain instances are selectively offloaded, together with their retrieved context, to a cloud-hosted TFM. The framework exposes an offloading threshold and a neighborhood retrieval policy that can be varied to balance predictive performance and communication cost. Experiments show \textit{HINT} consistently identifies favorable trade-offs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Vitor Crista, Afonso Louren\c{c}o, Diogo Martinho, Goreti Marreiros
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
