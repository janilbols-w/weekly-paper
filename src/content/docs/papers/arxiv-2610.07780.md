---
title: "APEX: Speculate smarter, not deeper"
description: "Speculative decoding reduces large language model inference latency by drafting multiple tokens before target-model verification, but its effectiveness depends on both the proposal mechanism and draft depth."
---

**评分：52/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2610.07780) · [PDF](https://arxiv.org/pdf/2610.07780)

## 一句话摘要

Speculative decoding reduces large language model inference latency by drafting multiple tokens before target-model verification, but its effectiveness depends on both the proposal mechanism and draft depth.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding reduces large language model inference latency by drafting multiple tokens before target-model verification, but its effectiveness depends on both the proposal mechanism and draft depth. Fixed configurations cannot respond to changes in predictability, repetition, and acceptance during generation, so deeper drafting can increase wasted computation without proportional speedup. We introduce APEX, a learned controller that balances decoding speed and draft-token waste through request-level expert selection and block-level depth adaptation. APEX-Router selects among EAGLE-3, n-gram, and draft-model speculation for each request, while APEX-Depth adjusts draft length at each verification block using causal decoding signals and recent verifier feedback. APEX models accepted draft length as censored survival feedback, learning position-wise rejection hazards, block execution costs, and an action utility that balances throughput, accepted progress, and wasted tokens. This allows the controller to adapt speculation while retaining the target model's verification procedure. We integrate APEX into vLLM and evaluate it with Qwen3-8B across six workloads, achieving up to 5.24X speedup over autoregressive decoding. Across the aggregate evaluation, APEX-S achieves 4.27X speedup, while APEX-B achieves 3.27X speedup with a 41.0% relative reduction in wasted-token percentage compared with fixed n-gram speculation at k=16, providing distinct operating points for balancing acceleration and draft-token utilization.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 18 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Manvi Jha, Zach Zhang, Zhichao Xu, Linbo Liu, Sai Muralidhar Jayanthi, Vinayak Arannil
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
