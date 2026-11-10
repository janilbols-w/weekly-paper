---
title: "PriorityFEC: Deadline-Aware Streaming FEC for KV-Cache Handoff in Edge Multi-Agent Systems"
description: "Collaborative edge large language model (LLM) systems often require repeated prefill computation when task contexts are transferred between agents."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.21390) · [PDF](https://arxiv.org/pdf/2610.21390)

## 一句话摘要

Collaborative edge large language model (LLM) systems often require repeated prefill computation when task contexts are transferred between agents.

## 为什么值得关注

待编辑增强。

## 摘要原文

Collaborative edge large language model (LLM) systems often require repeated prefill computation when task contexts are transferred between agents. Reusing previously computed key--value (KV) caches can eliminate this overhead, but requires KV-cache delivery before the receiving agent begins decoding. Under strict deadlines and unreliable edge links, complete KV cache transfer may be infeasible, making the timely delivery of useful KV information critical. This paper proposes PriorityFEC, a utility-aware KV-cache handoff scheme that combines prioritized source transmission with adaptive loss recovery. PriorityFEC first organizes KV blocks into a utility-aware source queue to prioritize important information. It then employs ACK-sliding Streaming FEC and a lightweight Double Deep Q-Network (Double-DQN) scheduler to dynamically balance source delivery and repair transmission under deadline constraints. We implement PriorityFEC in a distributed edge LLM-serving prototype and evaluate it using Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct across multiple workloads. Experimental results demonstrate that PriorityFEC preserves more useful KV information and achieves substantially higher task accuracy than competing transport schemes, particularly when the deadline is insufficient to deliver the complete KV cache.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Han Shen, Qifu Tyler Sun, Fanyang Meng, Ye Wang, Yongsheng Liang
- 发布：2026-10-15；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
