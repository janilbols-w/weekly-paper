---
title: "Budgeting Bytes: A Windowed Storage Roofline and Dual-Budget Architecture Ablations for Storage-Bound LLM Decoding"
description: "Autoregressive decoding on cheap hardware is bound not by FLOPs but by the bytes each generated token must move across the slowest populated tier of a memory hierarchy."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.04238) · [PDF](https://arxiv.org/pdf/2609.04238)

## 一句话摘要

Autoregressive decoding on cheap hardware is bound not by FLOPs but by the bytes each generated token must move across the slowest populated tier of a memory hierarchy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Autoregressive decoding on cheap hardware is bound not by FLOPs but by the bytes each generated token must move across the slowest populated tier of a memory hierarchy. We treat bytes-per-token as a first-class design axis, organized by an address-determinism taxonomy that classifies parameters by when their fetch address becomes known during a token's forward pass (A0: at token sampling; A1: before attention; A2: layerwise data-dependent; A3: always read). This reduces prefetch scheduling to single-machine feasibility with release times, yielding a closed-form windowed roofline. We run dual-budget (bytes-per-token times storage) ablations across three sub-100M scales, then take the framework to real large-MoE deployment and report a substantial negative result the roofline predicts: on an 8GB edge board running Qwen3-30B-A3B (4-bit, 18GB), the model overflows RAM and decode is pinned at the eMMC bandwidth ceiling; predictive expert prefetch does not help -- not temporal-locality prefetch (net-negative), not even a trace-driven oracle with perfect prediction -- because the binding constraint is byte volume over a saturated bus, which prefetch cannot reduce. The lever that works is reducing bytes-per-token until the model fits the fast tier: quantized to fit a 16GB unified-memory device, the same model runs GPU-resident at 11.5 tok/s (22x). We reconcile this with GPU-serving expert-prefetch predictors: a frozen-model probe predicts Qwen3-30B routing from the pre-attention state at 91.2%, a scale-invariant predictability property, but this converts to throughput only where the fast tier caches most of the model and per-token transfer is comparable to compute -- measured to hold on an A100 PCIe-offload path and to fail on bandwidth-walled edge storage. Predictability is not speedup; we chart where the gap closes.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Hanhaodi Zhang
- 发布：2026-09-07；更新：2026-09-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
