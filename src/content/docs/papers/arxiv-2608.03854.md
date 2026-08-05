---
title: "Quantization Effects on Biomedical LLM Reliability"
description: "When decoder language models are used as classifiers, predicted class probabilities depend on implementation choices, including the prompt template, verbalizer (label-to-token mapping), and scoring rule, that are rarely treated as experimental variables."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.03854) · [PDF](https://arxiv.org/pdf/2608.03854)

## 一句话摘要

When decoder language models are used as classifiers, predicted class probabilities depend on implementation choices, including the prompt template, verbalizer (label-to-token mapping), and scoring rule, that are rarely treated as experimental variables.

## 为什么值得关注

待编辑增强。

## 摘要原文

When decoder language models are used as classifiers, predicted class probabilities depend on implementation choices, including the prompt template, verbalizer (label-to-token mapping), and scoring rule, that are rarely treated as experimental variables. We present a controlled evaluation of three Mistral-7B variants (Base, BioMistral, and Instruct) on PubMed RCT sentence classification (n=2000) under FP16, INT8, and INT4 precision using four answer-text prompt templates. Our primary finding is that the probability extraction protocol dominates apparent calibration. Switching from summed to mean token log-likelihood scoring reverses the calibration ranking between models: BioMistral average expected calibration error increases from 0.097 to 0.289, whereas Instruct decreases from 0.237 to 0.096, while accuracy changes by less than 1 percentage point for the specialized models but 4-6 percentage points for the base model. Prompt template choice produces accuracy differences of 7-24 percentage points, comparable to or larger than model-level effects. On one template, BioMistral outperforms Instruct although the overall mean favors Instruct by only 1.3 percentage points. For BioMistral and Instruct, INT8 quantization changes accuracy and F1 by only 1-2 percentage points relative to FP16, whereas the base model shows larger INT8 effects on some templates (up to +4.2 percentage points). INT4 produces heterogeneous but non-catastrophic effects. Temperature scaling reduces expected calibration error under summed scoring for both models but only for that scoring rule. A fine-tuned PubMedBERT reference achieves 82.7% accuracy but uses about 176000 labeled training examples, precluding direct comparison. These results demonstrate that prompt template design and scoring normalization are first-order experimental decisions when evaluating decoder language model calibration.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, int8, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Anton Rasmussen, Hong Qin
- 发布：2026-08-05；更新：2026-08-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
