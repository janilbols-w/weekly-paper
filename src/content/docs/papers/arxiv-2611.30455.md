---
title: "CGSpec: Consistency-Guided Speculative Decoding with Overlap-Aware Verification Scheduling for Edge-Cloud Inference"
description: "Collaborative speculative decoding accelerates large language model inference by enabling edge clients to draft tokens locally and a shared cloud model to verify them."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2611.30455) · [PDF](https://arxiv.org/pdf/2611.30455)

## 一句话摘要

Collaborative speculative decoding accelerates large language model inference by enabling edge clients to draft tokens locally and a shared cloud model to verify them.

## 为什么值得关注

待编辑增强。

## 摘要原文

Collaborative speculative decoding accelerates large language model inference by enabling edge clients to draft tokens locally and a shared cloud model to verify them. However, draft target disagreement wastes communication and verification resources, while heterogeneous client return times complicate shared verifier scheduling. We propose CGSpec, a consistency guided framework for multi client edge-cloud speculative decoding. CGSpec uses draft target distribution divergence to adapt the speculative budget and introduces a nomination and competition mechanism to construct candidate trees through global growth control and local token selection. An overlap-aware scheduler further estimates remaining verification work and client return times to prioritize requests and improve verifier utilization. We evaluate CGSpec using four model pairs and three datasets under heterogeneous network conditions. Across 24 configurations with 8 and 16 clients, CGSpec achieves the highest mean system and client throughput among the evaluated methods. Compared with current SOTA methods, it improves system throughput by 12.2\% and 10.2\%, and mean client throughput by 14.0\% and 33.0\%, respectively.

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

- 作者：Yuanbing Ouyang, Xiaoli Liu, Shirong Wei, Hao Wang, Xiang Su
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
