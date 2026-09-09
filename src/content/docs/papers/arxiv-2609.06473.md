---
title: "Steering Under Compression: Dose-Response, Capability Cost, and Failure Asymmetry in Quantized LLMs"
description: "Inference-time activation steering enables behavioral control of large language models without parameter modification, while post-training quantization reduces memory and compute costs for deployment."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.06473) · [PDF](https://arxiv.org/pdf/2609.06473)

## 一句话摘要

Inference-time activation steering enables behavioral control of large language models without parameter modification, while post-training quantization reduces memory and compute costs for deployment.

## 为什么值得关注

待编辑增强。

## 摘要原文

Inference-time activation steering enables behavioral control of large language models without parameter modification, while post-training quantization reduces memory and compute costs for deployment. Despite their growing convergence in practice, the interaction between these two techniques remains uncharacterized. We systematically study activation steering under weight-only quantization (INT8 and NF4) across four open-weight 7-9B models and two behavioral targets: judged sentiment and judge-free reasoning length. Using an iso-effect framework that compares capability costs at matched behavioral effect, we find that sentiment steering survives quantization intact. After correcting a GSM8K parser artifact with a uniform v2.3.1 rescore, the pooled INT8 contrast is -0.010 (90% CI [-0.026, +0.007]), descriptively Equivalent under the preregistered three-label rule, while NF4 remains Inconclusive at -0.017 ([-0.067, +0.033]). In contrast, reasoning length exhibits a surprising asymmetric dose-response: lengthening is graded but terminates in cap-runaway and collapse, while shortening is a step function with only 12-30% shortening (model-dependent) before discontinuous failure. We expose a methodological pitfall: the naive iso-effect ladder anchors on the collapse floor for floor-bounded targets, and we introduce a censored construction that restores interpretable crossings. We also quantify a substantial baseline capability shift for Mistral-NF4 (0.545 to 0.365 GSM8K at alpha=0), demonstrating that compression can dominate the steering intervention. Despite this, steering vectors remain highly collinear with their FP16 siblings (cosine similarity 0.989-0.998 for INT8, 0.945-0.990 for NF4), confirming that the behavioral direction survives quantization even when the cost structure does not. All code and data are released.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Saurav Bhandari, Benjamin Wade
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
