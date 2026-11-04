---
title: "The Role of Quantization in Loss Spikes"
description: "Loss spikes in language model pretraining can waste substantial compute and derail otherwise healthy training runs."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.38277) · [PDF](https://arxiv.org/pdf/2610.38277)

## 一句话摘要

Loss spikes in language model pretraining can waste substantial compute and derail otherwise healthy training runs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Loss spikes in language model pretraining can waste substantial compute and derail otherwise healthy training runs. A primary driver of these instabilities is the growth and divergence of output logits in the final language modeling (LM) head. In this work, we study a particularly costly form of this instability associated with output logit growth: delayed, terminal divergences that emerge only after prolonged training, which we call time-bomb spikes. We find that these instabilities are preceded by rapidly growing quantization error in the LM head, which eventually culminates in a loss spike. Crucially, reducing numerical precision accelerates time-bomb spikes, while increasing precision improves stability. We then propose a simple yet effective mitigation that replaces AdamW on the LM head with SGD with momentum, suppressing logit growth and improving stability over long training horizons. Finally, we find that existing mitigation techniques from the literature (along with our own) all reduce quantization error, suggesting a shared numerical mechanism behind their effectiveness. Together, our results identify finite precision error as a hidden driver of time-bomb spikes and show that suppressing this error is key to stable long-horizon pretraining.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zaiqian Chen, Aditya Somasundaram, Sophie Li, Sean McLeish, John Kirchenbauer, Tom Goldstein, Micah Goldblum
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
