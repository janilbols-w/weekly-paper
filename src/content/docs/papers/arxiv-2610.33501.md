---
title: "DualPace: Decoupled Scheduling and Cooperative GPU--CPU Decoding for LLM Serving"
description: "Large language model (LLM) serving relies on batching to improve inference throughput, but the key-value (KV) cache grows with sequence length and limits GPU-resident concurrency."
---

**评分：47/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2610.33501) · [PDF](https://arxiv.org/pdf/2610.33501)

## 一句话摘要

Large language model (LLM) serving relies on batching to improve inference throughput, but the key-value (KV) cache grows with sequence length and limits GPU-resident concurrency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) serving relies on batching to improve inference throughput, but the key-value (KV) cache grows with sequence length and limits GPU-resident concurrency. CPU offloading can expand KV capacity using host memory, yet existing systems remain largely GPU-gated: CPU-resident requests make progress only when the GPU scheduler exposes suitable overlap opportunities. As a result, host memory and CPU compute cannot act as an independent serving resource, leading to bursty CPU-side progress and inflated tail inter-token latency (ITL) under load. We present DualPace, an LLM serving runtime that turns the host into an independently scheduled decode engine. DualPace separates scheduling authority across two engines: the GPU engine executes prefills and GPU-resident decodes, while an AMX-enabled CPU engine independently batches and advances CPU-resident decodes. The engines are decoupled in scheduling but cooperative in execution: the CPU can execute a complete decode iteration locally or selectively invoke GPU Dense Assist for dense stages, while offline profiles guide hardware-specific batching and routing. Our evaluations show that, in decode-oriented scenarios, DualPace improves serving throughput by 6.9--43.2\% over NEO, a state-of-the-art open-source CPU-offloading system, and by 11.5--90.6\% over vLLM, a widely used GPU serving system, while maintaining the same level of latency. DualPace also preserves NEO's P99 time-to-first-token (TTFT) advantage over vLLM while sustaining 7.3--50.5\% higher request rates than NEO at the same level of P99 ITL.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving, serving runtime
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：YuXuan Lin, KeQiang Wu, Kingsum Chow
- 发布：2026-10-27；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
