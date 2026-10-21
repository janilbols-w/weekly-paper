---
title: "Service-Induced Congestion in Memory-Constrained LLM Serving"
description: "In large language model (LLM) serving, each request accumulates persistent graphics processing unit (GPU) memory during service as its key-value cache grows with every generated token."
---

**评分：42/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2606.15555) · [PDF](https://arxiv.org/pdf/2606.15555)

## 一句话摘要

In large language model (LLM) serving, each request accumulates persistent graphics processing unit (GPU) memory during service as its key-value cache grows with every generated token.

## 为什么值得关注

待编辑增强。

## 摘要原文

In large language model (LLM) serving, each request accumulates persistent graphics processing unit (GPU) memory during service as its key-value cache grows with every generated token. Under high concurrency, aggregate memory usage therefore increases endogenously over time: the service process itself creates future capacity pressure. When memory capacity is exceeded, systems evict active requests, discarding cached state and restarting them later, which wastes computation and reduces throughput. We develop a discrete-time dynamical model of memory-constrained LLM inference that captures admission, memory growth, and eviction under continuous batching. In the saturated-input regime, the system admits both eviction-free fixed points and limit cycles with evictions. For homogeneous workloads, we show that the eviction-free equilibrium is unstable and that, except for a Lebesgue-measure-zero exact-capture set, the system converges to a unique worst-case limit cycle that is asymptotically stable outside this exceptional set, with throughput losses as large as 50%. For heterogeneous workloads, we prove a stability criterion in the two-class common-input setting and explain how the survival-polynomial mechanism generalizes to multiple classes and heterogeneous-input lengths. Under an input-dominated scaling regime, coprime decoding lengths stabilize the eviction-free equilibrium, while non-coprime lengths create synchronized modes that drive instability. These results characterize when workload heterogeneity desynchronizes completions and helps stabilize memory-constrained serving. More broadly, we identify service-induced congestion as a structural instability mechanism and derive scheduling design principles for sustaining high throughput.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ruicheng Ao, Jing Dong, Gan Luo, David Simchi-Levi
- 发布：2026-10-20；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
