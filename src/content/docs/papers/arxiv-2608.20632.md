---
title: "Sparse Token Routing in Efficient Transformers"
description: "Efficient-transformer research often motivates token pruning and adaptive computation with the claim that not all tokens require equal computational effort."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.20632) · [PDF](https://arxiv.org/pdf/2608.20632)

## 一句话摘要

Efficient-transformer research often motivates token pruning and adaptive computation with the claim that not all tokens require equal computational effort.

## 为什么值得关注

待编辑增强。

## 摘要原文

Efficient-transformer research often motivates token pruning and adaptive computation with the claim that not all tokens require equal computational effort. We test this claim end to end using SEWN, a two-stream Transformer that routes tokens through either lightweight or full-capacity processing using a learned gate. Across our experiments, routing introduces negligible accuracy change relative to parameter-matched baselines, while the gate's token-importance signal depends critically on how it is learned. A static lexicon-seeded prior fails a counterfactual faithfulness test on BoolQ, whereas a fully contextual gate achieves highly significant separation ($p<10^{-10}$) on both evaluated tasks without changing task accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sai Krishna Arthanari, JaeHyeong Chang, Chengzhe Sun, Siwei Lyu
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
