---
title: "Flide: Accelerating Decision Inference with Exact State Forking"
description: "Decision models such as Jev have emerged as a highly promising paradigm for LLM agent systems, providing lightweight and reliable categorical reasoning for rapid System One execution."
---

**评分：46/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2610.42148) · [PDF](https://arxiv.org/pdf/2610.42148)

## 一句话摘要

Decision models such as Jev have emerged as a highly promising paradigm for LLM agent systems, providing lightweight and reliable categorical reasoning for rapid System One execution.

## 为什么值得关注

待编辑增强。

## 摘要原文

Decision models such as Jev have emerged as a highly promising paradigm for LLM agent systems, providing lightweight and reliable categorical reasoning for rapid System One execution. However, existing generation-oriented inference engines fail to support these workloads effectively, suffering from severe prefix recomputation overheads or distorted output probabilities. To address this challenge, we propose Flide, an efficient and exact inference engine that decouples the logical tree structure of a decision request from its physical execution within a single flattened token stream. Through ForkAttention, Flide navigates request dependencies using GPU-resident indices across both standard attention and recurrent Gated DeltaNet layers, guaranteeing in exact arithmetic that every query branch evaluates identically to an isolated forward pass. By expressing branch topologies directly in GPU-resident metadata, Flide accommodates diverse request mixtures with a compact set of pre-recorded execution graphs while enabling expanding agent histories to resume from checkpoints saved in earlier passes. Extensive evaluations on public hybrid and decision models demonstrate that Flide answers queries up to 9.5 times faster than vLLM and SGLang while staying closest to a float32 reference in total variation distance. By unifying physical execution throughput with mathematical exactness, Flide establishes a principled foundation for scalable, latency-critical decision intelligence in agent systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: inference engine
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Bobo Li, Jiajia Song, Hao Fei, Wynne Hsu, Mong Li Lee
- 发布：2026-11-02；更新：2026-11-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
