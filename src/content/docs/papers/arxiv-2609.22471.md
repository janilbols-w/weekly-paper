---
title: "Efficient Mixture-of-Experts with Speculative Decoding via Expert Coactivation"
description: "Mixture-of-Experts (MoE) models are increasingly deployed alongside Speculative Decoding (SD) to accelerate inference, but combining the two is challenging."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.22471) · [PDF](https://arxiv.org/pdf/2609.22471)

## 一句话摘要

Mixture-of-Experts (MoE) models are increasingly deployed alongside Speculative Decoding (SD) to accelerate inference, but combining the two is challenging.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) models are increasingly deployed alongside Speculative Decoding (SD) to accelerate inference, but combining the two is challenging. SD improves the inference speed of dense models by verifying groups of tokens in parallel. However, the inference speedup for SD with MoEs depends heavily on the number of tokens being verified. Using more verification tokens results in more experts being transferred from DRAM to the Neural Processing Unit (NPU), which increases the memory transfer cost. This negatively impacts model runtime, as memory transfer is typically the bottleneck in inference. In this work, we investigate the impact of MoE router design during training on the speed of MoEs with SD. We find that routers with high degrees of expert coactivation result in much faster runtimes, mitigating the impact of using more verification tokens. Motivated by this observation, we assess the impact of various router design choices on expert coactivation and runtime using billion-parameter transformer models. We find that combining a global load-balancing loss, shared experts, a consistency loss, and an autoregressive expert selection mechanism during training results in significantly stronger expert coactivation. This increased coactivation translates into higher overall runtime throughput: our exploration yields a model that improves throughput by 21% over MoE baselines, while maintaining on-par accuracy with the baseline MoE.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kumari Nishu, Han-Byul Kim, Santosh Chilkunda, Maxwell Horton, Arnav Kundu, Mohammad Samragh, Lauren Hannah, Mohammad Sekhavat, Nikhil Bhendawade, Manuel Ciosici, Iman Mirzadeh, Keivan Alizadeh Vahid, David Harrison, Irina Belousova, Mehrdad Farajtabar, Minsik Cho
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
