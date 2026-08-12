---
title: "Astrolabe: Balancing Load in LLM Serving with Randomized Prediction-Guided Scheduling"
description: "This paper presents Astrolabe, a randomized prediction-guided scheduler for one-shot request dispatch in multi-instance large language model (LLM) serving."
---

**评分：46/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2508.03611) · [PDF](https://arxiv.org/pdf/2508.03611)

## 一句话摘要

This paper presents Astrolabe, a randomized prediction-guided scheduler for one-shot request dispatch in multi-instance large language model (LLM) serving.

## 为什么值得关注

待编辑增强。

## 摘要原文

This paper presents Astrolabe, a randomized prediction-guided scheduler for one-shot request dispatch in multi-instance large language model (LLM) serving. Astrolabe improves load balancing without relying on migration-based rebalancing, whose KV-cache transfers can introduce substantial overhead and network contention under high load. It combines response-length estimation, per-instance simulation-based latency prediction, and a power-of-two-choices dispatch policy to balance load while avoiding request herding. On the default Llama-2-7B/ShareGPT setup, Astrolabe matches the SLO capacity of the best load-aware baseline (31.6 versus 31.5 QPS), while reducing mean time-to-first-token (TTFT) by 8 to 36 percent, P99 TTFT by 16 to 77 percent, and mean end-to-end (E2E) latency by up to 5.6 percent, with approximately six times fewer preemptions once capacity is reached. Under configuration shifts, Astrolabe improves SLO capacity by up to 6 percent on Qwen2-7B and 7.1 percent under tight batching, reduces mean E2E latency by 6 to 9 percent under bursty arrivals, and achieves an approximately 2.8-fold reduction in per-predictor CPU usage relative to full fanout. With migration enabled on A100 GPUs, Astrolabe outperforms Llumnix by up to 2.6 times in throughput while achieving orders-of-magnitude lower per-token latency at saturation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Wei Da, Evangelia Kalyvianaki
- 发布：2026-08-12；更新：2026-08-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
