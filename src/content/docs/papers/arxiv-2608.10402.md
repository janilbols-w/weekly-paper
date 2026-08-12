---
title: "TideRL: Boosting Agentic RL Goodput with Readiness-Aware Scheduling"
description: "Reinforcement learning (RL) for large language models is moving toward multi-turn agentic workloads, where rollout tasks repeatedly pause for external environments, resume with growing contexts, and finish at highly variable times."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.10402) · [PDF](https://arxiv.org/pdf/2608.10402)

## 一句话摘要

Reinforcement learning (RL) for large language models is moving toward multi-turn agentic workloads, where rollout tasks repeatedly pause for external environments, resume with growing contexts, and finish at highly variable times.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement learning (RL) for large language models is moving toward multi-turn agentic workloads, where rollout tasks repeatedly pause for external environments, resume with growing contexts, and finish at highly variable times. In this setting, RL training goodput, measured by training throughput, matters more than raw GPU occupancy: GPU waiting and repeated prefill recomputation are pure overhead. We present TideRL, a readiness-aware elastic RL system with Continuous Task Batching, Resource-Aware Ref-Actor Pipelining, and Elastic Resource Scaling. CTB preserves useful rollout state, $\textrm{RA}^2\textrm{P}$ selects between decoupled streaming and colocated aggregation from the ready backlog and arrival interval, and ERS moves ranks between rollout and training using the same readiness signals. Across text-only and multi-modal agentic workloads, TideRL improves RL training goodput by up to 5.6$\times$ over synchronous baselines and over 33% over asynchronous baselines, while reaching similar task performance. It also improves KV cache hit rate by 1.58$\times$, reduces per-step training time by up to 44.3%, and cuts total waiting time by up to 77.6%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yanyu Ren, Xizheng Wang, Xiao Liu, Bowen Lv, Hanchen Zhang, Shudan Zhang, Hanyu Lai, Shuai Wang, Li Chen, Dan Li, Jie Tang
- 发布：2026-08-12；更新：2026-08-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
