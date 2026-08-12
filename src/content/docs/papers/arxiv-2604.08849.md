---
title: "SatIR: Scalable High-Recall Constraint-Satisfaction-Based Information Retrieval for Clinical Trials Matching"
description: "Many real-world retrieval and matching problems require more than topical relevance: a candidate must satisfy the specific constraints of one profile among many, not just be relevant to it."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2604.08849) · [PDF](https://arxiv.org/pdf/2604.08849)

## 一句话摘要

Many real-world retrieval and matching problems require more than topical relevance: a candidate must satisfy the specific constraints of one profile among many, not just be relevant to it.

## 为什么值得关注

待编辑增强。

## 摘要原文

Many real-world retrieval and matching problems require more than topical relevance: a candidate must satisfy the specific constraints of one profile among many, not just be relevant to it. Clinical trials are a high-stakes instance of this challenge: they are central to evidence-based medicine, yet many struggle to meet enrollment targets, despite the availability of over half a million trials listed on ClinicalTrials.gov, which attracts approximately two million users monthly. Existing retrieval techniques, largely based on keyword and embedding-similarity matching, treat eligibility constraints as soft signals rather than binding requirements, resulting in low recall, low precision, and limited interpretability. We propose SatIR, a scalable, efficient, high-precision, high-recall, interpretable clinical trial retrieval method based on formal constraint satisfaction. Leveraging established medical ontologies, we use Large Language Models (LLMs) to convert informal reasoning -- regarding ambiguity, implicit clinical assumptions, and incomplete patient records -- into explicit, precise, controllable, and interpretable formal Satisfiability Modulo Theories (SMT) constraints. For scalable and efficient retrieval, we project the SMT matching problem onto relational algebra, enabling an efficient database implementation that retains high recall while sacrificing little precision. SatIR consistently improves eligibility-aware retrieval over similarity-based baselines on the SIGIR 2016 dataset and a benchmark derived from TREC 2022. Relative to TrialGPT-style retrieval, SatIR retrieves 32%-72% more relevant-and-eligible trials per patient on SIGIR 2016 and achieves 1.8-3.2x higher eligible-trial recall on the TREC benchmark. Retrieval is fast, requiring only 146 milliseconds per patient over 3,621 SIGIR trials.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: low precision
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zikai Zhou, Yufei Jin, Yilin Xu, Yu-Chiang Wang, Chieh-Ju Chao, Monica S. Lam
- 发布：2026-08-12；更新：2026-08-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
