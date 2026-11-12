---
title: "Bursts That Outlast Themselves: Persistent Degradation in Prefix-Cached Agent Serving"
description: "LLM agents drive inference engines with closed-loop sessions whose context grows every turn, and serving them economically depends on prefix caching: a hit costs an incremental prefill of about a thousand tokens, a miss recomputes a 10--40K-token context."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.13412) · [PDF](https://arxiv.org/pdf/2611.13412)

## 一句话摘要

LLM agents drive inference engines with closed-loop sessions whose context grows every turn, and serving them economically depends on prefix caching: a hit costs an incremental prefill of about a thousand tokens, a miss recomputes a 10--40K-token context.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM agents drive inference engines with closed-loop sessions whose context grows every turn, and serving them economically depends on prefix caching: a hit costs an incremental prefill of about a thousand tokens, a miss recomputes a 10--40K-token context. We show that this makes prefix-cached agent serving metastable. With an identical base workload, a few minutes of extra arrivals leaves a vLLM server in a degraded regime--a ~10% hit ratio, about half the throughput, and a backlog that grows for the remaining 70 minutes--while its no-burst twin stays healthy (9 of 12 pairs; none in the reverse direction). The regime appears at loads the cache-warm server sustains, is absent without prefix caching, and also appears with Qwen3-32B on SWE-bench agent trace shapes and on SGLang, which tolerates larger triggers. Slower service keeps more sessions in the system, their working set outgrows the KV pool, and every turn becomes a recomputation; a first-order workload-balance condition, calibrated independently, brackets when the regime can drain. Getting out is the harder problem: throttling new admissions recovered 1 of 7 matched collapsed runs, while suspending admitted sessions against a capacity-based limit recovered all of them within minutes. A CPU offload tier delays the collapse but does not prevent it. A budgeter that bounds the resident KV demand of active sessions to the pool, with thresholds that need no per-workload tuning, prevented the failure in every run we tested.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: prefix caching
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Wen Huang, Jack Liu
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
