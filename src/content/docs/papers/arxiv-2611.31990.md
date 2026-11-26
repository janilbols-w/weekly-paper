---
title: "How Much Dependency Can a Marginal Rule See? Total Correlation in Diffusion LM Parallel Decoding"
description: "A masked diffusion language model is fast because it commits several tokens per step."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2611.31990) · [PDF](https://arxiv.org/pdf/2611.31990)

## 一句话摘要

A masked diffusion language model is fast because it commits several tokens per step.

## 为什么值得关注

待编辑增强。

## 摘要原文

A masked diffusion language model is fast because it commits several tokens per step. Each token is sampled from its own marginal, so the dependency between the tokens is lost, and the size of that loss is the conditional total correlation C of the committed set. Most decoders choose the set from per-position marginals, which can bound C but cannot determine it. We ask how well they predict it. We estimate C for fixed candidate sets on four masked diffusion LMs from two families. On three of the four, the best marginal-only predictor is off by about one bit (0.74 to 1.17), 1.8 to 3.7 times less than a baseline that knows only the bound, and most of this accuracy comes from the bound itself. On a subset, our estimate ranks sets like the exact KL cost of a parallel commit, but sits a median 0.4 to 1.1 bits below it on prose and when the rest of the text is still masked. Dream-instruct is the exception, mainly on prose, where its conditionals are least self-consistent. Among six common marginal rules, pooling over the set beats gating on its weakest position in all 24 paired comparisons. The measurement needs a validated readout: Dream and LLaDA place a position's prediction at different logit indices, and the wrong index inflates an inconsistency diagnostic 14 to 41 times. We give three checks that measure the convention. Our results concern predicting C for a fixed set, not what a dependency-aware decoder gains.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: parallel decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Dovud Asadov, Rustambek Urokov, Qobiljon Toshnazarov, Abduaziz Kayumov, Mardon Hazratov, Husanboy Mansuraliyev
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
