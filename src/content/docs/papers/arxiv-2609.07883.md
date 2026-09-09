---
title: "Deadline-Aware Adaptive Prefill Chunking for Efficient Large Language Model Serving"
description: "Continuous batching improves large language model (LLM) serving throughput, but long prompt prefills can delay decode iterations and violate inter-token latency objectives."
---

**评分：50/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.07883) · [PDF](https://arxiv.org/pdf/2609.07883)

## 一句话摘要

Continuous batching improves large language model (LLM) serving throughput, but long prompt prefills can delay decode iterations and violate inter-token latency objectives.

## 为什么值得关注

待编辑增强。

## 摘要原文

Continuous batching improves large language model (LLM) serving throughput, but long prompt prefills can delay decode iterations and violate inter-token latency objectives. Chunked prefill mitigates this interference, yet its chunk size is normally fixed: small chunks protect decode latency but repeatedly pay launch overhead, while large chunks improve prefill efficiency but create latency spikes. We introduce SLOWeave, an online scheduling method that selects the largest prefill chunk predicted to finish before the earliest active decode deadline. The decision requires no workload-specific chunk-size tuning and is computed by a logarithmic-time search over a monotone iteration-cost model. We prove that, whenever a decode-only iteration is feasible and the cost predictor is accurate, SLOWeave maximizes immediate prefill progress among decisions that preserve every active request's next-token deadline. We evaluate the method in a reproducible event-driven simulator and an iteration-level GPU runtime across chat, mixed-context, long-context, and bursty workloads. Under a 25ms time-per-output-token objective, SLOWeave improves goodput over the strongest fixed-chunk baseline by 39% on mixed requests and 38% on long-context requests. Under a stricter 10ms objective, the gains rise to 3.3$\times$ and 2.4$\times$, respectively. These results isolate adaptive chunk sizing as a useful serving primitive and provide an implementation-ready controller for integration with iteration-level LLM runtimes.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: model serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Siyu Song, Qi Bai, Jinbo Hao, Kai Li, Chenchen Wang, Jiayu Sun
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
