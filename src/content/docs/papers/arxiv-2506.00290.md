---
title: "DLM-One: Diffusion Language Models for One-Step Sequence Generation"
description: "This paper introduces DLM-One, a score-distillation-based framework for one-step sequence generation with continuous diffusion language models (DLMs)."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2506.00290) · [PDF](https://arxiv.org/pdf/2506.00290)

## 一句话摘要

This paper introduces DLM-One, a score-distillation-based framework for one-step sequence generation with continuous diffusion language models (DLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

This paper introduces DLM-One, a score-distillation-based framework for one-step sequence generation with continuous diffusion language models (DLMs). DLM-One eliminates iterative refinement by aligning the scores of a student model's outputs with the score function of a pretrained teacher DLM in the forward-diffused noisy space. We demonstrate that our framework is architecture-agnostic and robust across diverse continuous manifolds, including standard token embedding spaces and logit simplex spaces. Through experiments on multiple representative DLMs, we show that DLM-One achieves up to $\sim$2000$\times$ speedup in sampling steps and $\sim$500$\times$ in wall-clock time, while maintaining competitive performance on benchmark text generation tasks. We further analyze failure modes in language-domain diffusion distillation and propose an adversarially-regularized two-stage training scheme to prevent student degeneration. Our findings position one-step score distillation as a viable path for the efficient deployment of continuous diffusion models operating in continuous space for natural language processing.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tianqi Chen, Shujian Zhang, Mingyuan Zhou
- 发布：2026-09-03；更新：2026-09-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
