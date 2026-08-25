---
title: "When Calibration Depends on the Scoring Rule: Quantized Biomedical LLM Classification"
description: "Quantized large language models enable on-premises processing of sensitive data, but their confidence estimates must be trustworthy."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.03854) · [PDF](https://arxiv.org/pdf/2608.03854)

## 一句话摘要

Quantized large language models enable on-premises processing of sensitive data, but their confidence estimates must be trustworthy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Quantized large language models enable on-premises processing of sensitive data, but their confidence estimates must be trustworthy. Reliability depends on implementation choices--prompt template, label wording, and scoring normalization--that are seldom treated as experimental variables. We evaluate three 7-billion-parameter Mistral variants (base, BioMistral, and instruction-tuned) at FP16, INT8, and INT4 on five-class sentence classification in medical abstracts. Two primary templates are evaluated on n=2,000 test sentences and two auxiliary templates on n=200 validation sentences. Because the primary templates were selected using 100 test-derived examples and a preliminary scorer later found to have a token-boundary error, results involving them are exploratory. Within this design, candidate-scoring normalization dominates apparent calibration: switching from summed to mean-token log-likelihood reverses which model appears better calibrated (BioMistral's mean calibration error nearly triples, while the instruction-tuned model's drops by more than half), yet accuracy changes by at most 1.4 percentage points for the two specialized models. Negative log-likelihood and Brier score confirm the reversal. Across the two primary templates, prompt choice changes mean accuracy by 2.9--17.8 percentage points, depending on the model. INT8 changes accuracy by at most 1.1 percentage points for the specialized models; INT4 effects are mixed but non-catastrophic. Post-hoc temperature scaling improves calibration under summed scoring but has not been validated under the alternative normalization that reverses the ranking. These exploratory results indicate that scoring normalization and prompt design should be first-order experimental decisions in calibration comparisons of decoder-based classifiers.

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

- taxonomy keywords: int4, int8, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Anton Rasmussen, Hong Qin
- 发布：2026-08-04；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
