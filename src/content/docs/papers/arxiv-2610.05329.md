---
title: "Understanding the Weight Averaging Mechanism in LLM Training for Post-Training Quantization"
description: "Large language models (LLMs) are typically pretrained in high precision but increasingly deployed with low-precision post-training quantization (PTQ)."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.05329) · [PDF](https://arxiv.org/pdf/2610.05329)

## 一句话摘要

Large language models (LLMs) are typically pretrained in high precision but increasingly deployed with low-precision post-training quantization (PTQ).

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) are typically pretrained in high precision but increasingly deployed with low-precision post-training quantization (PTQ). Recent studies have shown that using weight averaging during pretraining can improve PTQ performance compared with learning-rate decay, suggesting that it might provide a simple way to improve the pretraining-to-quantization transition. But the mechanism behind weight averaging remains insufficiently explained. This leads to inconsistent and fragile performance gains, thereby preventing practitioners from applying such a technique confidently. As a response, we formulate weight averaging as a trade-off between retaining training progress and improving robustness under perturbation. We further derive a continuous family of averaging kernels that unifies conventional strategies and achieves the Pareto frontier between the two competing goals. Critically, a theoretical framework for performing weight averaging under PTQ is developed. It can be shown that coarser quantization is more susceptible to perturbations, whereas finer quantization could be less affected. Thus, our results could provide unified theoretical guidance for performing weight averaging under different PTQ conditions. Experiments validate both the predicted behavior and the proposed averaging strategy. Code is available at https://github.com/MOFA-LAB/weight-averaging-for-ptq.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Hanzhang Wang, Tianqi Shen, Zonglin Liu, Junze He, Difan Zou, Ziye Ma
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/MOFA-LAB/weight-averaging-for-ptq](https://github.com/MOFA-LAB/weight-averaging-for-ptq)
- 阅读深度：metadata
