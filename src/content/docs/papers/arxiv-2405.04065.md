---
title: "FlashBack: Efficient Retrieval-Augmented Language Modeling for Fast Inference"
description: "Retrieval-Augmented Language Modeling (RALM) by integrating large language models (LLM) with relevant documents from an external corpus is a proven method for enabling the LLM to generate information beyond the scope of its pre-training corpus."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2405.04065) · [PDF](https://arxiv.org/pdf/2405.04065)

## 一句话摘要

Retrieval-Augmented Language Modeling (RALM) by integrating large language models (LLM) with relevant documents from an external corpus is a proven method for enabling the LLM to generate information beyond the scope of its pre-training corpus.

## 为什么值得关注

待编辑增强。

## 摘要原文

Retrieval-Augmented Language Modeling (RALM) by integrating large language models (LLM) with relevant documents from an external corpus is a proven method for enabling the LLM to generate information beyond the scope of its pre-training corpus. Previous work utilizing retrieved content by simply prepending it to the input poses a high runtime issue, which degrades the inference efficiency of the LLMs because they fail to use the Key-Value (KV) cache efficiently. In this paper, we propose FlashBack, a modular RALM designed to improve the inference efficiency of RALM with appending context pattern while maintaining decent performance after fine-tuning by Low-Rank Adaption. FlashBack appends retrieved documents at the end of the context for efficiently utilizing the KV cache instead of prepending them. And we introduce Marking Token as two special prompt tokens for marking the boundary of the appending context during fine-tuning. Our experiments on testing generation quality show that FlashBack can remain decent generation quality in perplexity. And the inference speed of FlashBack is up to $4\times$ faster than the prepending counterpart on a 7B LLM (Llama 2) in the runtime test. Via bypassing unnecessary re-computation, it demonstrates an advancement by achieving significantly faster inference speed, and this heightened efficiency will substantially reduce inferential cost.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Runheng Liu, Xingchen Xiao, Heyan Huang, Zewen Chi, Zhijing Wu
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
