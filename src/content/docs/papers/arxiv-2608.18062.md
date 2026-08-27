---
title: "TokEval: A Tokenizer Evaluation Suite"
description: "Language model tokenizers are typically selected with minimal evaluation, despite the fact that their design choices directly impact model capabilities."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2608.18062) · [PDF](https://arxiv.org/pdf/2608.18062)

## 一句话摘要

Language model tokenizers are typically selected with minimal evaluation, despite the fact that their design choices directly impact model capabilities.

## 为什么值得关注

待编辑增强。

## 摘要原文

Language model tokenizers are typically selected with minimal evaluation, despite the fact that their design choices directly impact model capabilities. This can be partly attributed to a limited understanding of which tokenizer properties affect which aspects of downstream performance. We introduce TokEval, a framework of tokenizer evaluation metrics that goes beyond standard measures like fertility and compression rate to capture linguistically and structurally meaningful properties, e.g., UTF-8 character boundary integrity and digit place-value boundary alignment for mathematics. To validate whether these metrics are predictive of downstream model performance, we conduct controlled language model pretraining experiments, varying solely the tokenizers' training data mixture, pretokenization strategy, and training algorithm. We evaluate the resulting models on bits-per-byte (a tokenizer-agnostic version of perplexity) and several benchmarks, spanning linguistic understanding, mathematical reasoning, and code generation. Our experiments suggest that different intrinsic properties have different impacts on model abilities: information-theoretic metrics predict language modeling abilities (Spearman rho up to 0.80), while structure-sensitive metrics, such as those measuring digit and line-break handling, correlate with task accuracy. We hope TokEval enables more principled tokenizer evaluation, replacing pretraining sweeps with intrinsic measurement wherever the two agree.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Clara Meister
- 发布：2026-08-19；更新：2026-08-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
