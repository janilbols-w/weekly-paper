---
title: "Lexical Prompt Compression for Large Language Models: A Training-Free, Deterministic Pipeline with Empirical Pareto Analysis Across Eleven Task Categories"
description: "Recent advances in large language models (LLMs) have made prompts increasingly large and complex."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.13154) · [PDF](https://arxiv.org/pdf/2609.13154)

## 一句话摘要

Recent advances in large language models (LLMs) have made prompts increasingly large and complex.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent advances in large language models (LLMs) have made prompts increasingly large and complex. Techniques such as chain-of-thought reasoning (Wei et al., 2022) and in-context learning (Brown et al., 2020) frequently push real-world prompts past several thousand tokens, increasing inference cost and latency. Learned compression methods such as LLMLingua (Jiang et al., 2023) and Selective Context (Li et al., 2023) achieve high compression ratios but require auxiliary language models and are non-deterministic. We ask a complementary question: how far can a training-free, fully deterministic, CPU-only pipeline based on classical lexical NLP be pushed before output quality degrades significantly? Eleven toggleable lexical transformations - stopword removal, filler-phrase deletion, contraction and abbreviation substitution, part-of-speech-based pruning, lemmatization, WordNet-driven synonym shortening, and named-entity preservation - are assembled into a configurable pipeline. Fifteen configurations are evaluated on 1,242 English-only prompts from six sources (Dolly-15k, LMSYS-Chat-1M, WildChat-1M, MMLU, GSM8K, HellaSwag), spanning eleven automatically derived task categories, yielding 18,630 paired GPT-4o-mini completions. Output preservation is measured using BLEU, ROUGE-1/2/L, BERTScore-F1, and SentenceBERT cosine similarity. The most aggressive configuration achieves a mean token reduction of 40.3% (sigma = 9.2) at a BERTScore-F1 of 0.876 against the original-prompt output; a stopword-only configuration achieves 29.6% reduction at 0.913. The compression-versus-fidelity Pareto frontier is characterized per task category, with commonsense reasoning a systematic failure mode under aggressive compression. All code, prompts, and per-cell results are released for reproducibility.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shamin Chokshi
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
