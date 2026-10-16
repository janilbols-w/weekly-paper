---
title: "HyCo: Hybrid Drafting for Cost-Efficient Mobile-Cloud Speculative Decoding"
description: "Device-cloud speculative decoding reduces server computation, but growing a deep draft tree with a small language model (SLM) requires repeated passes on a mobile neural processing unit (NPU)."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2610.21436) · [PDF](https://arxiv.org/pdf/2610.21436)

## 一句话摘要

Device-cloud speculative decoding reduces server computation, but growing a deep draft tree with a small language model (SLM) requires repeated passes on a mobile neural processing unit (NPU).

## 为什么值得关注

待编辑增强。

## 摘要原文

Device-cloud speculative decoding reduces server computation, but growing a deep draft tree with a small language model (SLM) requires repeated passes on a mobile neural processing unit (NPU). We present HyCo, which assigns depth to the server model's native multi-token prediction (MTP) head, executed on the device, and alternative branches to one SLM pass. The server returns the hidden state, input embedding, and key-value entries needed by the head instead of executing its sequential steps. Quantization, a restricted vocabulary, and a 1K-token window fit both drafters to the NPU. An {\epsilon}-threshold rule additionally relaxes exact preservation of the verifier's sampling distribution. In single-client runs with a Galaxy S26 Ultra over LTE/5G, HyCo reduces server GPU time per output token relative to server-side MTP self-speculation by 38.6% on Spec-Bench and 29.2% on 32K-token summarization. With the same acceptance rule, three Spec-Bench runs per system show 9.0 percentage points more saving and 1.9x delivery speed than an SLM-only drafter. HyCo differs from Cloud+MTP by +0.2 judge-score points (paired 95% CI: -0.9 to +1.3); exploratory translation favors SpecEdge-{\epsilon}. Without relaxation, HyCo exact saves 27.7% and 11.9% on the two datasets.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Hanbin Bae, Heejin Choi, Joohyung Lee, Byoung Jin Choi, Sangjun Park, Hoon-Young Cho
- 发布：2026-10-15；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
