---
title: "ARK: Avoiding Routing Collisions for KV Cache Transfer in Disaggregated LLM Inference"
description: "Disaggregated LLM inference separates the prefill and decode phases across GPU pools, generating massive KV-cache transfers."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.41160) · [PDF](https://arxiv.org/pdf/2610.41160)

## 一句话摘要

Disaggregated LLM inference separates the prefill and decode phases across GPU pools, generating massive KV-cache transfers.

## 为什么值得关注

待编辑增强。

## 摘要原文

Disaggregated LLM inference separates the prefill and decode phases across GPU pools, generating massive KV-cache transfers. Because these transfers last hundreds of milliseconds to seconds, they behave as mega elephant flows that dominate link bandwidth utilization. In this regime, stateless ECMP can perform poorly: hash collisions may overload one spine link while leaving others idle, stretching transfer times by seconds. Yet this same persistence makes coordination practical. Since these flows are long-lived, even lightweight one-to-all coordination can be amortized over their lifetime. We present ARK, a distributed elephant-flow path reservation mechanism. ARK coordinates senders to choose source ports whose hashes map concurrent flows onto distinct spines, without requiring switch changes or receiver-side packet reordering. Packet-level RDMA simulations show that ARK reduces mean and P95 FCT by up to 27.3% and 34.0% under moderate load, and further reduces mean TTFT by up to 12.9%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hung-Chun Lin, Ting-Wei Hsu, Chung-En Ho, Ahmed Saeed
- 发布：2026-11-02；更新：2026-11-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
