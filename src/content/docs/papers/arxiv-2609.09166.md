---
title: "X-CoSD: Communication-Efficient Cross-Vocabulary Collaborative Speculative Decoding"
description: "This paper investigates collaborative speculative decoding (CoSD), a distributed large language model (LLM) inference framework in which an on-device small language model (SLM) drafts candidate tokens and a server LLM verifies them."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.09166) · [PDF](https://arxiv.org/pdf/2609.09166)

## 一句话摘要

This paper investigates collaborative speculative decoding (CoSD), a distributed large language model (LLM) inference framework in which an on-device small language model (SLM) drafts candidate tokens and a server LLM verifies them.

## 为什么值得关注

待编辑增强。

## 摘要原文

This paper investigates collaborative speculative decoding (CoSD), a distributed large language model (LLM) inference framework in which an on-device small language model (SLM) drafts candidate tokens and a server LLM verifies them. Existing CoSD methods assume a shared vocabulary between the SLM and the LLM and incur substantial communication load because residual resampling requires token distribution exchange between the user device and the edge server. To address these limitations, we propose cross-vocabulary CoSD (X-CoSD), a lossless and communication-efficient CoSD framework for heterogeneous SLM-LLM vocabularies. X-CoSD is built on hybrid resampling (HR), which splits residual resampling across the common-vocabulary region on the device and the LLM-only region on the server, so that distribution transmission is required only for the common-vocabulary region. We further propose X-CoSD-E, an enhanced variant based on server resampling with device verification (SR-DV), in which the server sends only replacement candidates sampled from the server LLM and their corresponding probabilities for local verification at the device. We prove that both X-CoSD and X-CoSD-E preserve the server LLM distribution, and experiments show that they significantly improve token generation speed while maintaining generation quality comparable to that of the server LLM.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jaeduk Lee, Wan Choi
- 发布：2026-09-10；更新：2026-09-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
