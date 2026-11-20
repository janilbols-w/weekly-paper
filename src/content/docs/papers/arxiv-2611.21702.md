---
title: "Watermark Evidence under Open-Weight LLM Modification: Exact Bounds for Low-Rank Output Watermarks"
description: "Open-weight language models can continue generating after their released weights are modified, while a watermark verifier still scores outputs against the original base and marked models."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.21702) · [PDF](https://arxiv.org/pdf/2611.21702)

## 一句话摘要

Open-weight language models can continue generating after their released weights are modified, while a watermark verifier still scores outputs against the original base and marked models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Open-weight language models can continue generating after their released weights are modified, while a watermark verifier still scores outputs against the original base and marked models. We study how such modifications change the evidence available to an OpenStamp-style verifier. At each shared prefix, we represent the modification as a residual in the next-token logits. We derive an exact finite-vocabulary lower bound on the expected log-likelihood-ratio evidence under a residual-span constraint, along with a sharp span-only deviation bound. We also characterize the first-order evidence shift through a covariance term with an explicit second-order remainder, and determine the residual span needed to reach a target evidence level. For sequence-level detection, we derive an exact conditional exponential-moment bound and combine it with a supermartingale argument and a distribution-free order-statistic tolerance bound. This yields a high-confidence upper bound on miss probability after attack selection on calibration data and evaluation on independent certification continuations. In experiments with OpenStamp on Llama-2-7B and Mistral-7B-v0.3, INT8 quantization and 30% pruning retain test true-positive rates of 85.6-94.8%, while 500-step LoRA fine-tuning lowers them to 28.8% and 11.6%. The covariance prediction tracks the measured mean LoRA evidence drift on both models, with no remainder-bound violations across 160,000 test prefixes. Additionally, we observe zero false positives among 500 base-model continuations per model. Through these theoretical and empirical results, the current research provides a better understanding of watermark robustness to model-editing/tuning attacks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Prashant Shekhar, Dumindu Samaraweera, Caroline Howard
- 发布：2026-11-16；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
