---
title: "PACE: Keeping the Right Tokens in the KV Cache Is Not Enough for Long-Horizon LLM Agents"
description: "Long-horizon LLM agents accumulate sessions of up to millions of tokens, far more key-value (KV) cache than one GPU holds, so serving systems keep a small budget of tokens and evict the rest."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.10240) · [PDF](https://arxiv.org/pdf/2611.10240)

## 一句话摘要

Long-horizon LLM agents accumulate sessions of up to millions of tokens, far more key-value (KV) cache than one GPU holds, so serving systems keep a small budget of tokens and evict the rest.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-horizon LLM agents accumulate sessions of up to millions of tokens, far more key-value (KV) cache than one GPU holds, so serving systems keep a small budget of tokens and evict the rest. Eviction methods differ in which tokens they keep but share one goal: that the tokens a later step needs are still cached. We show this is not enough. In 100K-token coding sessions on Qwen3-8B with a 2,048-token budget, a planner-guided policy that keeps over 99% of the needed tokens resident still fails late steps increasingly often: its accuracy falls from 93% to 64% as the gap between a definition and its use grows from 2K to 90K tokens, at residency 0.996. The needed tokens are resident but unretrievable: what grows is their rotary-position distance to the query. We present PACE (Planner-Aware Context Engine), a KV-cache engine that couples plan-aware retention, in which the agent's planner tells the cache which context future steps will read, with bounded positions, which renumber kept tokens so their rotary distance to the query stays below 8K at any session length. In a pre-registered evaluation on fresh tasks, PACE passes 97% of hidden unit tests at 100K tokens, against 42% for H2O and 3% for SnapKV under the same budget, and needs both components: either alone reaches 63% (the combination beats each, p < 10^-4). The result holds with length: in 1M- and 2M-token sessions on one 24 GB GPU, with definitions written 0.9M and 1.8M tokens before use, PACE passes 99% and 100% of checks and recalls every session fact, while bounded positions without foresight falls from 33% to 13%; PACE holds under 0.7 GB of KV state where the full cache would need 147-295 GB. Renumbering is exact, costs no measurable perplexity, and adds 9% wall time. On Mistral-7B, whose coding ability caps it at 40% even with nothing evicted, PACE stays at that ceiling while retention alone falls below it.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Suman Chatterjee
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
