---
title: "An Optical KV Cache Network for Disaggregated LLM Serving"
description: "Disaggregated LLM serving moves each request's KV cache from a prefill GPU to a decode GPU before the response begins, and a coding-agent turn often moves the KV of its whole long context."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2610.18444v1) · [PDF](https://arxiv.org/pdf/2610.18444v1)

## 一句话摘要

Disaggregated LLM serving moves each request's KV cache from a prefill GPU to a decode GPU before the response begins, and a coding-agent turn often moves the KV of its whole long context.

## 为什么值得关注

待编辑增强。

## 摘要原文

Disaggregated LLM serving moves each request's KV cache from a prefill GPU to a decode GPU before the response begins, and a coding-agent turn often moves the KV of its whole long context. Behind an oversubscribed packet fabric this transfer adds to time to first token (TTFT). An optical circuit switch (OCS) can give every transfer a full-rate circuit for less than an oversubscribed packet fabric costs, but a mechanical OCS needs tens of milliseconds to reconfigure. We hide this delay inside the prefill. A reservation scheduler commits each circuit while the prefill is still computing, so the circuit is ready when the KV is, and each GPU reaches the OCS over its own wavelength-multiplexed (WDM) optics on one fiber pair. In simulations of GPU clusters on real serving traces with measured prefill times on H100 GPUs, this optical KV cache network matches 400G packet fabrics with adaptive routing at 0.55 to 0.78 times the cost of a 2:1 fabric and tolerates the 50 ms reconfiguration delay of a 384-port mechanical OCS.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Seongwon Yoon, Shimeng Yu
- 发布：2026-10-13；更新：2026-10-13
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
