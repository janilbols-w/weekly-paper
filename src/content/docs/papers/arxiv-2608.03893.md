---
title: "Cross-Model KV Cache Transfer in LLM Families: A Closed-Form Linear Mapping for Prefill Reuse"
description: "Production deployments often swap between different-sized models in a family for cost-quality cascading, mid-conversation switching, and routing, and each swap forces the receiver to repay the prefill from scratch."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.03893) · [PDF](https://arxiv.org/pdf/2608.03893)

## 一句话摘要

Production deployments often swap between different-sized models in a family for cost-quality cascading, mid-conversation switching, and routing, and each swap forces the receiver to repay the prefill from scratch.

## 为什么值得关注

待编辑增强。

## 摘要原文

Production deployments often swap between different-sized models in a family for cost-quality cascading, mid-conversation switching, and routing, and each swap forces the receiver to repay the prefill from scratch. We propose cross-model KV cache transfer, where the receiver reuses the source's KV cache, skipping prefill. We find that cross-model KV has substantial linear structure across matched-KV pairs, where source and target share KV head count and per-head dimension. On Qwen3 14B->32B, one source layer explains 56% of variance in the target's keys and 32% in values, rising to 79% and 65% with multiple source layers. Building on this, we design a closed-form ridge mapper that operates per head and proceeds in three steps. First, for each target layer we select the top-k most predictive source layers and concatenate their KV as input. Second, we strip RoPE from the keys before mapping, so the fit is position-free and reusable across context lengths. Third, we fit ridge regression on a small calibration set of 500 FineWeb-Edu sequences of 1,024 tokens each. Surprisingly, across six pairs in three families, this linear mapper retains 73-98% of the receiver's standalone-prefill accuracy on four pairs, while two degrade sharply. A nonlinear MLP recovers up to +37 pp HellaSwag retention on the failures. The mapper runs 2.7-25x faster than re-prefill and remains stable across multi-turn handoff, making cross-model KV cache transfer practical.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Taekyung Heo, Rasoul Shafipour, Ritchie Zhao, Maximilian Golub, Mohammad Mahdi Kamani, Ritika Borkar, Makesh Tarun Chandran, Pantea Zardoshti, Bita Darvish Rouhani
- 发布：2026-08-04；更新：2026-08-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
