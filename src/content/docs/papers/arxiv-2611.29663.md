---
title: "Exact on Paper: Which LLM Serving Shortcuts Flip Graded Answers, Measured Against the Noise of Reordering the Same Requests"
description: "Teams enable serving features such as prefix caching, chunked prefill and speculative decoding after checking that benchmark accuracy is unchanged, because the engine documents them as exact."
---

**评分：38/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.29663) · [PDF](https://arxiv.org/pdf/2611.29663)

## 一句话摘要

Teams enable serving features such as prefix caching, chunked prefill and speculative decoding after checking that benchmark accuracy is unchanged, because the engine documents them as exact.

## 为什么值得关注

待编辑增强。

## 摘要原文

Teams enable serving features such as prefix caching, chunked prefill and speculative decoding after checking that benchmark accuracy is unchanged, because the engine documents them as exact. Accuracy is an aggregate, so a feature can hold it while flipping which requests are answered correctly. We serve one 4B instruction model in vLLM under nine single feature configurations and five replicas of a reference configuration, grade 3,380 requests from five benchmarks in every run, and compare each candidate with a restart floor (fresh process) and a scheduling floor (same requests in a different order). With default kernels every configuration keeps accuracy within one point, and the seven exact features flip the graded outcome of 1.47% (95% CI 1.13 to 1.85) to 1.78% (1.39 to 2.20) of requests, none above the scheduling floor of 1.72%, while the FP8 KV cache flips 3.36% (2.80 to 3.96), as many as FP8 weights. With batch invariant kernels all seven exact features, speculative decoding included, reproduce the reference text on every request, while the FP8 KV cache still flips 3.91% (3.28 to 4.53) of graded outcomes. A gate that compares against a single replica pair rejected an unchanged configuration, so we recommend certifying a serving change under batch invariant kernels, where the floor is zero, or against a scheduling floor measured from at least three replicas.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sharven Rane
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
