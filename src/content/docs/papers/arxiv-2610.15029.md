---
title: "Is a 9B Decision Foundation Model Needed for Symptom-to-Disease Classification? Fine-Tuning Clef-Flash Against TF-IDF Baselines"
description: "Disease classification from patient-reported symptom descriptions is usually approached with lightweight discriminative models or with autoregressive large language models (LLMs), which understand language broadly but generate text token by token and require output parsing."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.15029) · [PDF](https://arxiv.org/pdf/2610.15029)

## 一句话摘要

Disease classification from patient-reported symptom descriptions is usually approached with lightweight discriminative models or with autoregressive large language models (LLMs), which understand language broadly but generate text token by token and require output parsing.

## 为什么值得关注

待编辑增强。

## 摘要原文

Disease classification from patient-reported symptom descriptions is usually approached with lightweight discriminative models or with autoregressive large language models (LLMs), which understand language broadly but generate text token by token and require output parsing. We study decision foundation models, which score a closed set of candidate labels in a single forward pass without generating text. We adapt Clef-Flash, a 9-billion parameter decision model built on a Qwen3.5 backbone, to the 24-class Symptom2Disease benchmark using 4-bit quantized low-rank adaptation (QLoRA) on a stratified split of 960 training and 240 test cases. The fine-tuned model reaches 95.42% accuracy (95% CI 91.98-97.42%) and a macro F1 of 0.9551, up from 65.00% for the unadapted weights (62.92% through the remote API). However, TF-IDF linear SVM and logistic regression baselines trained on the same split reach 98.75% (95% CI 96.39-99.57%) with sub-millisecond CPU inference, so on this benchmark the fine-tuned model offers no accuracy advantage over a well-tuned linear classifier. A Leave-One-Symptom-Out clause-ablation analysis of four illustrative narratives shows predictions depending on distinguishing clauses: in a psoriasis example, removing the clause describing silvery scales lowers the predicted probability from above 99.99% to 0.12% and shifts the prediction to impetigo, while removing other clauses changes it by less than 0.001 percentage points. Decision architectures deliver structured, single-pass predictions from large language backbones, but short, lexically distinctive benchmarks such as Symptom2Disease cannot show an advantage over simple baselines; validation on longer, real clinical text and clinician review are needed.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：S. M. Mahbub Uddin Ahmed
- 发布：2026-10-10；更新：2026-10-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
