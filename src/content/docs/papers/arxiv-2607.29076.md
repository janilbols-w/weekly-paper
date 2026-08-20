---
title: "Selective KV Cache Protection for Noise-Resilient LLM Inference on Analog Compute-In-Memory Systems"
description: "Analog compute-in-memory (CIM) arrays have emerged as a promising substrate for energy-efficient LLM inference, particularly for weight-stationary computations in linear layers."
---

**评分：49/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2607.29076) · [PDF](https://arxiv.org/pdf/2607.29076)

## 一句话摘要

Analog compute-in-memory (CIM) arrays have emerged as a promising substrate for energy-efficient LLM inference, particularly for weight-stationary computations in linear layers.

## 为什么值得关注

待编辑增强。

## 摘要原文

Analog compute-in-memory (CIM) arrays have emerged as a promising substrate for energy-efficient LLM inference, particularly for weight-stationary computations in linear layers. However, extending analog CIM to attention mechanisms introduces a fundamental challenge: KV cache operations demand repeated in-situ weight updates, and the resulting mismatch with the weight-stationary paradigm exposes dynamic computations to significant hardware noise, a critical problem that remains largely unexplored. In this paper, we present the first systematic study of dynamic attention computation on analog CIM arrays, revealing that initial and recent tokens exhibit disproportionate vulnerability to hardware noise. Motivated by this token-level insight, we propose a hierarchical token protection strategy that keeps sink tokens and a sliding recent-token window on a higher-precision digital path while processing the bulk KV cache on analog CIM. A co-designed scheduler combines analog programming, ownership transition, and bulk-MVM tile formation to bound digital overhead. Evaluations on nine LLMs show that our approach lowers average perplexity under analog noise from 33.91 to 11.95, close to the clean baseline of 11.06, while improving dynamic-KV programming-row utilization from 23.1\% to 91.2\%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 8 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuannuo Feng, Wenyong Zhou, Yuang Ma, Yizhe Chen, Wenshuai Yao, Yuxin Xie, Ngai Wong, Wang Kang
- 发布：2026-08-20；更新：2026-08-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
