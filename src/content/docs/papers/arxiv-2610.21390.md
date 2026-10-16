---
title: "PriorityFEC: Deadline-Aware Streaming FEC for KV-Cache Handoff in Edge Multi-Agent Systems"
description: "Multi-agent large language model (LLM) systems are increasingly deployed at the edge to support complex tasks that require collaboration and information exchange among multiple agents."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.21390) · [PDF](https://arxiv.org/pdf/2610.21390)

## 一句话摘要

Multi-agent large language model (LLM) systems are increasingly deployed at the edge to support complex tasks that require collaboration and information exchange among multiple agents.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multi-agent large language model (LLM) systems are increasingly deployed at the edge to support complex tasks that require collaboration and information exchange among multiple agents. However, when task contexts are passed across agents, shared context that has already been processed by upstream agents often needs to be prefilled again, resulting in substantial redundant computation. Reusing an already prefilled key--value (KV) cache can avoid this recomputation, but requires the reusable KV state to be transferred across the network before the receiving agent can begin generation. Under strict time-to-first-token (TTFT) deadlines and unreliable edge links, delivering the complete KV cache may be infeasible, making it necessary to prioritize and protect the most valuable KV information within a limited transmission budget. This paper proposes PriorityFEC, a utility-aware KV-cache handoff scheme that jointly exploits model-side KV importance and transport-side reliability. PriorityFEC first constructs a utility-aware source stream by placing high-utility KV blocks at earlier transmission positions. It then protects the ordered stream using a feedback-adaptive Streaming Forward Erasure Correction (FEC) mechanism, which schedules repair packets according to receiver feedback before the TTFT deadline. We implement PriorityFEC on a distributed edge LLM serving prototype and evaluate it with Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct across multiple datasets. Results show that PriorityFEC achieves superior task quality over the compared transport schemes, with its advantages becoming particularly pronounced under stringent deadline constraints. These results demonstrate the importance of jointly optimizing KV-cache utility and deadline-aware transport reliability when reusable LLM state must be handed off across unreliable edge networks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Han Shen, Qifu Tyler Sun, Fanyang Meng, Ye Wang, Yongsheng Liang
- 发布：2026-10-15；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
