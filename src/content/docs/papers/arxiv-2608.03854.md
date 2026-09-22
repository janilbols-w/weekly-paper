---
title: "When Calibration Depends on the Scoring Rule: Quantized Biomedical LLM Classification"
description: "Quantized large language models can run on consumer hardware, which motivates interest in on-premises processing of sensitive data."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.03854) · [PDF](https://arxiv.org/pdf/2608.03854)

## 一句话摘要

Quantized large language models can run on consumer hardware, which motivates interest in on-premises processing of sensitive data.

## 为什么值得关注

待编辑增强。

## 摘要原文

Quantized large language models can run on consumer hardware, which motivates interest in on-premises processing of sensitive data. The reliability of their confidence estimates depends on implementation choices (prompt template, label wording, and scoring normalization) that are seldom treated as experimental variables. We evaluate three 7-billion-parameter Mistral variants (a base model, BioMistral, and an instruction-tuned checkpoint evaluated without its chat template) at FP16, INT8, and INT4 on five-class sentence classification in medical abstracts. We test two primary templates on n = 2,000 test sentences and two auxiliary templates on n = 200 validation sentences. Our central observation, made without post-hoc calibration, is that switching from summed to mean-token log-likelihood reverses which model appears better calibrated: BioMistral's mean calibration error across matched conditions nearly triples, while the instruction-tuned model's drops by more than half. Accuracy changes by at most 1.4 percentage points for these two checkpoints. Negative log-likelihood and Brier score show the same reversal. The two primary templates were selected using test-derived examples, so absolute performance with them is exploratory. Between them, prompt choice changes mean accuracy across precisions by 2.9 to 17.8 percentage points. Eight-bit quantization changes accuracy by at most 1.1 percentage points for the adapted checkpoints; four-bit quantization shows mixed but non-catastrophic effects. Post-hoc temperature scaling reduces calibration error under summed scoring but was not fitted under mean-token scoring, so whether the reversal survives per-scorer calibration is unknown. These exploratory results suggest that calibration comparisons of decoder-based classifiers should treat scoring normalization and prompt design as first-order experimental decisions.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, int8, quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Anton Rasmussen, Hong Qin
- 发布：2026-08-04；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
