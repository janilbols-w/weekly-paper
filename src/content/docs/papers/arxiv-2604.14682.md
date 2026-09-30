---
title: "Acceptance Dynamics Across Cognitive Domains in Speculative Decoding"
description: "Speculative decoding accelerates large language model (LLM) inference."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2604.14682) · [PDF](https://arxiv.org/pdf/2604.14682)

## 一句话摘要

Speculative decoding accelerates large language model (LLM) inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates large language model (LLM) inference. It uses a small draft model to propose a tree of future tokens. A larger target model then verifies these tokens in a single batched forward pass. Despite the growing body of work on speculative methods, the degree to which the cognitive characteristics of a task affect acceptance probability remains largely unexplored. We present an empirical study of tree-based speculative decoding acceptance dynamics. Our study spans four well-established NLP benchmark domains: code generation, mathematical reasoning, logical reasoning, and open-ended chat. For this, we use TinyLlama-1.1B as the draft model against Llama-2-7B-Chat-GPTQ as the target. Over 99,768 speculative nodes collected from 200 prompts, we derive per-domain acceptance rates, expected accepted lengths, depth-acceptance profiles, and entropy-acceptance correlations. We find that task type is a stronger predictor of acceptance than tree depth. Furthermore, only the chat domain consistently yields an expected accepted length exceeding 1.0 token per step. We also show that the entropy-acceptance correlation is consistently negative but weak across all domains (rho in [-0.20, -0.15]). Counterintuitively, chat produces the highest entropy yet the highest acceptance rate. We attribute this divergence to the lexical predictability of RLHF-aligned register. These findings have direct implications for domain-aware speculation budgets and draft-model selection strategies. Index Terms--speculative decoding, large language model inference, tree attention, draft model, acceptance probability, LLM efficiency

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Seifeldin Abdellatif
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
