---
title: "Faithfulness Is Not Free: Auditing Offline KV-Cache Quantization in Retrieval-Augmented Generation"
description: "Retrieval-augmented generation systems can precompute and store key-value caches of retrieved documents to avoid re-encoding context at every query."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.30996) · [PDF](https://arxiv.org/pdf/2608.30996)

## 一句话摘要

Retrieval-augmented generation systems can precompute and store key-value caches of retrieved documents to avoid re-encoding context at every query.

## 为什么值得关注

待编辑增强。

## 摘要原文

Retrieval-augmented generation systems can precompute and store key-value caches of retrieved documents to avoid re-encoding context at every query. Quantizing these caches further reduces storage, but no prior work asks whether compression damages faithfulness, whether responses remain grounded in the retrieved evidence. Faithfulness and accuracy are not equivalent: a model can produce a correct answer that is no longer supported by the context it was given. We evaluate Qwen2.5-7B-Instruct under INT8 and INT4 quantization on RGB and HotpotQA, measuring both accuracy and faithfulness with a hallucination detector, NLI entailment, and an LLM judge. INT8 is near-lossless across both metrics. INT4 reduces accuracy and, more critically, even among answers that remain factually correct, over 90% of faithfulness changes are negative, i.e., accuracy metrics are blind to this regression. The harm grows under noisy retrieval and with more retrieved chunks. Faithfulness must be audited before compressed caches are deployed.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, int8, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Atta Ul Asad, Ahsan Bilal, Muhammad Ali, Muhammad Haseeb, Dean F. Hougen
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
