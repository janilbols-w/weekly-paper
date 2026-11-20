---
title: "Harvesting Expert-Parallel Bubbles for Fine-Tuning"
description: "GPUs are expensive, yet latency-critical large language model (LLM) inference leaves part of them idle."
---

**评分：41/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2611.24496) · [PDF](https://arxiv.org/pdf/2611.24496)

## 一句话摘要

GPUs are expensive, yet latency-critical large language model (LLM) inference leaves part of them idle.

## 为什么值得关注

待编辑增强。

## 摘要原文

GPUs are expensive, yet latency-critical large language model (LLM) inference leaves part of them idle. Colocation reclaims this capacity by running best-effort work, such as fine-tuning, alongside serving. Many leading LLMs now use a Mixture-of-Experts (MoE) architecture, which adds a new source of idle time. Under expert parallelism, MoE experts are spread across GPUs, and because the router sends uneven numbers of tokens to each GPU, lightly loaded GPUs wait for the most loaded one. Even after applying load balancing solutions, such bubbles still take 8--13% of prefill time. We present BubbleTea, the first colocation system that leverages expert-parallel bubbles for fine-tuning. Unlike existing colocation systems, which make one scheduling decision for all GPUs per forward pass, BubbleTea predicts each GPU's bubble at every layer from the router's token assignment, and fills it with short chunks of fine-tuning work that reuse the weights already loaded for serving. We also introduce compiler passes that automatically derive these chunks from the served LLM as-is, without porting each model architecture to a separate training engine. Our evaluation on three MoE models, served on four A100 GPUs, shows that fine-tuning throughput with BubbleTea is 1.9--6.2$\times$ faster than with LLMStation, a state-of-the-art colocation system. BubbleTea keeps p90 inference latency within 10% of serving alone in 50 of 63 workloads, compared to 44 for LLMStation. On bursty production traces, BubbleTea trains 3.3$\times$ faster than LLMStation and 14$\times$ faster than a stock trainer colocated under CUDA MPS, with p90 inference latency staying within 7% of serving alone.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: load balancing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Oana Balmau, Saurav Banka, Jiaxuan Chen, Anne-Marie Kermarrec, Ramya Narasimha Prabhu, Rafael Pires, Mathis Randl, Martijn de Vos
- 发布：2026-11-18；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
