---
title: "JARQ: Joint Alternating Refinement for Quantization"
description: "Group-wise post-training quantizers for large language models round weights onto a grid that is not refit to the resulting integer codes."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.38599) · [PDF](https://arxiv.org/pdf/2609.38599)

## 一句话摘要

Group-wise post-training quantizers for large language models round weights onto a grid that is not refit to the resulting integer codes.

## 为什么值得关注

待编辑增强。

## 摘要原文

Group-wise post-training quantizers for large language models round weights onto a grid that is not refit to the resulting integer codes. We show that this leaves accuracy on the table: the best grid depends on the codes, input correlations couple the errors of different groups, and useful code changes often involve many codes at once. We propose JARQ , a plug-in refinement that starts from any group-wise quantizer and alternates a joint least-squares fit of all group scales with bounded Babai proposals that move many codes of a group together on the current grid. The problem is a bilinear box-constrained mixed-integer least-squares problem; the solver is backpropagation-free, does not increase the layer-wise objective under exact scale solves, and keeps the host's bit width, groups, zero points, and inference cost. Across Llama-2, Llama-3, and Qwen models with RTN, GPTQ, OmniQuant, and AWQ hosts, JARQ lowers perplexity in 90 of 96 comparisons, cuts three-bit RTN perplexity by up to 36%, raises mean multiple-choice accuracy in 23 of 24 configurations, and improves QEP, QuaRot, and OJBKQ outputs, at under a minute per 7B block.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xinyu Wang, Sicheng Lyu, Xiao-Wen Chang
- 发布：2026-09-29；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
