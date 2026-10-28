---
title: "On the Sparsity of Direct Preference Optimization: Weight Disentanglement in the NTK Regime"
description: "Direct Preference Optimization (DPO) has been widely adopted for aligning language models with human preferences."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.37085) · [PDF](https://arxiv.org/pdf/2610.37085)

## 一句话摘要

Direct Preference Optimization (DPO) has been widely adopted for aligning language models with human preferences.

## 为什么值得关注

待编辑增强。

## 摘要原文

Direct Preference Optimization (DPO) has been widely adopted for aligning language models with human preferences. Recent empirical work has revealed that DPO induces remarkably sparse parameter updates, yet no theoretical explanation for this phenomenon has been offered. We analyze DPO's optimization dynamics under a neural tangent kernel linearization and show that the logistic structure of the DPO loss gives rise to an implicit maximum-margin bias. Building on this observation, we introduce the concept of dual sparsity: the DPO update direction is a sparse linear combination (data-level sparsity, driven by support vectors) of sparse gradient feature vectors (parameter-level sparsity, arising from gradient cancellation between preferred and dispreferred responses). We formalize this structure in our main theorem, bound the number of support pairs by a margin-dependent spectral quantity, and present a framework relating dual sparsity to weight disentanglement---a condition favorable for model merging. Experiments on GPT-2 Small and Medium and on 7--9B instruction-tuned models (Llama-3-8B, Mistral-7B, Gemma-2-9B) with the Anthropic HH-RLHF and UltraFeedback datasets confirm both sources of sparsity, and experiments on GPT-2 show that DPO reduces cross-task interference by up to $35{\times}$ compared to supervised fine-tuning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kensuke Sasaki, Issei Sato
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
