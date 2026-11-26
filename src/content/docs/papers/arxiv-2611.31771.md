---
title: "SPARQL-Planned Single-Hop Traversal over a Live Knowledge Graph for Multi-Hop Question Answering"
description: "Semantic retrieval struggles with multi-hop question answering on both recall and precision: gold passages are buried among distractors that degrade the reader's answer, and retrieving them requires reasoning over the query rather than matching it."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2611.31771) · [PDF](https://arxiv.org/pdf/2611.31771)

## 一句话摘要

Semantic retrieval struggles with multi-hop question answering on both recall and precision: gold passages are buried among distractors that degrade the reader's answer, and retrieving them requires reasoning over the query rather than matching it.

## 为什么值得关注

待编辑增强。

## 摘要原文

Semantic retrieval struggles with multi-hop question answering on both recall and precision: gold passages are buried among distractors that degrade the reader's answer, and retrieving them requires reasoning over the query rather than matching it. GraphRAG techniques expand semantic retrieval by connecting passages to graph nodes and performing one or more hops of expansion after initial retrieval. This improves recall, but multi-hop expansion becomes expensive and brings additional noise into the retrieved set. We break this tradeoff by \emph{interleaving} dense retrieval with knowledge-graph traversal for complex multi-hop questions. Dense retrieval locates the first relevant regions of the search space at good recall, while traversal of a pre-existing external KG (Wikidata) restores precision and improves recall by confirming retrieved passages against a reasoning path through the KG. To keep traversal both question-adaptive and reliable, we have an LLM plan it as code generation task for graph traversal in SPARQL format but \emph{parse rather than execute} the query. On full 1{,}000-question splits under a shared corpus and reader, and with a single configuration applied identically to every dataset, we reach \textbf{62.5 / 75.1} EM/F1 on HotpotQA, \textbf{73.5 / 81.0} on 2WikiMultiHopQA, and \textbf{37.1 / 50.0} on MuSiQue, ahead of reproduced HippoRAG2, T\textsuperscript{2}RAG, and IRCoT on all three benchmarks. A second, token-matched setting stays ahead of T\textsuperscript{2}RAG on HotpotQA and 2Wiki while spending roughly its per-query budget. Executing the generated SPARQL instead of parsing it costs up to 11.4 EM, mostly because raw queries return empty results, not because of syntax errors.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Priyesh Vakharia, Masud Moshtaghi, Pratyay Banerjee, Nicholas Jedema, Amita Misra, Ankit Chadha
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
