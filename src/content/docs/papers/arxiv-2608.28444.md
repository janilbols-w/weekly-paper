---
title: "Sliding-window beats linear attention"
description: "Due to the nature of quadratic attention, Large Language Models (LLMs) consume a lot of memory and energy: every new token costs more than the previous one, and its keys and values must be stored in memory indefinitely, which is unsustainable."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.28444) · [PDF](https://arxiv.org/pdf/2608.28444)

## 一句话摘要

Due to the nature of quadratic attention, Large Language Models (LLMs) consume a lot of memory and energy: every new token costs more than the previous one, and its keys and values must be stored in memory indefinitely, which is unsustainable.

## 为什么值得关注

待编辑增强。

## 摘要原文

Due to the nature of quadratic attention, Large Language Models (LLMs) consume a lot of memory and energy: every new token costs more than the previous one, and its keys and values must be stored in memory indefinitely, which is unsustainable. Two main lines of work address this: compressing the KV cache, e.g., by evicting or quantizing keys and values, and retrofitting LLMs to use Linear Attention, which replaces the KV cache with a fixed-size state. Retrofitting has attracted a lot of attention, given its promise to solve the quadratic scaling problem with state-of-the-art performance at low cost. However, it has not been properly compared to the simplest form of KV-cache eviction: Sliding Window Attention (SWA) with attention sinks. In this work, we show that SWA with sinks performs as well or better than most retrofitted Linear Attention models across multiple LLMs and downstream tasks, with the largest gains on long-context and generative tasks. On long-context reasoning tasks (Needle-in-a-Haystack and BABILong), SWA achieves massively higher performance (2 to 10 times higher than linear attention). SWA requires no additional training, is extremely fast, and requires little memory, making it an extremely cheap and reliable solution. When the training budget is limited, switching to SWA is a much more effective way to reduce inference memory cost than retrofitting linear attention. Linear attention models have shown promise, but they require training from scratch or extensive retrofitting to reap their architectural benefits and come close to SWA.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Alexia Jolicoeur-Martineau, Rhea Sanjay Sukthanker, Pashmina Cameron, Emy Gervais
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
