---
title: "Farther the Shift, Sparser the Representation: Analyzing OOD Mechanisms in LLMs"
description: "In this work, we investigate how the internal representations of Large Language Models (LLMs) change with inputs of increasing difficulty."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2603.03415) · [PDF](https://arxiv.org/pdf/2603.03415)

## 一句话摘要

In this work, we investigate how the internal representations of Large Language Models (LLMs) change with inputs of increasing difficulty.

## 为什么值得关注

待编辑增强。

## 摘要原文

In this work, we investigate how the internal representations of Large Language Models (LLMs) change with inputs of increasing difficulty. Although sparsity changes may not be obvious for individual samples, dataset-level results reveal a consistent statistical trend: as task difficulty increases (e.g., harder questions, longer contexts, or more answer choices), the last hidden states of LLMs become systematically sparser. In short, \textbf{the harder the task, the sparser the representation}. This sparsity--difficulty relation is observable across diverse models and domains, suggesting that harder inputs drive more concentrated activation patterns in the last hidden state. Through a series of controlled analyses and learning-dynamics experiments, we show that representational density is a learned property of data familiarity: models develop rich, distributed representations for mastered patterns, while unfamiliar inputs default to sparser activations. Our finding is also actionable. We illustrate this with Sparsity-Guided Curriculum In-Context Learning (SG-ICL), which uses sparsity to select few-shot demonstrations matched to the query's difficulty, outperforming standard CoT and Auto-CoT baselines on MATH-500. Our study provides new insights into how LLM representations reflect task difficulty and how this signal can be leveraged for inference. The source code is available at the URL: https://github.com/MingyuJ666/sparsityLLM.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Mingyu Jin, Yutong Yin, Jingcheng Niu, Qingcheng Zeng, Wujiang Xu, Mengnan Du, Wei Cheng, Zhaoran Wang, Tianlong Chen, Dimitris N. Metaxas
- 发布：2026-11-05；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/MingyuJ666/sparsityLLM](https://github.com/MingyuJ666/sparsityLLM)
- 阅读深度：metadata
