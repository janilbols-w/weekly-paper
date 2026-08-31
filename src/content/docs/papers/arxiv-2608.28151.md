---
title: "Nested Byte-Level Vocabularies Are Cheap to Deploy and Expensive to Share: A Pre-Registered Negative Result"
description: "A byte-level BPE tokenizer is an ordered list of merge rules, so applying only a prefix yields a vocabulary whose token identifiers are the first rows of the full vocabulary."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2608.28151) · [PDF](https://arxiv.org/pdf/2608.28151)

## 一句话摘要

A byte-level BPE tokenizer is an ordered list of merge rules, so applying only a prefix yields a vocabulary whose token identifiers are the first rows of the full vocabulary.

## 为什么值得关注

待编辑增强。

## 摘要原文

A byte-level BPE tokenizer is an ordered list of merge rules, so applying only a prefix yields a vocabulary whose token identifiers are the first rows of the full vocabulary. This prefix nesting allows one language model to operate at several vocabulary sizes, use a control token to indicate the active size, and be deployed at any trained size by slicing its embedding and output head. We pre-registered five claims, including margins, seeds, contrasts, and a stop rule, and trained 30 models with 3.1M- and 10.6M-parameter bodies on 200M tokens each. Slicing is numerically exact: across 76 checks, a sliced model reproduces the restricted full model's logits bit for bit and removes 66% of deployed weights without changing latency. However, the shared model trails a fixed-cap specialist by 3.64% bits per byte at 32k against a 1% margin, and by 2.96% at 8k against a 2% margin. A 2x2 ablation separating the control token from output restriction finds that the token changes performance by +0.07% to +0.13%, with all intervals crossing zero, while output restriction costs +0.47% to +1.19%; the factors are substitutes rather than complements. Multi-cap training nevertheless improves robustness: under typographical noise, the same checkpoint degrades 12.5--15.4 points less in its fine mode and outperforms each fixed-cap specialist at that specialist's vocabulary size. A control with neither cap token nor output restriction is equally robust, attributing this benefit to multi-granularity training rather than conditioning. The per-cap penalty tracks each cap's share of training rows, yielding a falsifiable prediction for future work.

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

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Christos Koutsiaris
- 发布：2026-08-31；更新：2026-08-31
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
