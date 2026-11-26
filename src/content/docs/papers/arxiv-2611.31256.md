---
title: "Directly Maximizing On-policy Expected Accepted Length for Speculative Decoding"
description: "Speculative decoding accelerates large language model inference by using a lightweight draft model to propose tokens for verification by a target model."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2611.31256) · [PDF](https://arxiv.org/pdf/2611.31256)

## 一句话摘要

Speculative decoding accelerates large language model inference by using a lightweight draft model to propose tokens for verification by a target model.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates large language model inference by using a lightweight draft model to propose tokens for verification by a target model. Draft training commonly optimizes token-level distribution alignment, but this does not directly optimize the length of the accepted prefix: once a draft token is rejected, all subsequent draft tokens are discarded. We propose FreDraft, an on-policy training method that directly maximizes the expected accepted length of drafts sampled from the current draft model. This objective accounts for first-rejection truncation and induces prefix-aware credit assignment, weighting each token by its contribution to the acceptance of the current and subsequent tokens. To optimize the objective efficiently, we analytically marginalize token-level acceptance rate, using the target model's vocabulary distribution to reduce gradient variance. We further redistribute part of this distribution-level gradient into an explicit penalty for sampled tokens whose probabilities are overestimated by the draft model, while preserving the expected gradient. Experiments across multiple benchmarks and target models show that FreDraft improves accepted length and decoding speedup over strong baselines, achieving faster on-policy training convergence.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ziying Zhang, Yaqing Wang, Yong Liu, Quanming Yao
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
