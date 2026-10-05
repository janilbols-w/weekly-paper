---
title: "Morpheus: A Morphology-Aware Neural Tokenizer and Word Embedder for Turkish"
description: "Turkish is agglutinative: meaning is carried by morphemes, yet the subword tokenizers that drive modern language models split words by corpus statistics, fragmenting semantically loaded suffixes and -- in the case of WordPiece and rule-based analyzers -- failing to decode their output back to the original text."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2606.18717) · [PDF](https://arxiv.org/pdf/2606.18717)

## 一句话摘要

Turkish is agglutinative: meaning is carried by morphemes, yet the subword tokenizers that drive modern language models split words by corpus statistics, fragmenting semantically loaded suffixes and -- in the case of WordPiece and rule-based analyzers -- failing to decode their output back to the original text.

## 为什么值得关注

待编辑增强。

## 摘要原文

Turkish is agglutinative: meaning is carried by morphemes, yet the subword tokenizers that drive modern language models split words by corpus statistics, fragmenting semantically loaded suffixes and -- in the case of WordPiece and rule-based analyzers -- failing to decode their output back to the original text. This paper presents \textbf{Morpheus}, a neural morpheme-boundary model for Turkish that is at once a lossless, morphology-aware tokenizer and a word-embedding producer. A differentiable Poisson-binomial dynamic program turns per-character boundary probabilities into soft morpheme memberships during training and exact segments at inference, with no string normalization, so $\mathrm{decode}(\mathrm{encode}(w)) = w$ holds by construction. Because the model is neural, the same forward pass that tokenizes also emits a structured word embedding. Among reversible tokenizers -- the only ones valid for generation -- Morpheus attains the lowest bits-per-character ($1.425$), roughly doubles the gold morphological alignment of the subword family (MorphScore macro-F1 $0.61$ vs.\ ${\sim}0.32$), and uses ${\sim}19\%$ less GPU memory than 64K-vocabulary subword tokenizers. As an embedder, frozen Morpheus vectors lead on lexical retrieval (root-family MAP $0.85$) and same-root verification (ROC-AUC $1.00$), surpassing the multilingual retriever BGE-M3 and BERTurk; on context- and inflection-dependent tasks (NER, case/number probing) the heavier contextual encoders remain ahead -- a trade-off we attribute to Morpheus's root-centric geometry. Code: https://github.com/lonewolf-rd/TurkishMorpheus; model: https://huggingface.co/lonewolflab/Morpheus-TR-50K; interactive demo: https://huggingface.co/spaces/lonewolflab/morpheus-tr-demo.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Tolga \c{S}akar
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/lonewolf-rd/TurkishMorpheus](https://github.com/lonewolf-rd/TurkishMorpheus)
- 阅读深度：metadata
