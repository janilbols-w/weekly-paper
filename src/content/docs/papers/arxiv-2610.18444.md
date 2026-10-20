---
title: "An Optical KV Cache Network for Disaggregated LLM Serving"
description: "In disaggregated LLM serving, each request's KV cache moves from a prefill GPU to a decode GPU before the response begins, and a coding-agent turn often moves the KV cache of its whole long context."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.18444) · [PDF](https://arxiv.org/pdf/2610.18444)

## 一句话摘要

In disaggregated LLM serving, each request's KV cache moves from a prefill GPU to a decode GPU before the response begins, and a coding-agent turn often moves the KV cache of its whole long context.

## 为什么值得关注

待编辑增强。

## 摘要原文

In disaggregated LLM serving, each request's KV cache moves from a prefill GPU to a decode GPU before the response begins, and a coding-agent turn often moves the KV cache of its whole long context. Behind an oversubscribed packet fabric, this transfer adds to the time to first token (TTFT). An optical circuit switch (OCS) can give every transfer a full-rate circuit for less than an oversubscribed packet fabric costs, but a mechanical OCS needs tens of milliseconds to reconfigure. We hide this delay inside the prefill. A reservation scheduler commits each circuit while the prefill is still computing, so the circuit is ready when the KV cache is, and each GPU reaches the OCS through its own wavelength-multiplexed (WDM) optics on one fiber pair. In simulations of GPU clusters on real serving traces with prefill times measured on H100 GPUs, this optical KV cache network matches 400G packet fabrics with adaptive routing at 0.55 to 0.78 times the cost of a 2:1 fabric and tolerates the 50 ms reconfiguration delay of a 384-port mechanical OCS.

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
- 发布：2026-10-13；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
