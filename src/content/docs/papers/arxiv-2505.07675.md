---
title: "Simple yet Effective Semi-supervised Knowledge Distillation from Vision-Language Models via Dual-Head Optimization"
description: "Semi-supervised learning (SSL) has emerged as a practical solution for addressing data scarcity challenges by leveraging unlabeled data."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2505.07675) · [PDF](https://arxiv.org/pdf/2505.07675)

## 一句话摘要

Semi-supervised learning (SSL) has emerged as a practical solution for addressing data scarcity challenges by leveraging unlabeled data.

## 为什么值得关注

待编辑增强。

## 摘要原文

Semi-supervised learning (SSL) has emerged as a practical solution for addressing data scarcity challenges by leveraging unlabeled data. Recently, vision-language models (VLMs), pre-trained on massive image-text pairs, have demonstrated remarkable zero-/few-shot performance that often surpasses SSL approaches due to their exceptional generalization capabilities. This gap motivates us to question: how can we effectively harness the powerful generalization capabilities of VLMs into task-specific models? Knowledge distillation (KD) offers a natural framework for transferring VLM capabilities, but we identify that it suffers from gradient conflicts between supervised and distillation losses. To address this challenge, we propose Dual-Head Optimization (DHO), which introduces dual prediction heads for each distinct signal. We observe that DHO mitigates gradient conflicts, enabling improved feature learning compared to single-head KD baselines, with practical benefits of minimal computational overhead and test-time hyperparameter tuning without retraining. Extensive experiments across 15 datasets show that DHO consistently outperforms KD baselines, often outperforming teacher models with smaller student models. DHO also achieves new state-of-the-art performance on both in-distribution ImageNet semi-supervised learning and out-of-distribution generalization across ImageNet variants. Code and model checkpoints are publicly available at https://github.com/erjui/DHO/tree/main.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Seongjae Kang, Dong Bok Lee, Hyungjoon Jang, Sung Ju Hwang
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/erjui/DHO/tree/main](https://github.com/erjui/DHO/tree/main)
- 阅读深度：metadata
