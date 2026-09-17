---
title: "Machine Translation between English and Syriac (East Syriac Dialect) using Statistical Machine Learning"
description: "UNESCO considers the Assyrian (Syriac) language an endangered language."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.18529) · [PDF](https://arxiv.org/pdf/2609.18529)

## 一句话摘要

UNESCO considers the Assyrian (Syriac) language an endangered language.

## 为什么值得关注

待编辑增强。

## 摘要原文

UNESCO considers the Assyrian (Syriac) language an endangered language. Although Assyrians speak the language worldwide, the speaking population is uncertain (ranging from 500,000 to 1,500,000). Syriac is also one of the least studied languages in Natural Language Processing (NLP). Despite advances in Machine Translation (MT) over the past decade, the lack of publicly available corpora and the orthographic complexity of the Syriac script, specifically the Madnkhaya script, have left this language entirely ignored in the computational linguistics literature. This study develops the first phrase-based Statistical MT (SMT) model for English-to-Assyrian MT using the Moses framework. We created a dataset of 38,847 sentence pairs from the complete English and Syriac Bible, merging a pre-existing New Testament dataset with an Old Testament built from scratch through PDF extraction, using custom segmentation scripts and manual alignment review by three bilingual annotators. The Syriac side of the corpus undergoes diacritic removal and Byte-Pair Encoding tokenization to reduce orthographic sparsity before training. We trained and evaluated six models using different configurations and splitting-scheme ratios, language model order, distortion limits, and the inclusion of an Operation Sequence Model. The best-performing configuration achieves a word-level BLEU score of 23.54. Human evaluation by 11 native Assyrian speakers resulted in mean adequacy and fluency scores of 3.42 and 3.34 out of 5, respectively. These results are consistent with comparable low-resource SMT models trained on Biblical corpora for morphologically rich Semitic languages. The corpora, scripts, and trained model are publicly available, providing the research community with the first systematically curated English-Syriac dataset and a reproducible baseline for future MT and broader NLP work on this endangered language.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hadiana Sliwa, Hossein Hassani
- 发布：2026-09-17；更新：2026-09-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
