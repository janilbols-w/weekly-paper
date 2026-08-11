---
title: "Revision or Re-Solving? Decomposing Second-Pass Gains in Multi-LLM Pipelines"
description: "Multi-LLM revision pipelines, in which a second model reviews and improves a draft produced by a first, are widely assumed to derive their gains from genuine error correction."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2604.01029) · [PDF](https://arxiv.org/pdf/2604.01029)

## 一句话摘要

Multi-LLM revision pipelines, in which a second model reviews and improves a draft produced by a first, are widely assumed to derive their gains from genuine error correction.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multi-LLM revision pipelines, in which a second model reviews and improves a draft produced by a first, are widely assumed to derive their gains from genuine error correction. We question this assumption with a controlled decomposition experiment that uses four matched conditions to separate second-pass gains into three additive components: re-solving, scaffold, and content. We evaluate this design across two model pairs on three benchmarks spanning knowledge-intensive MCQ and competitive programming. Our results show that the gains of multi-LLM revision are not monolithic, but depend on task structure, draft quality, and the type of draft information. On MCQ tasks, where the answer space is constrained and drafts provide little structural guidance, most gains are consistent with stronger-model re-solving, and directly routing queries to the stronger model can be more effective than revising a weak draft. On code generation tasks, however, two-stage prompting remains useful because even semantically null drafts can provide substantial structural scaffolding, while weak draft content can be harmful. Finally, role-reversed experiments show that strong drafts clearly benefit weak reviewers. Ultimately, our findings demonstrate that the utility of multi-LLM revision is dynamically bottlenecked by task structure and draft quality, necessitating more targeted pipeline designs rather than blanket revision strategies.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jingjie Ning, Xueqi Li, Chengyu Yu
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
