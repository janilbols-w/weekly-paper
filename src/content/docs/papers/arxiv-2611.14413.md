---
title: "Bits or permutations? Spending a fixed inference budget on weight precision or on option-order averaging in small local language models"
description: "Local language models can save memory by storing weights in fewer bits, and they can reduce sensitivity to the order of answer options by averaging a few reorderings."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.14413) · [PDF](https://arxiv.org/pdf/2611.14413)

## 一句话摘要

Local language models can save memory by storing weights in fewer bits, and they can reduce sensitivity to the order of answer options by averaging a few reorderings.

## 为什么值得关注

待编辑增强。

## 摘要原文

Local language models can save memory by storing weights in fewer bits, and they can reduce sensitivity to the order of answer options by averaging a few reorderings. We ask whether the first makes the second worse, and which is the cheaper way to spend a fixed budget. On Qwen3-0.6B and Qwen3-1.7B with simulated round-to-nearest weight quantization (8, 6, 4 and 3 bits, fp16 reference), read from the logits of the letters A to D on ARC-Easy, ARC-Challenge, MMLU and HellaSwag (300 items each), 6 bits lose no accuracy against fp16 (they score +1.8 (+1.0 to +2.5) and +0.9 (+0.3 to +1.5) points higher, which we do not explain), and 8 bits change it by -0.7 (-1.1 to -0.3) and -0.4 (-0.7 to -0.2) points. At 4 bits the answer-slot skew rises from 0.15 to 0.53 (0.6B) and from 0.07 to 0.12 (1.7B); Gaussian noise at the same weight SNR gives 0.15 and 0.37 (two draws) and 0.19 (one draw), so the control is inconclusive on whether rounding adds slot skew beyond equal-power noise. Flip rates rise but stay below an accuracy-matched baseline of independent uniform errors. Averaging four cyclic orders recovers +12.6 points at 4 bits for 0.6B (+5.3 at fp16). We price bits and passes in one machine-independent unit, weight bytes read times passes. In cost-matched pairs, extra orders beat extra bits only when the weights have 6 or more bits, and the decision table reduces to: use 6-bit weights and spend the rest of the budget on up to four orders, one pass each. Everything is simulated on two small models with the simplest quantizer; a title-level search found no earlier study of quantization together with option order.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mohammed Nayeem Khan, Logesh L, Aliyas Ahmad Misri
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
