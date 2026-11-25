---
title: "Selection Policies for Equal-Byte Mixed-Precision Quantization of Small Language Models"
description: "Can changing which matrices receive 2, 4, or 8 bits improve a small language model without increasing its parameter storage?"
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.28318) · [PDF](https://arxiv.org/pdf/2611.28318)

## 一句话摘要

Can changing which matrices receive 2, 4, or 8 bits improve a small language model without increasing its parameter storage?

## 为什么值得关注

待编辑增强。

## 摘要原文

Can changing which matrices receive 2, 4, or 8 bits improve a small language model without increasing its parameter storage? I compare two parent-selection rules in the same genetic algorithm: a binary-tournament variant and an Alternis-inspired rule. A separate baseline samples repaired random allocations without crossover or mutation. All three use the same MLX affine quantizer, byte ceiling, initialization and candidate allowance within each study. An exploratory study on Qwen3.5-2B evaluates 90 allocations per run. The main study on Qwen3-1.7B evaluates 500 distinct allocations per run over 10 paired seeds. Against uniform four-bit, tournament reduces held-out next-token negative log-likelihood (NLL) by 0.0616 on AG News and 0.0152 on IMDb on average, improving all 10 seeds on each corpus at identical parameter storage. Alternis improves five seeds and ties five on AG News; on IMDb its mean gain is near zero. Random returns uniform four-bit in every seed. The tournament representative answers 156 of 400 ARC-Challenge questions correctly versus 163 for uniform; no accuracy gain is demonstrated on this subset. The result favors this tournament variant for text prediction under the tested protocol, not for compression ratio or task accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Smit Anand
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
