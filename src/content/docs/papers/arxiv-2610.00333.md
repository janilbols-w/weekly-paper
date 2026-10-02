---
title: "LEGO-OPD: Factorized Teacher Composition for Multimodal On-Policy Distillation"
description: "Multimodal on-policy distillation (OPD) aims to improve visual grounding while preserving the strong reasoning capabilities of language models."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.00333) · [PDF](https://arxiv.org/pdf/2610.00333)

## 一句话摘要

Multimodal on-policy distillation (OPD) aims to improve visual grounding while preserving the strong reasoning capabilities of language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multimodal on-policy distillation (OPD) aims to improve visual grounding while preserving the strong reasoning capabilities of language models. Recent multi-teacher approaches combine LLM and VLM teachers to provide complementary supervision. However, directly using a VLM's full predictive distribution entangles its visual grounding signal with its own language prior, preventing the grounding information from being transferred independently. Conversely, increasing the strength of visual supervision can improve perception but may overemphasize visual evidence and degrade language reasoning. To address this trade-off, we introduce LEGO-OPD, which selectively composes factors from a Language Expert and a Grounding expert into One teacher distribution for multimodal OPD. Under a generalized Bayesian formulation, the language expert provides a prior over candidate tokens, while the grounding expert contributes a visual likelihood that updates this prior, rather than transferring its complete predictive distribution. This factorized composition allows language reasoning and visual grounding to be controlled independently. We further introduce adaptive calibration to determine how strongly the visual likelihood should update the language prior at each decoding prefix. Specifically, LEGO-OPD uses the grounding expert's image-induced prediction shift as a prefix-dependent reference, preventing both insufficient and excessive visual supervision. Experiments with Qwen3 models show that LEGO-OPD consistently outperforms the evaluated single- and multi-teacher OPD baselines on both multimodal and text-only reasoning tasks. Moreover, it improves the initial student's visual perception while preserving text-only reasoning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jaeyun Shin, Hangeol Chang, Jong Chul Ye
- 发布：2026-10-02；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
