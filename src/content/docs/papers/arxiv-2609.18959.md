---
title: "LangSelect: Cost-Aware Target-Language Routing for LLM Code Generation"
description: "LLM code-generation systems usually choose a target programming language before decoding and treat that choice as fixed."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2609.18959) · [PDF](https://arxiv.org/pdf/2609.18959)

## 一句话摘要

LLM code-generation systems usually choose a target programming language before decoding and treat that choice as fixed.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM code-generation systems usually choose a target programming language before decoding and treat that choice as fixed. We show that, for language-flexible programming tasks -- tasks where several target languages are acceptable and checkable by the same tests -- this choice is a measurable cost lever: verified implementations of the same task can differ substantially in generated-token length. We introduce LangSelect, a verification-aware router that selects the target language before generation and falls back when the first attempt fails. To separate offline routing opportunity from end-to-end behavior, we evaluate verified-solution replay, which chooses among already accepted corpus solutions, and live GPT-5 generation, which charges every generation attempt, including failures and fallbacks. On MultiLang-Bench, a 3,000-task, 8-language verified corpus, replay shows substantial language-routing headroom. In live evaluation on 450 held-out tasks, a train-split Domain heuristic baseline reduces harness-proxy tokens, which include wrapper and entrypoint overhead, by 50.3\% at 92.9\% pass after fallback, while a learned CodeBERT+metadata selector reaches the highest pass after fallback, 93.8\%, with a 3.7\% token increase. These results show that output-language routing can define a practical cost-correctness frontier for unit-test-verifiable code generation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Son Ha Xuan, Phat T. Tran-Truong, Xuan-Bach Le, Nghia Duong-Trung
- 发布：2026-09-17；更新：2026-09-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
