---
title: "Flat Loss, Evolving Features: Grokking in Modular Addition"
description: "Can a network keep learning while its training cross-entropy stays nearly flat at a positive level?"
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.22593) · [PDF](https://arxiv.org/pdf/2610.22593)

## 一句话摘要

Can a network keep learning while its training cross-entropy stays nearly flat at a positive level?

## 为什么值得关注

待编辑增强。

## 摘要原文

Can a network keep learning while its training cross-entropy stays nearly flat at a positive level? We show that it can. On modular addition, a standard testbed for grokking, ReLU networks trained with supported-Polar hidden updates, normalized output-layer updates and weight decay can keep 100% training accuracy while their hidden features change and held-out accuracy rises from zero to above 90%, at relatively flat training cross-entropy. Correct classification need not minimize cross-entropy, which still depends on prediction confidence. We prove this coexistence for one-hidden-layer networks in two finite-window theorems from constructed initializations: one gives a constant gain in the Fourier fraction of the hidden features, and the other holds at arbitrarily low positive loss, where a readout refitted on the training data generalizes before the network. Experiments from random initialization show the same coexistence on a window fixed in advance, and in deeper networks held-out accuracy also rises over post-hoc windows with a net increase in training cross-entropy. With a last-layer rate set per training fraction and head decay scaled with the prime, deeper networks at p=47 and 61 meet a criterion on post-hoc windows, fixed in advance, in nearly all fresh runs. A one-block transformer trained with the same updates and a slowly decaying output gain keeps every training pair correct at every logged checkpoint while its training cross-entropy rises and its held-out accuracy approaches one; with two blocks this holds through the held-out rise, after which training pairs begin to flip. A plateau in training loss need not be a plateau in learning. Code: https://github.com/akashkumar-d/flat-loss-evolving-features.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Akash Kumar, Karthik Sankaranarayanan
- 发布：2026-10-19；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/akashkumar-d/flat-loss-evolving-features](https://github.com/akashkumar-d/flat-loss-evolving-features)
- 阅读深度：metadata
