---
title: "From Token Changes to Task Failures: Bit Flips in a Shared KV-Cache Block"
description: "In LLM serving systems with prefix caching, each KV block of a shared system prompt is held in GPU memory as a single physical copy, which every request with that prompt reads."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.22243) · [PDF](https://arxiv.org/pdf/2611.22243)

## 一句话摘要

In LLM serving systems with prefix caching, each KV block of a shared system prompt is held in GPU memory as a single physical copy, which every request with that prompt reads.

## 为什么值得关注

待编辑增强。

## 摘要原文

In LLM serving systems with prefix caching, each KV block of a shared system prompt is held in GPU memory as a single physical copy, which every request with that prompt reads. Our earlier work measured change and showed that one bit flip in such a block changes many later responses without making them visibly degenerate. This paper extends that work by measuring how often the changed responses are wrong. Using software fault injection into vLLM serving Qwen3-8B, we flip the most significant mantissa bit or the sign bit of a value in such a block. We score responses on four tasks: code generation, short-answer questions, multiple-choice reasoning, and refusal under a policy. The fraction of changes that turned a correct response wrong depended strongly on the task: 0.023 on MBPP+ and 0.59 on held-out TriviaQA at the mantissa bit, and 0.019 and 0.60 at the sign bit. Harm fell on requests whose sampled answers are sometimes wrong, so the damage of a flip depends on how common such requests are. Harmed responses looked like ordinary errors, so a flip should be detected by checking cached blocks rather than by monitoring outputs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache, prefix caching
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuji Yamamoto, Satoshi Matsuura
- 发布：2026-11-17；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
