---
title: "LLMVisor: A Real-Time Latency Attribution Model for Multi-Tenant LLM Serving"
description: "提出面向多租户 LLM 服务的实时请求级延迟归因模型 LLMVisor，以 Roofline 分析刻画 Prefill 与 Decode 的访存和计算阶段，并把批次延迟分解为可加的单请求份额。"
---

**评分：53/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2608.08382) · [PDF](https://arxiv.org/pdf/2608.08382)

## 一句话摘要

提出面向多租户 LLM 服务的实时请求级延迟归因模型 LLMVisor，以 Roofline 分析刻画 Prefill 与 Decode 的访存和计算阶段，并把批次延迟分解为可加的单请求份额。

## 为什么值得关注

细粒度共享需要低开销、可解释的请求级计量才能进入调度闭环；该模型以微秒级开销运行，并在两类模型和 A100/H100 实验中比 token 数基线更准确地归因尾部延迟。

## 摘要原文

As LLM inference shifts to multi-tenant GPU clusters, co-batching improves throughput but obscures per-tenant usage and limits control. Enabling fractional sharing of the inference engine requires a real-time, per-request attribution primitive that is accurate and light enough to run inside the scheduling loop. We present LLMVisor, a roofline-guided latency attribution model that captures the memory-bound and compute-bound phases via a concise piecewise-linear form over features proportional to FLOPs and memory I/O traffic. LLMVisor decomposes batch latency into additive, per-request shares and runs efficiently at microsecond scale. We evaluate LLMVisor across Llama 3.1-8B and Qwen 2.5-14B/32B on A100/H100 GPUs under varying tensor parallelism and workload mixes. Compared to a token-count baseline, LLMVisor attains near-perfect R-squared and reduces relative error by up to 2.5x and 3.3x at p90 and p99, respectively, for prefill, and by up to 3.5x and 4.4x for decode, despite batching variability and sequence divergence.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: inference engine, llm serving
- quantitative claim detected
- no code link detected in metadata
- 限制：实验仅覆盖两类模型、A100/H100 和给定并行配置；摘要尚未证明更准确的归因会直接改善端到端吞吐、SLO 隔离或多租户公平性。

## 元数据

- 作者：Shuowei Jin, Xueshen Liu, Jiaxin Shan, Le Xu, Tieying Zhang, Liguang Xie, Z. Morley Mao
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：abstract
