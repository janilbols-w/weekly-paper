---
title: "DecompressionLM: Deterministic, Diagnostic, and Zero-Shot Concept Graph Extraction from Language Models"
description: "Existing knowledge probing methods rely on pre-defined queries, limiting extraction to known concepts."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2602.00377) · [PDF](https://arxiv.org/pdf/2602.00377)

## 一句话摘要

Existing knowledge probing methods rely on pre-defined queries, limiting extraction to known concepts.

## 为什么值得关注

待编辑增强。

## 摘要原文

Existing knowledge probing methods rely on pre-defined queries, limiting extraction to known concepts. We introduce DecompressionLM, a stateless framework for zero-shot concept graph extraction that discovers what language models encode without pre-specified queries or shared cross-sequence state. Our method targets three limitations of common decoding-based probing approaches: (i) cross-sequence coupling that concentrates probability mass on high-frequency prefixes, (ii) competitive decoding effects that suppress long-tail concepts, and (iii) scalability constraints arising from sequential exploration. Using Van der Corput low-discrepancy sequences with arithmetic decoding, DecompressionLM enables deterministic, embarrassingly parallel generation without shared state across sequences. Across two model families and five quantization variants, we find that activation-aware quantization (AWQ-4bit) expands concept coverage by 30-170%, while uniform quantization (GPTQ-Int4) induces 71-86% coverage collapse - divergent behaviors not reliably reflected by explanation-level perplexity. Corpus-based verification further reveals a 19.6-point hallucination gap between top- and bottom-ranked MMLU-Pro Law models. DecompressionLM establishes concept coverage as a complementary evaluation dimension for assessing knowledge breadth and factual grounding in compressed models intended for deployment. Code is available at https://github.com/ulab-uiuc/decompressionlm.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, quantization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zhaochen Hong, Jiaxuan You
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/ulab-uiuc/decompressionlm](https://github.com/ulab-uiuc/decompressionlm)
- 阅读深度：metadata
