---
title: "Softmax Reparameterization for Output-Head Quantization"
description: "Large vocabularies make output heads a substantial inference cost in small language models."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.31291) · [PDF](https://arxiv.org/pdf/2609.31291)

## 一句话摘要

Large vocabularies make output heads a substantial inference cost in small language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large vocabularies make output heads a substantial inference cost in small language models. We introduce softmax reparameterization, a post-training method that searches over functionally equivalent output heads before quantization. The method subtracts a scalar multiple of the vocabulary-row mean from every output row and selects the coefficient by validation KL. For linear-softmax heads, these shifts preserve full-precision predictions exactly and require no decoder retraining; a rank-one correction extends the construction to nonlinear logit paths. Across seven output heads and three quantizers, W4 gains are largest where baseline quantization substantially distorts predictions: test KL falls by 93% on XGLM under RTN and by 73--77% on Phi, BLOOM, and BLOOMZ under activation-weighted MSE. Heads with low baseline error change little; at W2, used as a compression stress test, benefits extend more broadly. On Phi, the gains persist under stronger GPTQ calibration; a separate untouched holdout reproduces the improvements on Phi and BLOOM. Frozen WikiText-selected coefficients also transfer without retuning to C4 and OpenWebMath. Residual analysis on Phi shows how fidelity can improve despite greater total logit error: the selected representative reduces error on likely outputs and lowers its Fisher-weighted cost. For shift-compatible heads, the shift adds no inference operation. With the decoder held in BF16, a packed W4 Phi output head reduces batch-one generation latency by 10.8%, and reparameterization preserves this speedup.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Asim Kadav, Christian Flores, Chirag Arora, Varun Kotte, Hongbo Zheng, Lan Yan, Priya Shanmugasundaram, Tracy Holloway King
- 发布：2026-09-28；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
