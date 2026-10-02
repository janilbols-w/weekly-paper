---
title: "LongSpark: Efficient speculative decoding with a fixed-cost parallel drafter"
description: "Speculative decoding accelerates autoregressive inference by verifying multiple draft tokens in a single target forward pass."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](http://arxiv.org/abs/2609.37029v1) · [PDF](https://arxiv.org/pdf/2609.37029v1)

## 一句话摘要

Speculative decoding accelerates autoregressive inference by verifying multiple draft tokens in a single target forward pass.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates autoregressive inference by verifying multiple draft tokens in a single target forward pass. However, as the context grows, existing state-of-the-art drafters become increasingly expensive, eroding the very efficiency advantage they are designed to provide. We argue that this scaling is unnecessary. A standalone language model must grow with its prefix because it is solely responsible for every token it produces. A drafter, by contrast, only proposes candidates; the target catches and corrects every error before any token is committed. The drafter's decoding cost can therefore be made entirely independent of the prefix length. We introduce LongSpark, a block-diffusion drafter that achieves this by extracting fixed-size, multiscale views from the target's verification pass, thereby eliminating the need for a growing persistent state. Extensive evaluations demonstrate that LongSpark achieves state-of-the-art end-to-end efficiency across multiple model scales and realistic serving conditions. Notably, it delivers the lowest time-per-output-token on long-context tasks while reducing the drafter's context state by several orders of magnitude.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hao-Yuan He, Peng-Fei Liu, Si Shen, Ming Li
- 发布：2026-09-29；更新：2026-09-29
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
