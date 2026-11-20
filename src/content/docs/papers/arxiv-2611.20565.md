---
title: "Memory-Efficient Speculative Decoding with Quantized Draft KV Cache"
description: "Speculative decoding reduces generation cost, but it stores two KV caches: one for the target model and one for the draft model."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2611.20565v1) · [PDF](https://arxiv.org/pdf/2611.20565v1)

## 一句话摘要

Speculative decoding reduces generation cost, but it stores two KV caches: one for the target model and one for the draft model.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding reduces generation cost, but it stores two KV caches: one for the target model and one for the draft model. We reduce this extra memory by quantizing the draft cache. The target cache and verifier remain in BF16, so that compression cannot change the target model's final correction rule. We first study how to divide precision between keys and values. A naive per-token quantizer makes keys appear much more sensitive: splitting a 12-bit budget, K8V4 beats K4V8 in acceptance by 10.87pp. However, with grouped per-channel keys, the gap becomes -0.25pp. A controlled Qwen test confirms that changing only the key quantizer can erase or reverse the preferred bit split. Hence, following KIVI, we propose K4V4 quantization with per-channel keys and per-token values. Across six model pairs, our method reduces draft cache memory by 66.20%, and combined memory across both caches by 23.95%. Mean acceptance drops from 57.93% to 57.14%, only 1.36% relative. Overall, quantized draft caches can make speculative decoding more memory efficient; as a predictive principle for efficient AI design, key and value precision must be co-designed with the quantizer layout.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Saksham Gupta, Michael Li
- 发布：2026-11-16；更新：2026-11-16
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
