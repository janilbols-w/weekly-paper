---
title: "Speculation at a Distance: Where Edge-Cloud Speculative Decoding Actually Pays Off"
description: "Speculative decoding (SD) accelerates LLM inference by $1.5$-$3$ times when the draft and target models are co-located."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2606.25091) · [PDF](https://arxiv.org/pdf/2606.25091)

## 一句话摘要

Speculative decoding (SD) accelerates LLM inference by $1.5$-$3$ times when the draft and target models are co-located.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding (SD) accelerates LLM inference by $1.5$-$3$ times when the draft and target models are co-located. This has motivated a distributed variant (DSD) that places the draft model on an edge device while the target stays in the cloud. We show with closed-form inequalities that DSD's per-request latency benefit is limited under WAN edge-cloud communication. If the server can host both models, co-located SD has lower latency and communication than synchronous DSD, with the same per-output FLOPs and model-weight memory. Pipelining can make DSD competitive with co-located SD only in low-RTT regimes where the round trip is shorter than the edge drafting time window; at WAN RTTs, the cloud round trip remains too large for pipelined DSD to beat co-located SD. Against cloud autoregressive decoding, DSD can reduce latency only inside a bounded window given the target-model speed, acceptance rate, and RTT. DSD is also infeasible against closed-source APIs without a verifier-only interface. The main case for DSD appears in multi-tenant capacity. Under cross-client overlap, offloading draft compute lets a saturated cloud server sustain $(1 + \gamma\,t_d/t_v)$ times more concurrent clients at the same per-client rate, where $\gamma$ is the speculation length and $t_d, t_v$ are the per-step draft and verification times. DSD should therefore be evaluated primarily by multi-tenant capacity and server throughput, not only by single-request latency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuan Lyu, Bharath Irukulapati, Jaya Prakash Champati
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
