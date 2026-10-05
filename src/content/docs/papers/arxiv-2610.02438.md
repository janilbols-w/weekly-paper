---
title: "Are you Synthesizing or Recalling? Evaluating LLMs on Algorithmic Code Retrieval"
description: "Large language models (LLMs) have demonstrated strong performance in code generation, where success depends on both recalling relevant algorithmic knowledge and reasoning about how to apply it."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2610.02438) · [PDF](https://arxiv.org/pdf/2610.02438)

## 一句话摘要

Large language models (LLMs) have demonstrated strong performance in code generation, where success depends on both recalling relevant algorithmic knowledge and reasoning about how to apply it.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) have demonstrated strong performance in code generation, where success depends on both recalling relevant algorithmic knowledge and reasoning about how to apply it. However, existing LLM pipelines are opaque, with no explicit separation between these two components. We argue that for well-known algorithms whose canonical implementations are widely accessible in pretraining corpora, code generation is better measured as \textit{parametric code retrieval}: reproducing a named algorithm from internalised knowledge rather than synthesizing a novel one. We introduce AlgoREval, a benchmark of 599 problems spanning classical 77 algorithms across 14 domains, 7 programming languages, and 4 graph-input representations to evaluate this capability in isolation, and assess 15 models (7B--34B parameters) in a zero-shot setting. We find substantial variation in retrieval accuracy across languages and input representations, even for widely documented algorithms and show that prompt augmentation with retrieved code snippets or structured algorithmic hints improve accuracy on complex algorithms, while SFT achieves broader language gains and GRPO achieves larger per-language gains on specific languages. Together, our results establish parametric code retrieval as a distinct, measurable capability and caution against deploying AI-generated algorithmic code without systematic validation.\footnote{Code and dataset are available at https://github.com/Nickil21/AlgoREval

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Nickil Maveli, Antonio Vergari, Shay B. Cohen
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Nickil21/AlgoREval](https://github.com/Nickil21/AlgoREval)
- 阅读深度：metadata
