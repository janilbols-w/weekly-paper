---
title: "Effects of Model Scale and Quantization on Social Bias and Abstention in Question Answering"
description: "The deployment of small and quantized language models in resource-constrained settings raises an important fairness question: when a compressed model produces fewer biased responses, does this reflect fairer behavior or greater abstention?"
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.29657) · [PDF](https://arxiv.org/pdf/2610.29657)

## 一句话摘要

The deployment of small and quantized language models in resource-constrained settings raises an important fairness question: when a compressed model produces fewer biased responses, does this reflect fairer behavior or greater abstention?

## 为什么值得关注

待编辑增强。

## 摘要原文

The deployment of small and quantized language models in resource-constrained settings raises an important fairness question: when a compressed model produces fewer biased responses, does this reflect fairer behavior or greater abstention? We study this problem in Question Answering (QA) using the BBQ benchmark across multiple model sizes and quantization settings from Qwen3, Gemma-3, and SmolLM2. We also examine whether the observed trends remain stable across alternative prompt formulations and when the ``Unknown'' option is removed in a forced-choice setting. Our results show that larger models achieved higher QA accuracy, but bias showed no simple scaling trend and quantization effects varied across configurations. Notably, 20 of the 26 configurations with fewer biased responses also show increased over-abstention, indicating that lower observed bias can partly reflect greater abstention. These findings show that lower observed bias can partly reflect greater abstention, and that fairness evaluation should consider biased responses, abstention, prompt formulation, and answer-option design jointly.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kuniko Paxton, Ifeoluwa Wuraola, Dhavalkumar Thakker
- 发布：2026-10-22；更新：2026-10-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
