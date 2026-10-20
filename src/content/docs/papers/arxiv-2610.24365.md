---
title: "FlashMap: Flow Map Speculative Decoding"
description: "Speculative decoding accelerates large language model (LLM) inference by using a lightweight drafter to propose a block of tokens that the target model verifies in one parallel pass."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2610.24365) · [PDF](https://arxiv.org/pdf/2610.24365)

## 一句话摘要

Speculative decoding accelerates large language model (LLM) inference by using a lightweight drafter to propose a block of tokens that the target model verifies in one parallel pass.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates large language model (LLM) inference by using a lightweight drafter to propose a block of tokens that the target model verifies in one parallel pass. Autoregressive drafters generate this block one token at a time, whereas block diffusion drafters such as DFlash generate it in one pass, making drafting faster. However, these diffusion drafters predict each token independently, ignoring dependencies between tokens in the block. We introduce FlashMap, a continuous flow drafter that conditions a flow map language model on the target model's hidden states and generates the whole block in one forward pass while capturing inter-token dependencies. On Qwen3-8B, FlashMap is faster than a matched DFlash baseline on every benchmark, with 7% higher average speedup and up to 6.1x lossless acceleration.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jeff Shen, Zhejian Zhou, Ryan Lee, Jonathan May, Shirley Ho
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
