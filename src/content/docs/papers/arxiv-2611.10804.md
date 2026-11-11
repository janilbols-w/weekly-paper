---
title: "DICOMPUTE: An Economic and Privacy-Aware Framework for Distributed Artificial Intelligence Inference"
description: "The prevailing design of large-scale artificial intelligence inference concentrates accelerators, model weights, and request processing in centralized computing facilities."
---

**评分：52/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2611.10804) · [PDF](https://arxiv.org/pdf/2611.10804)

## 一句话摘要

The prevailing design of large-scale artificial intelligence inference concentrates accelerators, model weights, and request processing in centralized computing facilities.

## 为什么值得关注

待编辑增强。

## 摘要原文

The prevailing design of large-scale artificial intelligence inference concentrates accelerators, model weights, and request processing in centralized computing facilities. Centralization offers important benefits in accelerator utilization, high-bandwidth interconnects, operational control, and serving efficiency. Yet centralized infrastructure is not always the least-cost or most governance-compatible choice for every inference workload. This paper develops a research framework for DICOMPUTE, a heterogeneous distributed inference architecture in which policy-constrained scheduling can allocate suitable requests across privately controlled, regional, and independently operated computing resources. We derive a full-cost comparison that accounts for capital amortization, energy, network transfer, orchestration, utilization, failures, and trust-related expenses; characterize conditions under which distributed inference can outperform centralized alternatives; and specify a privacy model separating data residency, transport confidentiality, execution confidentiality, and verifiable accounting. We propose falsifiable hypotheses and a reproducible experimental design, without presenting simulated examples as measured performance. Our central conclusion is conditional: distributed inference is most promising for divisible, latency-tolerant or locality-sensitive workloads on underutilized compatible hardware, while centralized clusters retain structural advantages for tightly coupled, memory-intensive, high-throughput inference. The framework is intended to support rigorous evaluation rather than to assert universal superiority.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 17 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Atul Khekade, Ritesh Kakkad, Anil Chinchawale, Omkar Mestry, Behnam Mohammadkhani
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
