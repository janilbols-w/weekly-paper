---
title: "The KL Divergence Is Never Negative, Except in PyTorch"
description: "A Kullback--Leibler (KL) divergence is never negative, yet PyTorch users have reported negative values for years, and the standard advice is to clamp them at zero."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.30835) · [PDF](https://arxiv.org/pdf/2611.30835)

## 一句话摘要

A Kullback--Leibler (KL) divergence is never negative, yet PyTorch users have reported negative values for years, and the standard advice is to clamp them at zero.

## 为什么值得关注

待编辑增强。

## 摘要原文

A Kullback--Leibler (KL) divergence is never negative, yet PyTorch users have reported negative values for years, and the standard advice is to clamp them at zero. The sign is only the visible part of a silent failure. Many machine-learning applications compare nearby distributions, where conventional KL formulas lose accuracy. On 8.5 million inputs with certified references across 18 closed-form KL families and F.kl_div, we find widespread errors in values and gradients on CPU and GPU. Among scalar families in ordinary parameter ranges, over 85% of FP32 values have at least 1% relative error near KL 10^(-7) (FP16: 10^(-3)), and about 30% become negative at smaller divergences. More precision is not the cure: evaluated one precision higher, the same formulas still leave 7--51% of FP32 values significantly wrong for 22 of 23 configurations. Stable closed-form decompositions, compensated arithmetic, and analytic gradients remove over 97% of significant errors in the working format. Strict repairs eliminate significant errors on 7.2 million scored closed-form samples and correctly round all 567 million scored F.kl_div components. The errors affect parameter fitting, Bayesian decisions, identical-start distillation (up to 97% top-1 disagreement), KL-based layer rankings in a quantized LLM, and 19--59% of GPT-2 circuit edge scores. With the repaired code they all but vanish. Code and data: https://github.com/xi-xiaoran/stablekl

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zhen Yang, Wei Tang, Chu Chen, Rui Qian, Yixuan Chen, Fan Yang, Kangning Cui
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/xi-xiaoran/stablekl](https://github.com/xi-xiaoran/stablekl)
- 阅读深度：metadata
