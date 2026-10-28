---
title: "Request-Adaptive Execution for Efficient Hybrid LLM Inference"
description: "Hybrid large language models (LLMs) have emerged as a promising way to combine the modeling capability of the Attention mechanism with the efficiency of state space models (SSMs)."
---

**评分：49/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2610.37432) · [PDF](https://arxiv.org/pdf/2610.37432)

## 一句话摘要

Hybrid large language models (LLMs) have emerged as a promising way to combine the modeling capability of the Attention mechanism with the efficiency of state space models (SSMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Hybrid large language models (LLMs) have emerged as a promising way to combine the modeling capability of the Attention mechanism with the efficiency of state space models (SSMs). However, most existing hybrid LLMs still inherit a static design philosophy: once the Attention-to-SSM layout is chosen, every request must follow the same hybrid execution. This one-layout-fits-all design is inefficient for real-world serving workloads, where different requests rely on contextual information in different ways. This paper presents Morph, a serving system that co-designs the model architecture and runtime for request-adaptive hybrid LLM inference. Its model architecture pairs Attention and SSM layers within each block and uses prefill-oriented gating to select a request-specific layout that remains fixed throughout decoding. Its serving runtime preserves batching efficiency under divergent layer choices through selective batching and enables correct prefix reuse through hybrid-aware context caching. Experiments on six datasets show that Morph achieves a better quality-efficiency trade-off than existing static hybrid baselines. System-level evaluation further shows that Morph improves the serving throughput by up to 3.87x over baselines while substantially reducing inference latency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 15 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: serving runtime
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Fahao Chen, Xuzhe Yan, Qi Zhang, Peng Li, Dongxiao Yu, Song Guo
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
