---
title: "SMetric: Rethink LLM Scheduling for Serving Agents with Balanced Session-centric Scheduling"
description: "LLM scheduling is critical to serving, yet how well existing designs fit agentic serving--where agents, not humans, issue the requests--remains unclear."
---

**评分：43/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2607.08565) · [PDF](https://arxiv.org/pdf/2607.08565)

## 一句话摘要

LLM scheduling is critical to serving, yet how well existing designs fit agentic serving--where agents, not humans, issue the requests--remains unclear.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM scheduling is critical to serving, yet how well existing designs fit agentic serving--where agents, not humans, issue the requests--remains unclear. Agents shift the workload in two ways: they consume many more tokens than humans, so the cluster must provide high throughput (TPS) at low latency; and their requests reuse far more KV\$ than chat. Existing schedulers still trade off load balance against KV\$ reuse: cache-aware schedulers may crowd requests onto the few instances caching the KV\$, leaving the rest idle, while balanced schedulers may lose the opportunity for reuse, which is costly at a high reuse ratio. We thus present two key insights: (1) with a global-tier KV\$ store, pursuing load balance need not compromise KV\$ reuse, though the slower global tier must be used with care; and (2) given the agent's intra-session locality, routing requests by their sessions can balance the load with high KV\$ reuse. A key challenge in realizing session-centric scheduling is that the scheduler must identify a request's session statelessly, which is difficult for model providers serving arbitrary agents. SMetric addresses this with differential scheduling based on two indicators derived from the request itself, the session turn and the local KV\$ hit: it schedules first-turn requests for load balance, and sticks follow-ups to the instance with the highest local hit for high KV\$ reuse. As sessions differ widely in size, SMetric sticks a follow-up only if the instance can serve it within its SLO, and otherwise migrates the session to the least-loaded instance to prevent many long sessions from eventually imbalancing the load. Evaluated on real-world traces, SMetric improves the peak TPS by 9-15% under prefill-decode colocation with a provisioned global tier and the peak prefill TPS by 9% under disaggregation over state-of-the-art schedulers, also with lower latency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: slo
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiahao Wang, Kaizhan Lin, Kaixi Zhang, Jinbo Han, Xingda Wei, Sijie Shen, Chenguang Fang, Wenyuan Yu, Rong Chen, Haibo Chen
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
