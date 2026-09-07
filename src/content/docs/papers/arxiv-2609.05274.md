---
title: "How to Speculate about Uncertainty in Agentic Coding? A Draft-Model Gate Method"
description: "LLM agents deployed for software engineering fail expensively: they act confidently wrong, and bad actions are recognized only after costly execution and retry."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.05274) · [PDF](https://arxiv.org/pdf/2609.05274)

## 一句话摘要

LLM agents deployed for software engineering fail expensively: they act confidently wrong, and bad actions are recognized only after costly execution and retry.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM agents deployed for software engineering fail expensively: they act confidently wrong, and bad actions are recognized only after costly execution and retry. We present Speculative Uncertainty (SU), a method that recovers a predictive failure signal for a black-box agent from its output tokens alone, with no access to logits, weights, activations, or repeated sampling. Inverting speculative decoding, a small open-weight draft model scores the agent's already-generated trajectory in a single forward pass. From these speculative cross-likelihoods we extract phase-aware features by separating the reasoning and action spans, and calibrate them against a verifiable objective. SU produces a failure-likelihood score that any downstream policy, such as routing, human intervention, or extra test-time compute, can consume directly. To show the signal is actionable, we instantiate one such policy, a pre-execution veto gate, on software engineering agents Qwen3-Coder-480B and closed-source Claude 3.5 Sonnet, cutting execution error rate by 6-8 percentage points and token cost by 14-19% in deployment, transferring to out-of-distribution benchmarks without retraining, and generalizing across agent models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Konstantin Grotov, Valentin Malykh
- 发布：2026-09-07；更新：2026-09-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
