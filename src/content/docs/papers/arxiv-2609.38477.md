---
title: "Security-Enhanced Seed-Based Weight Quantization for Large Language Models"
description: "Large language models (LLMs) incur substantial storage, memory-bandwidth and energy costs, motivating compact weight representations."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.38477) · [PDF](https://arxiv.org/pdf/2609.38477)

## 一句话摘要

Large language models (LLMs) incur substantial storage, memory-bandwidth and energy costs, motivating compact weight representations.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) incur substantial storage, memory-bandwidth and energy costs, motivating compact weight representations. Existing seed-based compression methods reconstruct weights from compact pseudo-random representations but do not explicitly account for the non-uniform sensitivity of model weights. We introduce Seed-Q, a security-enhanced sensitivity-aware seed-based weight compression framework that uses lightweight Linear Feedback Shift Register (LFSR)-based weight generation with non-uniform bit allocation. Our approach assigns larger representation budgets to sensitive weights while aggressively compressing less sensitive regions. Importantly, this non-uniform allocation requires no side-information: the decoder deterministically reconstructs the bit-allocation schedule, with no rung depending on the decoded weights, eliminating the need to store per-block metadata or use calibration data while preserving the baseline coding rate. Experiments across diverse LLMs show that Seed-Q matches 4-bit perplexity of SeedLM with fewer bits, while at the same 4 bits/weight it reduces both perplexity degradation and zero-shot accuracy loss relative to SeedLM. We also show that Seed-Q simultaneously achieves high security against bit-flip attacks on model parameters, as bit corruption affects multiple reconstructed weights, greatly amplifying its impact and making it easier to detect. We further implement Seed-Q in an ASIC-based accelerator and demonstrate modest hardware overhead compared to prior seed-based approaches.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qiuyu Ren, Sudipta Paria, Aritra Dasgupta, Swarup Bhunia
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
