---
title: "Toward System One Clinical Intelligence: Parameter-Efficient Fine-Tuning and Counterfactual Explainability of Decision Foundation Models"
description: "Automated disease classification from patient-reported symptoms requires balancing the speed of lightweight discriminative models against the contextual understanding and latency costs of autoregressive large language models (LLMs)."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2610.15029v1) · [PDF](https://arxiv.org/pdf/2610.15029v1)

## 一句话摘要

Automated disease classification from patient-reported symptoms requires balancing the speed of lightweight discriminative models against the contextual understanding and latency costs of autoregressive large language models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Automated disease classification from patient-reported symptoms requires balancing the speed of lightweight discriminative models against the contextual understanding and latency costs of autoregressive large language models (LLMs). Decision foundation models offer an alternative by mapping representations directly to candidate classes without free-form text generation. We adapt Clef-Flash, a 9-billion-parameter decision model built on a Qwen3.5 backbone, for 24-class disease classification on the Symptom2Disease benchmark. Using 4-bit quantized low-rank adaptation (QLoRA) with differential learning rates and a stratified split of 960 training and 240 test cases, the model achieves 95.42% diagnostic accuracy and a macro F1 score of 0.9551. This improves upon the reported zero-shot baselines of 61.67% for a remote API and 65.00% for a local unadapted initialization, and outperforms the ClinicalBERT baseline (90.90%). By evaluating candidate logits in a single forward pass without autoregressive decoding, inference takes under 80 milliseconds per record on a single GPU, yielding a reported 31-fold speedup over generative LLM baselines. To examine symptom-level evidence, we introduce a Leave-One-Symptom-Out (LOSO) counterfactual perturbation framework. Removing disease-defining symptom clauses in a psoriasis example reduces predicted-class confidence from 100.00% to 0.12% and shifts the prediction to impetigo with 99.59% confidence, while removing secondary systemic symptoms produces less than 0.01% change in confidence. These findings suggest that decision-based architectures can combine the linguistic capabilities of large foundation models with low-latency inference and symptom-level interpretability for clinical triage.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：S. M. Mahbub Uddin Ahmed
- 发布：2026-10-10；更新：2026-10-10
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
