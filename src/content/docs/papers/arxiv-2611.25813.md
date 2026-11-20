---
title: "Efficient and Robust Drafting with Multi-Token Prediction"
description: "Speculative decoding has emerged as a critical technique for accelerating Large Language Model (LLM) inference by decoupling generation into a drafting phase and a parallel verification phase."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2611.25813v1) · [PDF](https://arxiv.org/pdf/2611.25813v1)

## 一句话摘要

Speculative decoding has emerged as a critical technique for accelerating Large Language Model (LLM) inference by decoupling generation into a drafting phase and a parallel verification phase.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding has emerged as a critical technique for accelerating Large Language Model (LLM) inference by decoupling generation into a drafting phase and a parallel verification phase. A crucial challenge is therefore designing a drafter that is both lightweight and accurate enough to approximate the predictions of the target model. We present a highly optimized Multi-Token Prediction (MTP) architecture that extends existing backbone LLMs to efficiently produce high-quality drafts. Built around a single shared drafting head, our approach features three core architectural optimizations: target activation injection to anchor semantic planning, zero-copy KV-cache cross-attention to bypass prefill compute and reduce memory overhead, and an efficient clustered vocabulary projection to reduce the cost of full-vocabulary decoding. Testing these improvements with the Gemma 4 model family, our G-MTP shows out-of-the-box speedups for both large server-side setups (up to 3.1$\times$) and smaller models targeting memory-constrained on-device environments (up to 2.3$\times$ on H100 and up to 2.2$\times$ on a smartphone GPU). In addition, we present parameter-efficient fine-tuning recipes for G-MTP that keep the drafter aligned with the backbone LLM under domain shift, requiring up to 1.83$\times$ fewer target forward passes than tuning only the backbone.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Filippo Galgani, Ziwei Ji, Omri Homburger, Ganesh Jawahar, Michelle Ramanovich, Ivan Korotkov, Luciano Martins, Utku Evci, Edouard Yvinec, Pooja Consul, Vivek Kumar, Tal Schuster
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
