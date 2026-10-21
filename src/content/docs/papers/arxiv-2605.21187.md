---
title: "NVIDIA Spectrum-X: Hardware-Accelerated Multiplane Networking for Large-Scale AI Training"
description: "As distributed model training scales to span hundreds of thousands of GPUs, scale-out networks face unprecedented performance and efficiency demands."
---

**评分：42/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2605.21187) · [PDF](https://arxiv.org/pdf/2605.21187)

## 一句话摘要

As distributed model training scales to span hundreds of thousands of GPUs, scale-out networks face unprecedented performance and efficiency demands.

## 为什么值得关注

待编辑增强。

## 摘要原文

As distributed model training scales to span hundreds of thousands of GPUs, scale-out networks face unprecedented performance and efficiency demands. NVIDIA Spectrum-X Ethernet has been designed from the ground up to achieve predictable and stable network performance with high utilization and low latency. This paper presents the Spectrum-X multiplane architecture, which replaces hierarchical depth with topological parallelism, and introduces hardware-accelerated load balancing in NICs and switches as the key architectural approach to provide fast reaction to highly dynamic network conditions at the microsecond timescales that AI training workloads demand. We describe the motivation, design principles, evaluation methodology and performance on state-of-the-art benchmarks, as well as the lessons we learned from deploying and debugging Spectrum-X networks in large-scale systems. Our evaluation highlights production-grade AI infrastructure performance across four core dimensions: 98% of the theoretical line rate with low jitter-free latency; strong cross-tenant isolation for concurrent workloads; robust, capacity-proportional bisection bandwidth and 7% latency increase for 10% fabric link failures; and rapid reaction to host and fabric link flaps during LLM training workloads.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: load balancing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sajy Khashab, Albert Gran Alcoz, Alon Gal, Jacky Romano, Rani Abboud, Yonatan Piasetzky, Lior Maman, Amit Nishry, Barak Gafni, Omer Shabtai, Matty Kadosh, Dror Goldenberg, Gilad Shainer, Mark Silberstein
- 发布：2026-10-21；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
