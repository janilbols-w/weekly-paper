---
title: "TSWAP: A Multilingual Retrieval-Augmented Thai Wellness Advisor"
description: "We present TSWAP, a deployed eight-language conversational wellness advisor grounded, via retrieval-augmented generation, in a verified knowledge base of Thai traditional medicine and certified wellness providers."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2608.22917v1) · [PDF](https://arxiv.org/pdf/2608.22917v1)

## 一句话摘要

We present TSWAP, a deployed eight-language conversational wellness advisor grounded, via retrieval-augmented generation, in a verified knowledge base of Thai traditional medicine and certified wellness providers.

## 为什么值得关注

待编辑增强。

## 摘要原文

We present TSWAP, a deployed eight-language conversational wellness advisor grounded, via retrieval-augmented generation, in a verified knowledge base of Thai traditional medicine and certified wellness providers. An unmodified open-weight LLM (Qwen3.6-35B-A3B on vLLM) is grounded on a ~30.6K-chunk Thai index by a hybrid dense-sparse retriever with cross-encoder reranking; a first-turn query classifier forces tool-based retrieval for entity lookups; a rule-based safety layer enforces medical scope and Thai emergency routing; and all eight languages are served zero-shot with translate-then-retrieve. We release the first Thai traditional-medicine/wellness retrieval benchmark (50 questions with gold document IDs; Recall@5 = 0.88), production QA logs (91.1% test-retest pass over 259 cases), and a 71-question frontier no-retrieval probe showing what each grounding pillar contributes: without the safety prompt the backend model family produced a full drug-dosing schedule and complied with out-of-scope requests, and without the knowledge base it produced zero verifiable provider recommendations. We further report two transferable deployment findings: English-calibrated 4-bit AWQ quantization corrupts Thai tone marks, and forced-retrieval routing is necessary for reliable grounding.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Pornthep Ukosaramig, Kobkrit Viriyayudhakorn
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
