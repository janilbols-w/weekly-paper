---
title: "CAMR: Compatibility-Aware Memory Replay for Continual Learning in Large Language Models"
description: "Continual learning requires large language models to acquire new knowledge and capabilities while retaining what they have learned."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2610.36734) · [PDF](https://arxiv.org/pdf/2610.36734)

## 一句话摘要

Continual learning requires large language models to acquire new knowledge and capabilities while retaining what they have learned.

## 为什么值得关注

待编辑增强。

## 摘要原文

Continual learning requires large language models to acquire new knowledge and capabilities while retaining what they have learned. Fine-tuning and replay support acquisition and retention, but deciding whether incoming examples need supervision and which historical examples to revisit remains a challenge. We propose Compatibility-Aware Memory Replay (CAMR), an adaptive framework that jointly controls current-example supervision and historical replay. CAMR combines compatibility checks with a learned memory gate to guide an online policy over three actions: learning incoming examples with general replay, jointly reinforcing compatible related examples, and skipping direct supervision of verified mastered duplicates. The policy learns from acquisition, retention, and training-cost feedback under a bounded per-arrival replay budget. We evaluate CAMR with Qwen3-8B-Base on continual factual updating and cross-task and cross-domain learning. On WikiBigEdit, CAMR consistently leads evaluated methods in Original Match from 3K to 100K facts, reaching 93.66% after just 3K facts and surpassing Full-history Replay (LoRA) after 100K facts. It also achieves the highest final scores on all four selected TRACE tasks and maintains or improves earlier-task performance relative to post-acquisition levels in a sequence spanning financial question answering, mathematical reasoning, code generation, and summarization.

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

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jingpu Yang, Tianhao Li, Fengxian Ji, Yufeng Wang, Shuxin Zheng, Xiaoqing Zhang
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
