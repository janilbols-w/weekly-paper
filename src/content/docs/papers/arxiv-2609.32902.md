---
title: "Linger and Lose: Knowledge Collapse in Low-Bit Language Models"
description: "Training language models with ternary weights is commonly judged by loss and downstream accuracy, which record only a modest cost relative to full precision."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.32902) · [PDF](https://arxiv.org/pdf/2609.32902)

## 一句话摘要

Training language models with ternary weights is commonly judged by loss and downstream accuracy, which record only a modest cost relative to full precision.

## 为什么值得关注

待编辑增强。

## 摘要原文

Training language models with ternary weights is commonly judged by loss and downstream accuracy, which record only a modest cost relative to full precision. We show that these metrics can conceal a much larger failure. We instead measure knowledge capacity, the factual bits stored per parameter, on synthetic biographies with known information content. We train GPT-2-style models from scratch with 2.5M to 50M parameters at five precisions. Under the standard cosine schedule, ternary models retain as little as 6% of an identically trained fp16 model's capacity. The deficit widens with model size while perplexity rises by only 1.4 to 1.6 times. Measured throughout training, these models first acquire capacity and then lose most of it. We identify this knowledge collapse as a learning-rate dwell instability. Held near $1$--$2\times10^{-4}$ with no decay, a pre-collapse model collapses within a few hundred exposures, and returning to a safe rate does not restore capacity. We then locate the collapse in the output head. It happens at a value the model can never predict. The weights there grow unchecked, while every other prediction the model makes is unchanged. We find that making the value predictable removes the collapse, regardless of which attribute carries it. A warmup-stable-decay schedule with a 10% cooldown increases ternary capacity by 2.7 times at 25M and 4.3 times at 50M. Gains are larger at lower precision. Cutting the output head's learning rate prevents failure when training from scratch. The post-training quantization methods we tested recover no measurable capacity below 4 bits. Our findings suggest judging low-precision training by retained capacity during training rather than final loss.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Prashanna Mani Paudel, Shivanand Venkanna Sheshappanavar
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
