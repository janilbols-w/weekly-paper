---
title: "OpticalRAG: Pixel-Space Compression for Token-Efficient Retrieval-Augmented Generation"
description: "Retrieval-augmented generation (RAG) is bottlenecked by the token budget of large language models: feeding long documents into the context window is expensive, while aggressive textual compression discards fine-grained information that is irreversibly lost in a one-dimensional token sequence."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.13675) · [PDF](https://arxiv.org/pdf/2611.13675)

## 一句话摘要

Retrieval-augmented generation (RAG) is bottlenecked by the token budget of large language models: feeding long documents into the context window is expensive, while aggressive textual compression discards fine-grained information that is irreversibly lost in a one-dimensional token sequence.

## 为什么值得关注

待编辑增强。

## 摘要原文

Retrieval-augmented generation (RAG) is bottlenecked by the token budget of large language models: feeding long documents into the context window is expensive, while aggressive textual compression discards fine-grained information that is irreversibly lost in a one-dimensional token sequence. We argue that this bottleneck is not fundamental to information density but to the choice of compression \emph{modality}. Modern visual encoders can pack the contents of a rendered text page into roughly a hundred visual tokens with little semantic loss, opening a new compression-fidelity tradeoff that purely textual methods cannot reach. We present \textbf{OpticalRAG}, a framework that renders documents as page images, encodes them with a frozen vision encoder, and distills the retrieved visual tokens into as few as $16$ injected tokens before passing them to the LLM. Two ingredients make this work without expensive cross-modal training: (i) \emph{Encoder-Bridged Retrieval}, which projects text-query states into the visual feature space of the frozen encoder, through a projection shared with the compressor, to retrieve visual tokens from a text query, with no contrastive training; and (ii) \emph{Query-Driven Distillation}, a lightweight cross-attention compressor that condenses the retrieved visual tokens into a small set of query-conditioned prefix tokens. On LongBench-v2, BAMBOO, and LooGLE-v2, OpticalRAG achieves the best compression-aware accuracy (CAP) on all three benchmarks while injecting only $16$ tokens, and improves the closed-book Qwen2.5-7B-Instruct backbone by $5.17$ points on LongBench-v2.Code is available at https://github.com/brighterr/OpticalRAG.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Senhao Liu, Yuheng Zhang, Chunyu Wei, Yueguo Chen, Xinran Zhang
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/brighterr/OpticalRAG](https://github.com/brighterr/OpticalRAG)
- 阅读深度：metadata
