---
title: "Lachesis: Lifetime-Aware KV Cache Placement for Agent Serving across HBM and High-Bandwidth Flash"
description: "Large language model (LLM) serving is increasingly dominated by agentic workloads, in which agents and their sub-agents accumulate context as KV cache across many requests, consuming substantial memory."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.08378) · [PDF](https://arxiv.org/pdf/2610.08378)

## 一句话摘要

Large language model (LLM) serving is increasingly dominated by agentic workloads, in which agents and their sub-agents accumulate context as KV cache across many requests, consuming substantial memory.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) serving is increasingly dominated by agentic workloads, in which agents and their sub-agents accumulate context as KV cache across many requests, consuming substantial memory. High-bandwidth flash (HBF) is a promising solution, providing an order of magnitude greater capacity at HBM-class read bandwidth, but its finite write endurance is the key limiting factor. Our key insight is that KV cache should be placed across HBM and HBF by its lifetime. Placing shorter-lived data in HBM lets HBM absorb more of an agent run's writes and sends less of them to HBF. As the lifetime of KV cache in agentic serving is dictated by the harness, the program that orchestrates the agents, we analyze its behavior and identify three axes along which lifetime diverges, temporal, structural, and inter-worker. Guided by these observations, we present Lachesis, a lifetime-aware KV cache placement layer between the agent harness and the serving engine. At write time, it places each segment in HBM or HBF according to its lifetime, and frees its blocks once the segment is no longer read. In trace-driven simulation, Lachesis extends HBF lifetime by 1.19-3.13x over HBM-first placement, reaching 3.3-12.2 device-years. Even under continuous 24x7 operation at the full load a tight SLO admits, HBF outlasts its five-year warranty on the multi-agent trace.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jaehoon Yang, Jeongmin Lee, Haneul Park, Seung Yul Lee, Nam Sung Kim, Jae W. Lee
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
