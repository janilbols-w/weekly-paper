---
title: "SemMask: Semantic-Prioritized Progressive Masking for Diffusion Language Models"
description: "Diffusion Language Models (DLMs) are designed to enable globally parallel generation."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2611.19560) · [PDF](https://arxiv.org/pdf/2611.19560)

## 一句话摘要

Diffusion Language Models (DLMs) are designed to enable globally parallel generation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion Language Models (DLMs) are designed to enable globally parallel generation. However, in practice, they often exhibit pseudo-autoregressive behavior and a function-word-first bias, which undermines their performance on tasks such as text writing and code generation that benefit from global planning and parallel decoding. To address this, we propose SemMask, a novel fine-tuning paradigm that leverages a semantic-prioritized progressive masking strategy to encourage the model to decode high-information semantic tokens early and globally, thereby enhancing its global planning and parallel generation capabilities. Specifically, we first use the gradients of the original DLM with respect to each token to identify semantic tokens. During masking, these semantic tokens are preserved with priority, establishing a progressive generation order in which semantic tokens are decoded prior to function tokens. Meanwhile, we adjust the loss weight for semantic tokens to further reinforce their early prediction. Experimental results show that SemMask achieves quality comparable to strong autoregressive baselines on both text writing and code generation tasks, while providing superior semantic coherence. Notably, SemMask achieves higher accuracy with substantially fewer decoding steps, indicating that the early establishment of semantic structure improves the efficiency--accuracy trade-off.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qi Chen, Zifeng Cheng, Zhiwei Jiang, Qing Gu
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
