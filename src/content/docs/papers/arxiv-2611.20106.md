---
title: "Making Preemption Productive in Long-Output LLM Serving"
description: "Reasoning LLMs generate long outputs whose key--value (KV) caches occupy GPU memory for minutes."
---

**评分：43/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.20106) · [PDF](https://arxiv.org/pdf/2611.20106)

## 一句话摘要

Reasoning LLMs generate long outputs whose key--value (KV) caches occupy GPU memory for minutes.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reasoning LLMs generate long outputs whose key--value (KV) caches occupy GPU memory for minutes. When memory fills, the server preempts requests, and a preempted request can repeatedly lose and recover its state while producing little new output. We call this behavior KV thrashing. In certain cases, existing systems leave more than a fifth of requests stalled for over a minute. Because preemption cannot be avoided without delaying admission, we ask how to make it productive. We present Stint, a serving system that preserves a preempted request's work, bounds how long it waits, and gives it fresh output after it returns. Stint stores fixed-length KV snapshots in a contiguity-first CPU pool with an exact-extent allocator, and moves them with fused K/V gather/scatter kernels and double buffering. Age-based readmission brings stalled requests back, and protection gives them a turn of fresh decoding before another preemption. Remaining-length estimates from decoding hidden states guide victim selection. On olympiad-math replays with Qwen3-32B on H200 GPUs, no request pauses for more than 50 seconds under Stint and p99 time per output token falls by 50.7\% relative to recomputation in the same engine. The replay as a whole finishes 10.7\% sooner (12.0\% higher throughput), because the requests that baselines starve no longer finish last.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ziji Shi, Xinyi Wan, Chaoyi Ruan, Guangxing Huang, Min Lin, Jialin Li
- 发布：2026-11-15；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
