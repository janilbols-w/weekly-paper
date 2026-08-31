---
title: "Parser States Already Know: Structure-Conditioned KV Persistence for Structured Generation"
description: "Structured generation underpins large language model (LLM) agents that produce JSON, SQL, and function calls, where a single wrong field can cause the downstream action to fail."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2608.28276) · [PDF](https://arxiv.org/pdf/2608.28276)

## 一句话摘要

Structured generation underpins large language model (LLM) agents that produce JSON, SQL, and function calls, where a single wrong field can cause the downstream action to fail.

## 为什么值得关注

待编辑增强。

## 摘要原文

Structured generation underpins large language model (LLM) agents that produce JSON, SQL, and function calls, where a single wrong field can cause the downstream action to fail. Constrained decoding already tracks parser transitions to enforce formal validity, and these transitions expose how generated tokens participate in schema-critical decisions such as required fields, arguments, and structural boundaries under the active grammar. Existing KV compression largely leaves this task-relevant structural signal unused. We introduce PASK (Parser-Aware Structural KV Persistence), which turns parser-derived structure into layer-group-specific KV persistence decisions. PASK addresses the mismatch between model-side KV sensitivity and task-level structured risk by using task-error sensitivity to set minimum protection floors and attention-output distortion to allocate residual KV capacity. An offline calibration stage compiles these signals into a persistence policy, leaving only lightweight structure-conditioned lookup online. At a targe total KV budget of 0.33, PASK outperforms the strongest compressed baseline by 17.39 percentage points on average across eight BFCL non-live and Live subcategories on Qwen3-4B. In end-to-end serving, PASK achieves up to 2.2x higher throughput and 3.3x lower TPOT, while using 0.53x the peak GPU memory of Full KV.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Linze Wu, Xinrui Chen
- 发布：2026-08-31；更新：2026-08-31
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
