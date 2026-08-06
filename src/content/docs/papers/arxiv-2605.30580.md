---
title: "Speculative Decoding and the Curse of Multilinguality"
description: "Speculative decoding is a popular technique for large language model (LLM) inference, enabling faster generation by drafting multiple tokens with a smaller draft model."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2605.30580) · [PDF](https://arxiv.org/pdf/2605.30580)

## 一句话摘要

Speculative decoding is a popular technique for large language model (LLM) inference, enabling faster generation by drafting multiple tokens with a smaller draft model.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding is a popular technique for large language model (LLM) inference, enabling faster generation by drafting multiple tokens with a smaller draft model. However, the effectiveness of speculative decoding has mainly been studied for English. Motivated by the curse of multilinguality, we hypothesize that speculative decoding is far less effective for low-resource languages due to the limited multilingual capacities of smaller models. We test eleven languages under a standard speculative decoding setup and find strong evidence for our hypothesis. Next, we try to improve the multilingual capabilities of the smaller draft model via distillation from the larger model. We find, though, that distillation generalizes poorly across tasks in the same language, and we argue that assembling a task-agnostic, fully representative dataset is infeasible for low-resource languages. Finally, we propose weaker n-gram models as draft models; these provide moderate speed-ups due to their minuscule inference cost.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Nirajan Paudel, Michael Ginn, Luc De Nardi, Alexis Palmer
- 发布：2026-08-05；更新：2026-08-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
