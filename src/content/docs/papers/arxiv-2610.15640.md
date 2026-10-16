---
title: "Context-Aware Precision Scheduling for Small Language Models"
description: "Small language models (SLMs) used as on-device agents must balance accuracy and latency as their context grows."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2610.15640v1) · [PDF](https://arxiv.org/pdf/2610.15640v1)

## 一句话摘要

Small language models (SLMs) used as on-device agents must balance accuracy and latency as their context grows.

## 为什么值得关注

待编辑增强。

## 摘要原文

Small language models (SLMs) used as on-device agents must balance accuracy and latency as their context grows. Mixed precision helps manage this tradeoff by assigning different precisions to weight tensors according to their size and sensitivity. However, these choices depend on the operating conditions, so a configuration selected for a short context may no longer provide the best tradeoff at a longer one. We calibrate a timing model from measurements at different precisions and context lengths, and combine it with tensor sensitivities to choose configurations under a latency or accuracy budget. We argue that fewer bits do not always mean faster execution, so our predictor estimates latency from calibrated execution costs rather than weight bytes alone. Under a latency budget, reading the larger key-value (KV) cache leaves less time for weight operations, leading the allocator to select lower precisions. This gives a schedule of tensor changes that can be prepared before execution. Our runtime follows the schedule while retaining the session's KV cache. We evaluate executed schedules on a laptop GPU, including a longer-context schedule with three weight formats and a tool-use benchmark measuring full response time and correctness. Under an accuracy budget, measured error from a quantized KV cache determines the budget left for weights. The allocator can raise or lower weight precision as this estimate changes. These experiments show where context-aware precision helps and where accuracy recovery remains limited.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: mixed precision, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mukund Athmaram, Manoj Rao, Liang Ma
- 发布：2026-10-11；更新：2026-10-11
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
