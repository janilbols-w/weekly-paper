---
title: "Learning to Read Out: Unembedding Dynamics in Language Model Pretraining"
description: "When does a language model acquire a capability?"
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.21025) · [PDF](https://arxiv.org/pdf/2610.21025)

## 一句话摘要

When does a language model acquire a capability?

## 为什么值得关注

待编辑增强。

## 摘要原文

When does a language model acquire a capability? Developmental studies usually answer this by tracking when models start producing the correct token. But that prediction passes through the unembedding matrix, or readout, which is itself still being learned during pretraining. We show that a model's hidden states can encode task information before its own readout expresses it, so timelines read from outputs conflate what the model encodes with what its readout expresses. To track the readout directly, we introduce parameter-trajectory crosscoding, which fits one sparse dictionary to every token's readout row at every checkpoint. Unlike crosscoders on activations, it needs only checkpoint weights. We use it to locate a narrow early window, 0.4-1.1% of the way through Pythia's pretraining, in which the readout reorganizes and WordNet word categories become decodable from its rows. By then, linear probes on the hidden states already decode task information that the model's own outputs do not yet show. To test whether such gaps depend on how fast the readout learns, we pretrain small models from scratch that differ only in the readout's learning rate. We find that raising it makes the readout develop earlier and the gap close sooner, with little effect on final loss. Together, these results imply that early in training, where many developmental transitions are dated, a behavioral date can reflect when the readout learns to express task information and not when the model learns it.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Matteo He, William F. Shen, Alex Iacob, Andrej Jovanovic, Xinchi Qiu, Nicholas D. Lane
- 发布：2026-10-14；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/hematteo/learning-to-read-out](https://github.com/hematteo/learning-to-read-out)
- 阅读深度：metadata
