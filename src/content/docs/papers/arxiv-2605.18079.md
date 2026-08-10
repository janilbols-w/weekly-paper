---
title: "The Expressive Power of Low Precision Softmax Transformers with (Summarized) Chain-of-Thought"
description: "Existing expressivity results for transformers typically rely on hardmax attention, high precision, and other architectural modifications that disconnect them from the models used in practice."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2605.18079) · [PDF](https://arxiv.org/pdf/2605.18079)

## 一句话摘要

Existing expressivity results for transformers typically rely on hardmax attention, high precision, and other architectural modifications that disconnect them from the models used in practice.

## 为什么值得关注

待编辑增强。

## 摘要原文

Existing expressivity results for transformers typically rely on hardmax attention, high precision, and other architectural modifications that disconnect them from the models used in practice. We bridge this gap by analyzing standard transformer decoders with softmax attention and rounding of activations and attention weights, while allowing depth and width to grow logarithmically with the context length. As an intermediate step, we construct hardmax transformers with ternary activations and well-separated attention scores that simulate Turing machines using Chain-of-Thought (CoT). This lets us convert the constructions to equivalent softmax transformers without the unrealistic parameter magnitudes or activation precision that prior approaches would require. Using the same technique, we analyze a recently proposed summarized CoT paradigm and show that it simulates Turing machines more efficiently, with model size scaling logarithmically in a space bound rather than a time bound. We empirically test predictions made by our results on a Sudoku reasoning task and find better alignment with learnability than for prior high-precision results. Our code is available at https://github.com/moritzbroe/transformer-expressivity.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: low precision
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Moritz Br\"osamle, Stephan Eckstein
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/moritzbroe/transformer-expressivity](https://github.com/moritzbroe/transformer-expressivity)
- 阅读深度：metadata
