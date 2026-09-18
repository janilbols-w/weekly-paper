---
title: "PixelFlow: Token-Level Workload Management for Efficient Distributed DiT Serving"
description: "Online image generation with Diffusion Transformers (DiTs) must meet latency service-level objectives (SLOs) while using GPU resources efficiently."
---

**评分：43/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2609.20723) · [PDF](https://arxiv.org/pdf/2609.20723)

## 一句话摘要

Online image generation with Diffusion Transformers (DiTs) must meet latency service-level objectives (SLOs) while using GPU resources efficiently.

## 为什么值得关注

待编辑增强。

## 摘要原文

Online image generation with Diffusion Transformers (DiTs) must meet latency service-level objectives (SLOs) while using GPU resources efficiently. Existing systems improve GPU utilization by batching multiple requests for joint execution. However, request-level batching offers limited control over batch size: batches may be too small to saturate GPU compute, while larger ones may violate latency SLOs. Globally coordinated scheduling introduces further delays by requiring independently progressing GPUs to synchronize before admitting new work. We present PixelFlow, a distributed DiT serving system that addresses these limitations through token-level workload management. Its key idea is to use image tokens (the units a DiT processes to generate an image) to divide and batch request workloads at a finer granularity. This allows each GPU to take on a portion of additional work under latency constraints. By distributing these portions across GPUs, PixelFlow accommodates more concurrent requests, improving GPU utilization while reducing queueing delays. To realize this flexibility, PixelFlow provides a runtime that splits requests into variable-sized partitions and batches them efficiently on each GPU. To reduce the resulting communication overhead, it optimizes token placement to limit cross-GPU data exchange while balancing GPU workloads. It further exploits similarity across denoising steps to overlap the remaining transfers with computation. An SLO-aware scheduler groups GPUs to share compute resources among requests with compatible latency requirements. Each group progresses independently, synchronizing with others only when their combined resources are needed to admit a new request. Evaluation with Stable Diffusion 3 and FLUX.1-dev on H100 GPUs shows that PixelFlow improves SLO attainment by up to 43% and achieves up to 2.8 times the goodput of state-of-the-art DiT serving systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: slo
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zhexiang Zhang, Minchen Yu, Yifan Sun, Xu Bai, Xingliang Yuan, Adel N. Toosi
- 发布：2026-09-17；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
