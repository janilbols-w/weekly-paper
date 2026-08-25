---
title: "When Less Latent Leads to Better Relay: Information-Preserving Compression for Latent Multi-Agent LLM Collaboration"
description: "Multi-agent LLM systems are moving beyond discrete-token messages toward richer relays that preserve internal state."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2604.13349) · [PDF](https://arxiv.org/pdf/2604.13349)

## 一句话摘要

Multi-agent LLM systems are moving beyond discrete-token messages toward richer relays that preserve internal state.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multi-agent LLM systems are moving beyond discrete-token messages toward richer relays that preserve internal state. Recent work such as LatentMAS transmits full key-value (KV) caches between agents but pays a high memory and communication cost. We adapt KV-cache eviction to this setting and introduce \textbf{Orthogonal BackFill (OBF)}, which injects a low-rank residual from the discarded KV states back into the retained ones, orthogonal to what is already kept. With only $9.9\%$-$20.2\%$ of the prompt KV retained, compressed relay cuts bandwidth by $4.7\times$ and GPU memory by $8\%$ at under $5\%$ wall-clock overhead, and stays close to full relay in accuracy across nine benchmarks, ahead of it on several. OBF matches or improves over headwise eviction on all nine, and its gain is proportional to the accuracy gap eviction opens against full relay ($r{=}0.78$ across three model scales), so it gives back part of what eviction takes. Code is available at https://github.com/markli404/When-Less-Latent-Leads-to-Better-Relay.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yiping Li, Zhiyu An, Wan Du
- 发布：2026-08-25；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/markli404/When-Less-Latent-Leads-to-Better-Relay](https://github.com/markli404/When-Less-Latent-Leads-to-Better-Relay)
- 阅读深度：metadata
