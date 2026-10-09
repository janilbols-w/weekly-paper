---
title: "Fair-GPTQ: Bias-Aware Quantization for Large Language Models"
description: "The high memory demands of generative language models have drawn attention to quantization, which reduces memory usage by mapping model weights to lower-precision integers."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2509.15206) · [PDF](https://arxiv.org/pdf/2509.15206)

## 一句话摘要

The high memory demands of generative language models have drawn attention to quantization, which reduces memory usage by mapping model weights to lower-precision integers.

## 为什么值得关注

待编辑增强。

## 摘要原文

The high memory demands of generative language models have drawn attention to quantization, which reduces memory usage by mapping model weights to lower-precision integers. However, recent empirical studies show that, while efficient, quantization can increase the likelihood of generating biased outputs and degrade performance on fairness benchmarks. In this work, we draw new links between quantization and model fairness by adding explicit group-fairness constraints to the quantization objective and introduce Fair-GPTQ, the first quantization method explicitly designed to reduce unfairness in large language models. The added constraints guide the learning of the rounding operation toward less-biased text generation for protected groups. Specifically, we focus on stereotype generation involving occupational bias and discriminatory language spanning gender, race, and religion. Fair-GPTQ has minimal impact on performance, preserving at least 90% of baseline accuracy on zero-shot benchmarks, reduces unfairness relative to a half-precision model, and retains the memory and speed benefits of 4-bit quantization.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Irina Proskurina, Guillaume Metzler, Julien Velcin
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
