---
title: "Audit at the Precision You Deploy: Quantization Reshapes a Subliminally Learned Preference"
description: "Subliminal learning allows AI models to inherit hidden preferences from seemingly unrelated training data, such as number sequences."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.00665) · [PDF](https://arxiv.org/pdf/2611.00665)

## 一句话摘要

Subliminal learning allows AI models to inherit hidden preferences from seemingly unrelated training data, such as number sequences.

## 为什么值得关注

待编辑增强。

## 摘要原文

Subliminal learning allows AI models to inherit hidden preferences from seemingly unrelated training data, such as number sequences. Safety audits may evaluate models at standard 16-bit precision, while deployments may use compressed, quantized weights. We ask whether quantization changes the expression of a subliminal preference and what drives any resulting change. To investigate, we implant a "favourite animal: panda" preference into Qwen2.5-7B-Instruct. We define its net strength as the difference in mean panda-answer probability between subliminal models and neutrally trained controls under the same quantization setting. Applying this metric across different compression levels reveals a stark contrast. While behaviour remains stable at 8 bits, 4-bit quantization triggers severe, opposing shifts depending on the quantizer. Half-Quadratic Quantization (HQQ) amplifies the preference, raising the subliminally trained model's panda probability from roughly 55% at 16 bits to 64% at 4 bits, while the controls stay near 17%. This raises the trait's net strength ~1.3 times its 16-bit value. In contrast, NormalFloat (NF4) at 4-bit suppresses it, shrinking the net strength to just ~0.3 times its 16-bit value, despite producing rounding errors of the same size to within 4%. We examine the structure of the rounding errors and find that their arrangement drives the divergence. Randomly shuffling HQQ's errors within each quantization group, without changing their magnitude, shifts the trait's net strength between 0.2 and 1.6 times its 16-bit value. Despite these opposing shifts, the underlying fine-tuning signal remains largely intact. Because a model's internal state and outward behaviour diverge so unpredictably under compression, a 16-bit audit cannot reliably bound real-world risks. Safety evaluations must test the exact quantized weights intended for deployment.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Md Rayhanul Masud, Mst Suraiya Akter Shefa
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
