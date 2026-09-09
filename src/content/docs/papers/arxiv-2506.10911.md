---
title: "NoLoCo: No-all-reduce Low Communication Training Method for Large Models"
description: "Training large language models is generally done on clusters containing thousands of accelerators, communicating over a high-bandwidth interconnect."
---

**评分：40/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2506.10911) · [PDF](https://arxiv.org/pdf/2506.10911)

## 一句话摘要

Training large language models is generally done on clusters containing thousands of accelerators, communicating over a high-bandwidth interconnect.

## 为什么值得关注

待编辑增强。

## 摘要原文

Training large language models is generally done on clusters containing thousands of accelerators, communicating over a high-bandwidth interconnect. Scaling up these clusters is expensive and can become impractical, imposing limits on the size of models that can be trained. Several recent studies have proposed training methods that are less communication intensive, avoiding the need for compute clusters with extremely high interconnect speeds. These low communication training methods still employ a global synchronization step for model parameters, which can be too costly with a high number of participants, as the communication cost scales quadratically with group size. In this work, we propose a novel optimization method, NoLoCo, that does not explicitly synchronize all model parameters during training and does not require any collective communication. NoLoCo implicitly synchronizes model weights via a novel variant of the Nesterov momentum optimizer by partially averaging model weights within randomly selected subgroups. We provide both a theoretical convergence analysis of our optimizer and empirical results from language model training. Our method requires significantly less communication than fully sharded data parallel training and DiLoCo, a widely used low-communication baseline. Moreover, our method avoids global blocking communication, thereby reducing accelerator idle time. Our experiments show that NoLoCo is more communication-efficient than DiLoCo, improving final perplexity by up to $4\%$ and converging up to $4\times$ faster in wall-clock time across a range of worker counts, model sizes, and communication bandwidths.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jari Kolehmainen, Nikolay Blagoev, Semih Kara, John Donaghy, Christopher Nies, O\u{g}uzhan Ersoy
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
