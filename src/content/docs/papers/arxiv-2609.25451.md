---
title: "Fast Recovery for LLM Serving via Decoupled Device Memory Lifetime in Dynamo"
description: "Large language model (LLM) inference replicas run across tightly coupled GPUs and serve traffic continuously for weeks."
---

**评分：49/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.25451) · [PDF](https://arxiv.org/pdf/2609.25451)

## 一句话摘要

Large language model (LLM) inference replicas run across tightly coupled GPUs and serve traffic continuously for weeks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) inference replicas run across tightly coupled GPUs and serve traffic continuously for weeks. Hardware and software failures are therefore inevitable, and one worker failure can disrupt an entire replica. Recovery requires reinitializing the engine, taking minutes even when weights and compilation artifacts are cached. Production deployments overprovision serving capacity to mask this window. We argue that the dominant cost is loss of ready serving capacity, not request progress, so recovery should preserve initialized engine state rather than reconstruct it. We present fast recovery for Dynamo based on this principle. Snapshots capture an initialized engine once and restore it instead of reinitializing it. Analysis of 18 weeks of failures from the Dynamo cluster shows that most failures are device-preserving: the engine process fails while the GPU and its resident allocations remain intact. Our key insight is that independent engine processes can reuse the same GPU-resident state while keeping mutable execution state private. The GPU Memory Service (GMS) decouples device-memory ownership from engine processes, enabling engines to share and reattach surviving allocations without copying them. GMS preserves model weights and shares them read-only between replacement and Shadow Engines, avoiding weight reloads. A second initialized runtime on the same GPUs reduces recovery to promotion. Across four models on vLLM and SGLang, these mechanisms recover a failed replica in under 7 seconds, 13-29 times faster than a warm restart, using a fixed 4-8 GiB of device memory per GPU independent of model size. Replaying the production trace, we estimate they would reclaim 79% of GPU-hours lost to recovery.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Schwinn Saereesitthipitak, Mohammed Abdulwahhab, Hannah Zhang, Dan Feigin, Neelay Shah, Maksim Khadkevich, Itay Neeman, Vikram Sharma Mailthody, Wen-mei W. Hwu
- 发布：2026-09-21；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/ai-dynamo/dynamo](https://github.com/ai-dynamo/dynamo)
- 阅读深度：metadata
