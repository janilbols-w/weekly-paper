---
title: "Time Series Foundation Models on the Edge"
description: "Time series foundation models (TSFMs) forecast zero-shot with accuracy exceeding that of task-specific models, and the smaller ones fit on edge devices."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.30404) · [PDF](https://arxiv.org/pdf/2611.30404)

## 一句话摘要

Time series foundation models (TSFMs) forecast zero-shot with accuracy exceeding that of task-specific models, and the smaller ones fit on edge devices.

## 为什么值得关注

待编辑增强。

## 摘要原文

Time series foundation models (TSFMs) forecast zero-shot with accuracy exceeding that of task-specific models, and the smaller ones fit on edge devices. Operational deployments must refresh their forecast as new observations arrive, and privacy and latency requirements often force this refresh onto resource-constrained edge devices. To serve as a forecasting system there, a TSFM must refresh quickly, keep latency and peak memory bounded as the stream grows, and retain its accuracy as the observed history accumulates. Refreshing incrementally without altering the forecast requires temporal causality: non-causal models recompute at every update, causal attention admits a KV cache that grows linearly, and causal recurrent models update a fixed-size state in constant time and memory. We make these states persist across refreshes for every causal architecture and verify equivalence to full recomputation. We evaluate nine TSFM configurations on univariate forecasting against all three requirements, measuring accuracy as a function of context length, single-refresh latency, and latency and memory on streams of up to one million time steps on a server-grade GPU and three edge devices. No model gains on average accuracy beyond its trained context and most lose it well before the full history is reached, while KV caches leave latency and memory growing linearly with the retained history. TiRex-2 is the only one of the nine configurations meeting all three requirements: it refreshes in 14 ms on the GPU and 120 ms on a Raspberry Pi 5, keeps latency, energy and peak memory constant over a million steps, and retains its accuracy on the untruncated history.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Marco Pichler, Patrick Podest, G\"unter Klambauer, Sepp Hochreiter
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
