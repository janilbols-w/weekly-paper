---
title: "DeferMem: Query-Time Evidence Distillation via Reinforcement Learning for Long-Term Agent Memory"
description: "Large language model (LLM) agents still struggle to effectively use long-term memory, with answer-supporting evidence often scattered across long conversational histories and buried in substantial irrelevant content."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.22411) · [PDF](https://arxiv.org/pdf/2605.22411)

## 一句话摘要

Large language model (LLM) agents still struggle to effectively use long-term memory, with answer-supporting evidence often scattered across long conversational histories and buried in substantial irrelevant content.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) agents still struggle to effectively use long-term memory, with answer-supporting evidence often scattered across long conversational histories and buried in substantial irrelevant content. Existing memory systems commonly process memory into dedicated units before future queries are known and retrieve these preconstructed units at query time. Because the contents and granularity of these units are determined before the current query is known, the retrieved units can remain coarse and noisy for that query, leaving downstream answerers to further denoise them and uncover query-specific evidence. We present DeferMem, a long-term memory framework that decouples this problem into high-recall candidate retrieval and query-conditioned evidence distillation. DeferMem uses a lightweight segment-link structure to organize raw history and retrieve broad candidates at query time. A memory distiller then distills these high-recall but highly noisy candidates into a set of faithful, self-contained, and query-conditioned evidence. To train this distiller, we introduce DistillPO, a reinforcement learning algorithm that formulates post-retrieval evidence distillation as a structured action comprising message selection and evidence rewriting. It optimizes this action with a decomposed-and-gated reward pipeline and structure-aligned advantage assignment, gating reward components from validity to quality checks while exposing answerability-related feedback early and assigning each reward to its responsible output span. On LoCoMo and LongMemEval-S, DeferMem surpasses strong baselines in QA accuracy and memory-system efficiency, achieving the highest QA accuracy and fastest runtime while consuming no commercial-API tokens for memory operations.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jianing Yin, Tan Tang, Yingcai Wu
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
