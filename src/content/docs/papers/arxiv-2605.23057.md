---
title: "RequestRouter: Request-Boundary Routing for Efficient Single-GPU LLM Inference"
description: "RequestRouter is a lightweight request-boundary controller for reducing the latency and energy cost of single-GPU large language model inference."
---

**评分：53/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2605.23057) · [PDF](https://arxiv.org/pdf/2605.23057)

## 一句话摘要

RequestRouter is a lightweight request-boundary controller for reducing the latency and energy cost of single-GPU large language model inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

RequestRouter is a lightweight request-boundary controller for reducing the latency and energy cost of single-GPU large language model inference. Rather than serving all requests with one static configuration, the system uses cheap request-level features to select one fixed inference mode per request, including FP16, quantized inference, speculative decoding, prefix caching, continuous batching, and hybrid modes such as GPTQ plus prefix caching and INT8 plus continuous batching. We evaluate RequestRouter using an 8B instruction-tuned language model served through vLLM on NVIDIA A100 GPUs. Across the full-scale A100 evaluation--26,500 fixed-mode evaluations followed by 3,500 online-controller evaluations, for 30,000 measured inference executions in total--the controller achieves a 2.10x mean latency speedup over FP16 and a 0.48x energy ratio on deployment-style workloads. A smaller matched evaluation with repeated measurements provides a controlled statistical check of this result: RequestRouter retains a 1.93x latency speedup (95% CI: 1.88--1.98x) and a 0.523 energy ratio (95% CI: 0.506--0.540), showing that the gains persist under a more tightly controlled protocol. On a separate expanded automatic benchmark evaluation, the routed policy retains 99.6% of FP16 macro accuracy. A 100,000-call CPU microbenchmark measures only 0.00475 ms mean routing overhead (0.00532 ms p99). Thus, simple request-aware routing can recover substantial serving efficiency without retraining or modifying the underlying LLM.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Aman Sunesh, Ali Alshehhi, Hivansh Dhakne
- 发布：2026-08-21；更新：2026-08-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
