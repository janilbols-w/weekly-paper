---
title: "Pallas: A Proactive KV Cache Migration Framework for LLM Inference in AI-RAN"
description: "AI-RAN brings large language model (LLM) serving close to mobile users, but cellular handover can separate an active request from its inference state: the user attaches to a target base station (gNB) while the large and growing key-value (KV) cache remains at the source."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.16477) · [PDF](https://arxiv.org/pdf/2608.16477)

## 一句话摘要

AI-RAN brings large language model (LLM) serving close to mobile users, but cellular handover can separate an active request from its inference state: the user attaches to a target base station (gNB) while the large and growing key-value (KV) cache remains at the source.

## 为什么值得关注

待编辑增强。

## 摘要原文

AI-RAN brings large language model (LLM) serving close to mobile users, but cellular handover can separate an active request from its inference state: the user attaches to a target base station (gNB) while the large and growing key-value (KV) cache remains at the source. Retaining inference at the source preserves service continuity but persistently increases inter-token latency (ITL), whereas recovering the state at the target restores serving locality but requires KV-cache transfer, recomputation, or a combination of both only after handover, directly prolonging service interruption time (SIT). This work presents Pallas, a \textit{proactive} KV-cache migration framework that prepares the inference state at the predicted target before handover, in parallel with ongoing source-side inference and token delivery. At the preparation trigger, Pallas partitions the token sequence into a stable historical prefix and an evolving suffix. The target reconstructs the prefix through local prefill, while the source streams the KV blocks generated for the suffix. At handover, the target assembles both portions into an up-to-date KV cache and resumes decoding locally, leaving only unfinished preparation to contribute to SIT. An online scheduler selects the \textit{prefetching window}, which determines how early preparation begins before handover, based on mobility predictions and runtime telemetry. Across three LLMs and $100$--$500~\mathrm{Mbps}$ inter-gNB links, our vLLM-based prototype reduces average SIT by factors of $2.28$--$89.68$ over target-side recovery approaches and lowers average ITL by $16.0\%$--$50.0\%$ compared with source-side forwarding.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tianhang Ding, Jianchun Liu, Hongli Xu
- 发布：2026-08-17；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
