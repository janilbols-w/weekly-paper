---
title: "PATTON: Enabling Commodity PIM for Production LLM Serving"
description: "Processing-in-Memory (PIM) is promising for accelerating memory-bound decode attention, but attention acceleration alone is insufficient for production LLM serving, where engines dynamically allocate, populate, share, cache, and reclaim logical KV cache blocks."
---

**评分：53/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.11392) · [PDF](https://arxiv.org/pdf/2609.11392)

## 一句话摘要

Processing-in-Memory (PIM) is promising for accelerating memory-bound decode attention, but attention acceleration alone is insufficient for production LLM serving, where engines dynamically allocate, populate, share, cache, and reclaim logical KV cache blocks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Processing-in-Memory (PIM) is promising for accelerating memory-bound decode attention, but attention acceleration alone is insufficient for production LLM serving, where engines dynamically allocate, populate, share, cache, and reclaim logical KV cache blocks. Supporting this lifecycle on commodity PIM requires efficient physical memory allocation, block-to-address mapping, and command generation. For the Value cache, these requirements create a fundamental conflict among GEMV efficiency, single-token write efficiency, and memory capacity: GEMV-optimized layouts scatter newly generated Value vectors across rows, making writes costly, while finer-grained memory sharing improves capacity utilization but fragments GEMV reductions. We present PATTON, a PIM runtime that integrates production LLM serving engines with commodity PIM. PATTON introduces hierarchical granule allocation: block-sized Key and Value granules map one-to-one to logical token blocks, fixing their physical placements and commands, while coarser granules group blocks for efficient GEMV execution and memory utilization. A Commit Zone stages partial Value blocks for efficient single-token writes before committing them to GEMV-optimized locations. PATTON tracks these placements to generate KV cache writes and QK-transpose/SV commands. Across attention execution and runtime-induced prefill recomputation, PATTON achieves an average 1.95x speedup and 4.83x higher energy efficiency over evaluated baselines, requires no PIM processing-unit modifications, and maintains a KV cache hit rate comparable to the native GPU KV cache in vLLM.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 18 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Hangyeol Kim, Sanghyun Lee, Teokkyu Suh, Joo-Young Kim
- 发布：2026-09-10；更新：2026-09-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
