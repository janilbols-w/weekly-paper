---
title: "Verifiable but Not Predictable: What Sentence Embeddings Know About Propositional Decomposition"
description: "Quality control for proposition decomposition by large language models (LLMs) raises two asymmetric questions."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.33668) · [PDF](https://arxiv.org/pdf/2611.33668)

## 一句话摘要

Quality control for proposition decomposition by large language models (LLMs) raises two asymmetric questions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Quality control for proposition decomposition by large language models (LLMs) raises two asymmetric questions. After decomposition, one can verify: given a sentence and a candidate proposition, does the proposition belong to that sentence? Before decomposition, one would like to predict: how many propositions should the sentence yield? On PropSegmEnt, a corpus of English Wikipedia sentences each segmented by three human annotators, we find that the two questions live in different representational spaces. A natural language inference (NLI) judge verifies membership with 92.8% accuracy and an area under the ROC curve (AUC) of 0.977, and its residual errors turn out to be mostly propositions that are true in document context rather than genuine entailment mistakes. Vector geometry cannot verify: cosine similarity saturates, and a sentence embedding is not a linear combination of its propositions' embeddings. For prediction, every symbolic anchor we test, namely token count, the CPIDR idea-density counter, and a Neo-Davidsonian predicate count, reduces to a length proxy once token count is controlled. A linear ridge probe on sentence embeddings is the only predictor that keeps genuine count signal: its length-partialled correlation with human counts is 0.40-0.49 with bootstrap confidence intervals (CIs) excluding zero, and it orders length-matched sentence pairs correctly 67-71% of the time against a 50% chance level, statistically matching the inter-annotator agreement ceiling. This signal survives INT8 quantization without loss, INT4 at a small cost, and Matryoshka truncation to 256 dimensions, and it works as well in a 2021 encoder as in a 2025 one. Its structured weakness is a systematic under-splitting of long sentences. We distill the protocol lessons, including a retracted pilot study, into a checklist for probing length-confounded quantities.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, int8, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qingan Li, Tianxiao Wu, Xiling Cui
- 发布：2026-11-25；更新：2026-11-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
