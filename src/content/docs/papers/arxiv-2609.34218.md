---
title: "Loop Dropout: Regularizing Shared Updates in Looped Language Models"
description: "Looped language models separate computational depth from parameter count by repeatedly applying the same transformer block."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2609.34218) · [PDF](https://arxiv.org/pdf/2609.34218)

## 一句话摘要

Looped language models separate computational depth from parameter count by repeatedly applying the same transformer block.

## 为什么值得关注

待编辑增强。

## 摘要原文

Looped language models separate computational depth from parameter count by repeatedly applying the same transformer block. Adapting these models requires a shared update that remains effective as hidden states evolve throughout the recurrent computation. Our empirical analysis reveals a pronounced late-loop bias in standard low-rank adaptation (LoRA): the shared update provides limited adaptation at early loop positions. This imbalance motivates training shared updates under varying combinations of their applications. Randomly omitting adapter applications alone, however, does not improve task performance; it reduces expected update strength during training while leaving inference unchanged. We introduce Loop Dropout, which couples stochastic masking of adapter applications with inverse-survival rescaling to preserve expected update strength and promote effective adaptation across loops. Extensive experiments demonstrate improved mathematical reasoning across model sizes, adapter ranks and training recipes, with benefits extending to general instruction tuning and code generation. Loop Dropout outperforms existing LoRA variants and adapter regularizers, while further analysis shows stronger early-loop adaptation. Every backbone loop remains active, and inference applies the adapter at all loops using standard LoRA without additional trainable parameters or inference computation. Code is available at https://github.com/NUS-HPC-AI-Lab/loop-dropout .

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zirui Zhu, Hailun Xu, Xuanlei Zhao, Yong Liu, Yingxuan Ren, Kanchan Sarkar, Kun Xu, Yang You
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/NUS-HPC-AI-Lab/loop-dropout](https://github.com/NUS-HPC-AI-Lab/loop-dropout)
- 阅读深度：metadata
