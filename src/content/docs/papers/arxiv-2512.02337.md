---
title: "SpecPV: Improving Self-Speculative Decoding for Long-Context Generation via Partial Verification"
description: "Growing demands from tasks like code generation, deep reasoning, and long-document understanding have made long-context generation a crucial capability for large language models (LLMs)."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2512.02337) · [PDF](https://arxiv.org/pdf/2512.02337)

## 一句话摘要

Growing demands from tasks like code generation, deep reasoning, and long-document understanding have made long-context generation a crucial capability for large language models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Growing demands from tasks like code generation, deep reasoning, and long-document understanding have made long-context generation a crucial capability for large language models (LLMs). Speculative decoding is one of the most direct and effective approaches for accelerating generation. It follows a draft-verify paradigm, where a lightweight draft model proposes several candidate tokens and the target model verifies them. However, we find that as the context length grows, verification becomes the dominant bottleneck. To further accelerate speculative decoding in long-context generation, we introduce SpecPV, a self-speculative decoding approach that performs fast verification using partial key-value states (KV) and periodically applies full verification to eliminate accumulated errors. We validate SpecPV across multiple long-context benchmarks and models, including LLaMA-3.1-8B-Instruct and Qwen3-series. Experimental results show that SpecPV achieves up to 6x decoding speedup over standard autoregressive decoding with minor degradation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zhendong Tan, Xingjun Zhang, Chaoyi Hu, Junjie Peng, Kun Xia
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
