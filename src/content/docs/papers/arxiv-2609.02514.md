---
title: "AceSpec: An Asymmetric Edge-Cloud Collaborative Framework for Communication-Efficient LLM Inference"
description: "Deploying Large Language Models (LLMs) on edge devices typically relies on model compression or split inference."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.02514) · [PDF](https://arxiv.org/pdf/2609.02514)

## 一句话摘要

Deploying Large Language Models (LLMs) on edge devices typically relies on model compression or split inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deploying Large Language Models (LLMs) on edge devices typically relies on model compression or split inference. However, compression degrades reasoning capabilities, while split inference suffers from severe Wide Area Network (WAN) communication bottlenecks. Edge-cloud speculative decoding emerges as a promising alternative, leveraging an edge small model to draft tokens for cloud verification. Yet, over volatile WANs, inevitable prediction rejections trigger catastrophic pipeline stalls and network-wide rollbacks, neutralizing collaborative gains. To overcome this, we propose AceSpec, an asymmetric edge-cloud collaborative framework. AceSpec utilizes un-saturated edge compute to proactively construct a probabilistic state cache, effectively transforming network-wide pipeline flushes into $\mathcal{O}(1)$ local memory lookups. To preserve bandwidth, it employs an asymmetric communication protocol that transmits minimal main-chain indices uplink and compact sparse distributions downlink. Furthermore, we introduce a network-aware, Lagrangian-optimized resource allocation strategy that dynamically maximizes the local cache hit rate. Evaluations demonstrate that AceSpec achieves up to a 3.52$\times$ throughput speedup and exhibits exceptional bandwidth immunity, sustaining near-peak inference performance even under severely constrained 50 Kbps WAN conditions.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yida Zhang, Zhiyong Gao, Shuaibing Yue, Jie Li, Rui Wang
- 发布：2026-09-02；更新：2026-09-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
