---
title: "Purlin: Separating Orchestration from the Datapath of Collectives"
description: "Distributed inference depends on GPU collective communication that must keep pace with evolving hardware and specialized workloads."
---

**评分：52/100** · LLM 高效推理 > Serving 与分布式推理 > 并行与通信

[论文原文](https://arxiv.org/abs/2609.36954) · [PDF](https://arxiv.org/pdf/2609.36954)

## 一句话摘要

Distributed inference depends on GPU collective communication that must keep pace with evolving hardware and specialized workloads.

## 为什么值得关注

待编辑增强。

## 摘要原文

Distributed inference depends on GPU collective communication that must keep pace with evolving hardware and specialized workloads. However, existing collective implementations often couple semantics, orchestration (where and when data moves), and the datapath (how data moves). This coupling makes it costly to adopt new hardware mechanisms and customize communication for applications. We present Purlin, a scale-up communication framework that separates these concerns. At the top of Purlin, we specify collectives as a naming of an input and output layout and a copy or reduction operation. In the middle, we introduce a shared orchestration protocol, Stage, Notify, And Consume (SNAC), which derives coordination from these specifications. Below SNAC sits a hardware-specific datapath we call Atom, which implements two key data movement primitives for collectives: copy and reduce. This separation lets us customize collectives and adopt new hardware mechanisms while reusing orchestration via SNAC. We evaluate Purlin on A100, H200, and B200 GPUs. Across seven collectives, Purlin achieves latency speedups of up to 5.14x and bandwidth improvements of up to 4.50x over baselines. Integrated into SGLang, Purlin improves offline LLM serving throughput and interactivity by 1.13x on average and up to 1.37x over baselines. For online LLM inference, Purlin improves interactivity by 1.26x on average and up to 2.85x, with the largest gain occurring under overload. For diffusion image generation, Purlin reduces end-to-end latency by up to 1.13x.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: collective communication, distributed inference
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Osayamen Jonathan Aimuyo, Swapnil Gandhi, Christos Kozyrakis
- 发布：2026-09-29；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
