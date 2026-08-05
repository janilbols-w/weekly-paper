---
title: "Structured Recurrent Mixers for Massively Parallelized Sequence Generation"
description: "Over the last two decades, language modeling has experienced a shift from the use of predominantly recurrent architectures that process tokens sequentially during training and inference to non-recurrent models that process sequence elements in parallel during training, which results in greater training efficiency and stability at the expense of lower inferen"
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2605.08696) · [PDF](https://arxiv.org/pdf/2605.08696)

## 一句话摘要

Over the last two decades, language modeling has experienced a shift from the use of predominantly recurrent architectures that process tokens sequentially during training and inference to non-recurrent models that process sequence elements in parallel during training, which results in greater training efficiency and stability at the expense of lower inferen

## 为什么值得关注

待编辑增强。

## 摘要原文

Over the last two decades, language modeling has experienced a shift from the use of predominantly recurrent architectures that process tokens sequentially during training and inference to non-recurrent models that process sequence elements in parallel during training, which results in greater training efficiency and stability at the expense of lower inference throughput. Here we introduce the Structured Recurrent Mixer, an architecture that allows for algebraic conversion between a sequence parallel representation at train time and a recurrent representation at inference, notably without the need for specialized kernels or device-specific memory management. We show experimentally that this dual representation allows for greater training efficiency, higher input information capacity, and larger inference throughput and concurrency when compared to other linear complexity models. We postulate that recurrent models are poorly suited to extended sequence length scaling for information-rich inputs typical of language, but are well suited to scaling in the sample (batch) dimension due to their constant memory per sample. We provide Mojo/MAX inference implementations of SRMs exhibiting 12x the throughput and 170x the concurrency of similarly powerful Transformers inferenced on vLLM, increases characteristic of Pytorch implementations resulting in a 30\% increase in compute-constant GSM8k Pass@k. We conclude by demonstrating that SRMs are effective reinforcement learning training candidates.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: memory management
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Benjamin L. Badger
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
