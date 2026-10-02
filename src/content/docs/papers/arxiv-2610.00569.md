---
title: "Scaling Collider Event Generation with Residual-Quantized Tokens"
description: "Full detector simulation and reconstruction of collider events are projected to become major bottlenecks at the High-Luminosity Large Hadron Collider, motivating the development of fast, ML-based surrogates."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.00569) · [PDF](https://arxiv.org/pdf/2610.00569)

## 一句话摘要

Full detector simulation and reconstruction of collider events are projected to become major bottlenecks at the High-Luminosity Large Hadron Collider, motivating the development of fast, ML-based surrogates.

## 为什么值得关注

待编辑增强。

## 摘要原文

Full detector simulation and reconstruction of collider events are projected to become major bottlenecks at the High-Luminosity Large Hadron Collider, motivating the development of fast, ML-based surrogates. At the same time, LLMs have driven fast progress in generative discrete modeling: autoregressive transformers trained on tokenized data now represent the state of the art across a range of generative tasks. We extend the discrete modeling paradigm by introducing a particle-level generative model trained on residual-quantized full-event data. We demonstrate the ability of this model family to perform conditional generation from detector-stable particles; we study its scaling behavior across a range of dataset and model sizes, characterize the effects of repeated data exposure and demonstrate that token-level loss systematically predicts downstream physical fidelity. These results provide an empirical framework for scalable collider full-event generation based on residual-quantized representations.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dan Godi, Dmitrii Kobylianskii, Eilam Gross
- 发布：2026-09-30；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
