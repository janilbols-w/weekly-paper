---
title: "Where KV-Cache Error Lives in Looped Language Models: A Diagnostic Study of Ouro and Huginn"
description: "A looped language model applies one block of layers 4 times per token and keeps a key/value (KV) plane for each loop."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.41825) · [PDF](https://arxiv.org/pdf/2610.41825)

## 一句话摘要

A looped language model applies one block of layers 4 times per token and keeps a key/value (KV) plane for each loop.

## 为什么值得关注

待编辑增强。

## 摘要原文

A looped language model applies one block of layers 4 times per token and keeps a key/value (KV) plane for each loop. We study where storage error changes the next-token distribution and how shared-weight error accumulates, using Ouro-1.4B (4 loops) on GSM8K and MATH and Huginn-0125 (32 loops) on GSM8K-derived chains, with dense, simulated quantization. Per unit of error, values carry 94% of the diagonal Fisher mass, but measured KL is dominated by keys with larger quantization errors. Local second-order prediction follows the measured KL of typical sequences, including 136 held-out chains, but misses a few confident rows, and a local second-order factor for shared weights at 32 loops ranges from 1.65 (INT8) to 4.09 (INT4), so it depends on the error direction. A cell-level allocator lowers one-step KL at 25-48% of BF16 bytes, while paired task-accuracy comparisons depend on budget and the 25% gap against K4V2 shrinks to near zero under a post hoc answer-extraction check. A later Ouro-2.6B test retains the key/value split but falsifies measured-cost allocation's advantage over Fisher at 31%; across all 21 ledger registrations, 60 of 176 criteria failed.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Dezhen Lu, Runguo Li, Zixiang Ni, Yuchen Tang, Xingquan Kong, Jiaxing Yang, Jiarui Guo, Lingxiang Gao
- 发布：2026-11-02；更新：2026-11-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
