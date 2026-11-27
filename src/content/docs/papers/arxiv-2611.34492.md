---
title: "FlyingStart: Learned Cross-Token Warm Starts for Fixed-Point Decoding in Recurrent-Depth Language Models"
description: "Recurrent-depth language models generate each token by iterating a shared block of layers until its hidden state converges."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2611.34492) · [PDF](https://arxiv.org/pdf/2611.34492)

## 一句话摘要

Recurrent-depth language models generate each token by iterating a shared block of layers until its hidden state converges.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recurrent-depth language models generate each token by iterating a shared block of layers until its hidden state converges. Inference methods for these models decide when to stop the iteration, yet every token still starts from random noise and pays the full cost of converging. We show that where the iteration starts is a second, independent lever. A token's fixed point is predictable from the state at which the previous token stopped, after a learned change of coordinates, and we introduce FlyingStart, a linear warm start that is fitted in closed form on the frozen model and costs under 5% of one loop. The iteration and its stopping rule are unchanged, so the exit criterion certifies the same distance to the fixed point from any start: a better start removes loops at unchanged accuracy. On Huginn-0125, FlyingStart matches the accuracy of the strongest training-free baseline with 14--19% fewer decoding layers, raises batched throughput by 16--18% in two serving engines, and adds a further 10--14% on top of self-speculative decoding. A contraction analysis predicts the number of loops saved on all four models we study, including one where the prediction was recorded before any evaluation, and token by token on Huginn, and it identifies when a warm start pays off: the saving grows with the number of loops a model needs to converge.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Runguo Li, Dezhen Lu, Zixiang Ni
- 发布：2026-11-25；更新：2026-11-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
