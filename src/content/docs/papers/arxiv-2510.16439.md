---
title: "FrugalPrompt: Reducing Contextual Overhead in Large Language Models via Token Attribution"
description: "Human communication heavily relies on laconism and inferential pragmatics, allowing listeners to successfully reconstruct rich meaning from sparse, telegraphic speech."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2510.16439) · [PDF](https://arxiv.org/pdf/2510.16439)

## 一句话摘要

Human communication heavily relies on laconism and inferential pragmatics, allowing listeners to successfully reconstruct rich meaning from sparse, telegraphic speech.

## 为什么值得关注

待编辑增强。

## 摘要原文

Human communication heavily relies on laconism and inferential pragmatics, allowing listeners to successfully reconstruct rich meaning from sparse, telegraphic speech. In contrast, large language models (LLMs) owe much of their stellar performance to expansive input contexts, yet such verbosity inflates monetary costs, carbon footprint, and inference-time latency. This overhead manifests from the redundant low-utility tokens present in typical prompts, as only a fraction of tokens typically carries the majority of the semantic weight. Inspired by the aforementioned cognitive psycholinguistic processes, we address this inefficiency by introducing FrugalPrompt, a novel prompt compression framework for LLMs, which retains only the most semantically significant tokens. Leveraging two state-of-the-art token attribution methods, GlobEnc and DecompX, we assign salience scores to every token in an input sequence, rank them to retain the top-k% tokens, and obtain a sparse frugalized prompt. We establish the theoretical stability of our approach and provide strong empirical results across a suite of four NLP tasks to study the trade-off between the portion of retained tokens and performance. Experimental findings across retention settings reveal asymmetric performance patterns that suggest potential task contamination effects. We posit that our work contributes to a more nuanced understanding of LLM behavior in performance-efficiency trade-offs and delineates the boundary between tasks tolerant of contextual sparsity and those requiring exhaustive context.

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

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Syed Rifat Raiyan, Md Farhan Ishmam, Abdullah Al Imran, Mohammad Ali Moni
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
