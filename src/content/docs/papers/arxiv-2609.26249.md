---
title: "PACE-dLLM: Elastic Block Decoding via Confidence Cliff Estimation for Diffusion Language Models"
description: "Diffusion language models (dLLMs), such as LLaDA and Dream, have become competitive with autoregressive (AR) LLMs in generation quality while supporting native parallel decoding."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.26249) · [PDF](https://arxiv.org/pdf/2609.26249)

## 一句话摘要

Diffusion language models (dLLMs), such as LLaDA and Dream, have become competitive with autoregressive (AR) LLMs in generation quality while supporting native parallel decoding.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion language models (dLLMs), such as LLaDA and Dream, have become competitive with autoregressive (AR) LLMs in generation quality while supporting native parallel decoding. A standard acceleration strategy is block-wise decoding, where each forward pass predicts a block of length B and commits high-confidence tokens. However, B couples two distinct decisions: the look-ahead horizon and the number of tokens to commit. Existing accelerators address this limitation through indirect heuristics, such as volatility tracking, delimiter detection, and learned scoring. In contrast, we show that the required information is already encoded in the model's own per-step confidence: in-window confidence typically follows a context-dependent cliff, whose saturation point directly identifies the appropriate look-ahead horizon. We propose PACE-dLLM, which fits this parametric cliff in closed form at each step, sets the next horizon by its saturation point, and uses an independent confidence threshold for token commitment. Under a saturated-yield abstraction, we show that the cliff-anchored horizon is the smallest horizon attaining maximal useful per-pass yield: fixed horizons that undershoot it incur a worse asymptotic NFE rate, while overshooting adds no useful yield. On four reasoning and code benchmarks, PACE-dLLM achieves the best average accuracy on both open-source dLLM backbones, with average wall-clock speedups of 5.23x on LLaDA and 3.06x on Dream (up to 8.52x on math) over the unaccelerated semi-AR baseline, advancing the quality-throughput Pareto frontier.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: parallel decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Xiaocheng Lu, Shuhan Guo, Ziyue Ma, Jie Zhang, Jian Liu, Jingcai Guo, Haoxuan Che, Song Guo
- 发布：2026-09-23；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
