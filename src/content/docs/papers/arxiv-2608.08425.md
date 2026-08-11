---
title: "PSP: Low-Overhead Packet-Level Load Balancing for Stale-State and Bandwidth-Asymmetric Networks"
description: "With the rapid growth of large language model training and generative artificial intelligence services, data center networks face severe micro-burst traffic and high concurrency."
---

**评分：44/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2608.08425) · [PDF](https://arxiv.org/pdf/2608.08425)

## 一句话摘要

With the rapid growth of large language model training and generative artificial intelligence services, data center networks face severe micro-burst traffic and high concurrency.

## 为什么值得关注

待编辑增强。

## 摘要原文

With the rapid growth of large language model training and generative artificial intelligence services, data center networks face severe micro-burst traffic and high concurrency. Traditional hash-based flow-level load balancing cannot sense link states, leading to hash collisions, hotspot congestion, and tail latency in multipath Clos networks. Existing packet-level schemes are constrained by stale state information, high hardware complexity, and poor adaptation to heterogeneous links. To address these issues, this paper proposes probabilistic state-proportional (PSP) dispatching, a packet-level load balancing algorithm. Using a Band-based discrete state representation, PSP replaces global sorting with local probability mapping, reducing hardware complexity while suppressing herding and oscillations caused by stale states. Experiments on a cycle-accurate simulator show that PSP is robust across port scales, bandwidth-limited paths, and fixed-flow interference. It outperforms join-the-shortest-queue (JSQ) scheduling and Random in loss rate, 99th-percentile buffer occupancy, and scalability, while remaining competitive with Top-k at lower hardware cost. PSP provides an effective balance among performance, stability, and overhead for artificial intelligence data centers.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: load balancing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiaqi Liu, Chunyang Zhang, Heng Pan, Yanbiao Li
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
