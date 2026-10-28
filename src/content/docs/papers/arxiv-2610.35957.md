---
title: "Distributed LLM Inference via Communication-Efficient Speculative Decoding"
description: "Distributed speculative decoding has emerged as a promising approach for device--server collaborative large language model (LLM) inference, but its decoding speedup is often limited by the vocabulary-scale communication overhead."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2610.35957) · [PDF](https://arxiv.org/pdf/2610.35957)

## 一句话摘要

Distributed speculative decoding has emerged as a promising approach for device--server collaborative large language model (LLM) inference, but its decoding speedup is often limited by the vocabulary-scale communication overhead.

## 为什么值得关注

待编辑增强。

## 摘要原文

Distributed speculative decoding has emerged as a promising approach for device--server collaborative large language model (LLM) inference, but its decoding speedup is often limited by the vocabulary-scale communication overhead. In existing distributed speculative decoding methods, exact rejection sampling requires transmitting full token distributions over the LLM vocabulary between the device and the server, which becomes costly in bandwidth-constrained environments. To address this issue, we propose DISCO, a communication-efficient framework for distributed speculative decoding, that eliminates vocabulary-scale distribution transfer while preserving the exact target distribution. DISCO achieves this by introducing a server-side replica of the draft small language model (SLM), which enables the server to locally obtain the draft-side distribution required for rejection sampling. As a result, DISCO exchanges only drafted token indices and scalar probability values between the device and the server. Experimental results on multiple datasets show that DISCO consistently achieves higher decoding speedup than existing distributed speculative decoding methods, particularly under stringent bandwidth constraints.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Joohyun Shin, Byeonghyeon Park, Keumseo Ryum, Joonhyuk Kang
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
