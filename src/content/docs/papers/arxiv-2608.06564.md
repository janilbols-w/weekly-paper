---
title: "Which Decisions Low-Bit Quantization Breaks, and How to Predict Them"
description: "Quantization is how large language models are actually deployed, and below four bits it hurts."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.06564) · [PDF](https://arxiv.org/pdf/2608.06564)

## 一句话摘要

Quantization is how large language models are actually deployed, and below four bits it hurts.

## 为什么值得关注

待编辑增强。

## 摘要原文

Quantization is how large language models are actually deployed, and below four bits it hurts. What nobody can say is which decisions change at a given bit-width -- which matters most where a model acts rather than answers, since a tool call it declines to make is a failure no score reports. A compressed agent stops calling its tools, then loses half its safety refusals, while benchmark scores barely move. Prior work assumes the added noise has a roughly fixed size, which would make confident decisions safe. We measure the decision instead: the margin between the option a model picks and its best alternative, before and after quantization, across 16 models, three methods, and 8 down to 2 bits. Kinds of decision do not break together -- at 3 bits the decision to call a tool collapses toward inaction while the choice of which tool is untouched -- and the damage is proportional rather than fixed, the margin multiplied by a factor that collapses with bit-width (median 0.86 at 4 bits, 0.33 at 3, 0.00 at 2). Fitted against additive competitors, including one whose noise grows with the margin, no account with an additive mean wins a damaged tool or safety cell; that is the best description among those stated, not a proof of generative form. Given a condition's own constants the relation predicts flip rates on its held-out decisions to a median of 1.8 points, with calibrated per-decision probabilities (calibration error 0.004 over 131,758 predictions), and no flip was used in the fit. Borrowed constants are wrong by 18-33 points at 3 bits, so a small paired margin set measured per model is the instrument, not a way to skip measuring. It is anchored to behaviour where used: at 4 bits the most likely token over the vocabulary is one of the two options in 85% of tool items, and the 2-bit floor is where the instrument stops measuring. Nothing repairs the damage more cheaply than one more bit.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zekun Wu, Swati Dhiman, Adriano Koshiyama
- 发布：2026-08-10；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
