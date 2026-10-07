---
title: "SchemaFill: Efficient LLM Tool Calling via Slot-Parallel Speculative Decoding"
description: "LLM agents interact with external systems by generating structured tool calls."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2610.07086) · [PDF](https://arxiv.org/pdf/2610.07086)

## 一句话摘要

LLM agents interact with external systems by generating structured tool calls.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM agents interact with external systems by generating structured tool calls. Given a user request, conversational context, and a catalog of tool schemas, a tool-calling model must select tools and generate their arguments, potentially producing multiple calls in a single response. Standard autoregressive decoding generates these calls token by token, incurring substantial latency for requests involving multiple calls or many argument fields. The explicit argument structure offers opportunities for parallel generation, but later argument values may depend on preceding fields and calls, so independently generated values can differ from the target model's output. We present SchemaFill, a framework for efficient LLM tool calling through slot-parallel speculative decoding. SchemaFill generates future slot values concurrently as candidates, without requiring advance knowledge of the actual call sequence or argument values. Candidates spanning multiple fields and calls are concatenated for verification by the target model under the actual output prefix. Only verified tokens are committed, and the target supplies corrections when candidates disagree. This applies target verification while exploiting parallelism across slots and calls. On Glaive and BFCL, SchemaFill achieves up to a 4.05$\times$ improvement in end-to-end throughput over autoregressive decoding. Code is available at https://github.com/Czzzk/SchemaFill.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zhi-Kai Chen, Song-Yan Li, De-Chuan Zhan, Han-Jia Ye
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Czzzk/SchemaFill](https://github.com/Czzzk/SchemaFill)
- 阅读深度：metadata
