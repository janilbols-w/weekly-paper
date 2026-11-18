---
title: "SpecRelay: Amortize or Avoid the Round Trip in Edge-Cloud Speculative Decoding"
description: "Edge-cloud speculative decoding moves autoregressive drafting to an edge device while a larger cloud model verifies draft tokens in parallel, so that edge drafting and cloud verification overlap under a synchronous draft-verify schedule."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2611.18963) · [PDF](https://arxiv.org/pdf/2611.18963)

## 一句话摘要

Edge-cloud speculative decoding moves autoregressive drafting to an edge device while a larger cloud model verifies draft tokens in parallel, so that edge drafting and cloud verification overlap under a synchronous draft-verify schedule.

## 为什么值得关注

待编辑增强。

## 摘要原文

Edge-cloud speculative decoding moves autoregressive drafting to an edge device while a larger cloud model verifies draft tokens in parallel, so that edge drafting and cloud verification overlap under a synchronous draft-verify schedule. Beyond low-latency local networks, however, the next verification request of that schedule can be sent only after the previous reply arrives, so every round still waits out a full round trip, and throughput falls as the network RTT grows. To recover this loss, we present SpecRelay, an edge-cloud LLM inference system that addresses this cost at two levels: it amortizes round trips when cloud verification is necessary and avoids them when local reasoning suffices. For cloud-bound queries, an asynchronous verification pipeline keeps fixed-budget draft trees in flight while earlier replies are still outstanding, and the cloud rejects stale requests before the target-model forward pass (the asynchronous schedule). At the query level, an RTT-conditioned router (the Latency-Aware Router) estimates quality and completion latency for three on-device modes (direct generation, Chain-of-Draft, and full reasoning) and cloud speculative decoding, selecting among them under a configurable accuracy-latency objective without adding latency during inference, since the router runs concurrently with the draft-model prefill. The asynchronous schedule alone improves decoding throughput by up to 50% over a reproduced synchronous baseline across multiple benchmarks. At matched target-model accuracy and 250 ms of added round-trip latency, the full system with the router delivers 1.95x and 1.55x the throughput of the same baseline on SPROUT and OlympiadBench, respectively, while sending only 47% and 39% of the queries to the cloud.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jai Jain, Chihyo Ahn, Yong Liu, Charles Chen, Duc N. M Hoang, Ajay Kumar Jaiswal, Fatih Ilhan, Han-Byul Kim, Lauren Hannah, Richa Dixit, Minsik Cho, Yingyan Celine Lin, Hyesoon Kim
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
