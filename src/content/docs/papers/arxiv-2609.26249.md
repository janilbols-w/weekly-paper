---
title: "PACE-dLLM: Elastic Block Decoding via Confidence Cliff Estimation for Diffusion Language Models"
description: "Diffusion language models (dLLMs), such as LLaDA and Dream, have become competitive with autoregressive (AR) LLMs in generation quality while supporting native parallel decoding."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.26249) · [PDF](https://arxiv.org/pdf/2609.26249)

## 一句话摘要

Diffusion language models (dLLMs), such as LLaDA and Dream, have become competitive with autoregressive (AR) LLMs in generation quality while supporting native parallel decoding.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion language models (dLLMs), such as LLaDA and Dream, have become competitive with autoregressive (AR) LLMs in generation quality while supporting native parallel decoding. A standard acceleration strategy is block-wise decoding, where each forward pass predicts a block of length B and commits high-confidence tokens. Confidence-threshold commitment adapts which tokens are accepted, but a fixed B still constrains the prediction scope. Existing horizon policies use manually chosen sizes, volatility statistics, or candidate-boundary scores. We instead use the model's own per-step confidence: in-window confidence typically follows a context-dependent cliff, providing a direct signal for adapting the look-ahead horizon. In this work, we propose PACE-dLLM, which refits this parametric cliff periodically in closed form, sets the next horizon at a shared confidence anchor, and retains confidence-threshold token commitment. Under a saturated-yield abstraction with iid, policy-independent monotone profiles, the oracle horizon is the smallest attaining maximal per-pass yield and improves the asymptotic forward-pass rate when fixed blocks undershoot it with positive probability. On four reasoning and code benchmarks across two open-source dLLM backbones, PACE-dLLM achieves the best average accuracy among the evaluated decoders on both backbones, with average throughput speedups of 5.23x on LLaDA and 3.06x on Dream (up to 8.52x on LLaDA MATH) over the unaccelerated semi-AR baseline, advancing the quality-throughput Pareto frontier.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: parallel decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Xiaocheng Lu, Shuhan Guo, Ziyue Ma, Jie Zhang, Jian Liu, Jingcai Guo, Haoxuan Che, Song Guo
- 发布：2026-09-23；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
