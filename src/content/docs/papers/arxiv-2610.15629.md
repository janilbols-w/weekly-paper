---
title: "The Price of Precision: A Calibrated Cost Model for Mixed-Precision LLM Serving"
description: "Choosing a mixed-precision configuration for large language model (LLM) serving trades speed against accuracy."
---

**评分：45/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](http://arxiv.org/abs/2610.15629v1) · [PDF](https://arxiv.org/pdf/2610.15629v1)

## 一句话摘要

Choosing a mixed-precision configuration for large language model (LLM) serving trades speed against accuracy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Choosing a mixed-precision configuration for large language model (LLM) serving trades speed against accuracy. Allocators that use average bit-width or a memory budget as a speed proxy can miss changes in the resource that limits execution. We argue that served speed can be limited by compute, weight loading, or key-value (KV) cache access, depending on the phase, batch size, and context length. A byte-based proxy does not capture all of these costs, so fewer bits do not always mean faster serving. To address this gap, we build a cost model that accounts for the binding resource and use it in two ways. First, as a predictor: given a configuration and operating point, it estimates serving latency using constants calibrated for the model, GPU, and serving stack. We evaluate its accuracy across three hardware classes. Second, as an allocator: we combine modeled time costs with measured per-tensor accuracy costs and use a dynamic program to select a configuration under a latency or accuracy budget. We compare its configurations against byte-aware and sensitivity-only allocation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mukund Athmaram, Manoj Rao, Liang Ma
- 发布：2026-10-11；更新：2026-10-11
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
