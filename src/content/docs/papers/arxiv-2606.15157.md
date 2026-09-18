---
title: "Exploring a Layer-Wise Design Space for KV Cache Eviction"
description: "KV cache eviction methods typically use a single retention-rule family throughout a model, making eviction-method identity a model-level design choice."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2606.15157) · [PDF](https://arxiv.org/pdf/2606.15157)

## 一句话摘要

KV cache eviction methods typically use a single retention-rule family throughout a model, making eviction-method identity a model-level design choice.

## 为什么值得关注

待编辑增强。

## 摘要原文

KV cache eviction methods typically use a single retention-rule family throughout a model, making eviction-method identity a model-level design choice. Yet Transformer layers differ substantially in their attention behavior, representations, and sensitivity to compression, suggesting that a uniform rule may overlook useful layer-wise structure. This raises a basic question: should eviction methods themselves vary across layers? We investigate this question by composing existing eviction methods across Transformer layers and systematically exploring the resulting layer-wise design space. Using simple offline profiles, we construct fixed routes and study how their quality varies with method placement and cache budget. On LongBench, heterogeneous routing improves performance on a majority of tasks over homogeneous policies at the same cache budget. Even when method counts are held fixed, the profile-guided placement ranks second among 100 evaluated assignments, demonstrating that routing quality depends strongly on where methods are placed. Moreover, the same fixed route outperforms the best of nine standalone baselines across all five tested cache budgets. Together, these results establish layer-wise method composition as an exploitable, placement-sensitive design dimension for KV cache compression.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chao Fei, Kaihua Liang, Hanzhi Hu, Hongcheng Guo, Jian Weng, Marco Canini, Panos Kalnis
- 发布：2026-09-18；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
