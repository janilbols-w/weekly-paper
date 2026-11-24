---
title: "Run One, Get Two: Near-Free Streaming Safety Checks for Local LLMs"
description: "Local LLM assistants decode for one user at a time, so decoding is bound by memory bandwidth and leaves compute idle."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.26975) · [PDF](https://arxiv.org/pdf/2611.26975)

## 一句话摘要

Local LLM assistants decode for one user at a time, so decoding is bound by memory bandwidth and leaves compute idle.

## 为什么值得关注

待编辑增强。

## 摘要原文

Local LLM assistants decode for one user at a time, so decoding is bound by memory bandwidth and leaves compute idle. Streaming safety checks today trade accuracy against cost. A dedicated guard model is accurate but nearly doubles the latency per token, while a hidden-state probe is cheap but less accurate. We present ToRA, an adapter that runs a second model as an extra row in the generator's decode step, sharing its weights and KV cache. Dual-row kernels read each weight once for both rows. On Qwen3-0.6B, ToRA matches or beats a dedicated streaming guard, with higher F1 on 12 of 17 benchmarks. It detects 11.8 points more unsafe responses than the probe at a similar cost, under 4% added latency per token.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Soheil Zibakhsh, Pedram Aghazadeh, Farinaz Koushanfar
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
