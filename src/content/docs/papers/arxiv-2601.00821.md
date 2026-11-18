---
title: "Fidelity Before Structure: Verbatim Chunks Beat Lossy Artifact Extraction in Long-Conversation LLM Memory"
description: "A growing class of conversational-memory systems compresses dialogue history into structured artifacts (extracted facts, decisions, or events)."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2601.00821) · [PDF](https://arxiv.org/pdf/2601.00821)

## 一句话摘要

A growing class of conversational-memory systems compresses dialogue history into structured artifacts (extracted facts, decisions, or events).

## 为什么值得关注

待编辑增强。

## 摘要原文

A growing class of conversational-memory systems compresses dialogue history into structured artifacts (extracted facts, decisions, or events). The premise is that distilled structure retrieves better than raw text. We test this premise with a controlled ablation. Within one fixed retrieval--rerank--reasoning pipeline, we swap only the stored representation (LLM-extracted typed artifacts versus verbatim conversation chunks) and hold the model, retriever, reranker, and judge constant. Verbatim chunks win by 15.9 points on LoCoMo (43.9% vs. 28.0%) and by 22.0 points on LongMemEval-S (67.4% vs. 45.4%). A semantic graph does not recover the gap, and six confound controls reproduce the effect. The mechanism is lossy distillation rather than structure per se. Accuracy tracks how much source text survives in the store, and the extracted-artifact pipeline does not beat naive RAG in overall accuracy (chunks do abstain worse; see Limitations). For the extraction designs we test, structured memory should augment verbatim text rather than replace it. Adding artifacts alongside chunks costs no detected accuracy, while substituting them forfeits the gap. Code and data are available at https://github.com/tao-hpu/cog-canvas.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Tao An
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/tao-hpu/cog-canvas](https://github.com/tao-hpu/cog-canvas)
- 阅读深度：metadata
