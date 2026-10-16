---
title: "When Dynamic Scaling Fails: A Scale-State Feedback Governs Recurrent-State Quantization in Linear-Attention and SSM LLMs"
description: "Linear-attention and state-space LLMs carry long context in a fixed-size recurrent state, and quantizing that state is the natural way to cut its cost during long decode."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2610.15139v1) · [PDF](https://arxiv.org/pdf/2610.15139v1)

## 一句话摘要

Linear-attention and state-space LLMs carry long context in a fixed-size recurrent state, and quantizing that state is the natural way to cut its cost during long decode.

## 为什么值得关注

待编辑增强。

## 摘要原文

Linear-attention and state-space LLMs carry long context in a fixed-size recurrent state, and quantizing that state is the natural way to cut its cost during long decode. Unlike a weight tensor, the state is rewritten at every step, so a quantizer applied at each step sits inside the recurrence and its errors compound. INT4 that leaves synthetic recall perfectly intact at the start destroys it a thousand steps later. The mechanism is a feedback between the quantizer scale and the state it is derived from. Yoking that scale to a full-precision reference removes the resulting norm explosion entirely, yet recovers only 1.8 of the 5.4 nats lost, so numerical instability and functional degradation are separable failures. The remainder is a resolution problem that locating outliers does not solve, since every outlier-aware scheme here loses to plain persistent scaling. Allocating bits across layers does help, but under article-disjoint splits a learned allocation collapses onto the trivial rule of protecting the first few layers. Run out to 32K, group-wise INT4 is worth no more than discarding the state. Contain the scale rather than locate outliers, and report the decode horizon at which a bit-width was certified.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuhang Jiang
- 发布：2026-10-10；更新：2026-10-10
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
