---
title: "Bit-Flip Attacks on Quantized Neural Networks without Knowledge of Model Parameters"
description: "We show that quantization asymmetry concentrates bit-flip vulnerability in small tensors retained at high precision."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.32128) · [PDF](https://arxiv.org/pdf/2611.32128)

## 一句话摘要

We show that quantization asymmetry concentrates bit-flip vulnerability in small tensors retained at high precision.

## 为什么值得关注

待编辑增强。

## 摘要原文

We show that quantization asymmetry concentrates bit-flip vulnerability in small tensors retained at high precision. CoarseHammer targets these tensors and accepts flips at any bit, without parameter values, gradients, or data. It remains effective under continued fine-tuning. Under ideal placement, CoarseHammer reaches chance accuracy in at least 81.5% of runs on each of ten evaluated models, including four large language models, with median successful runs requiring at most 24 flips. On simulated DRAM with 0.01 flippable bits per million, it outperforms three prior attacks on every evaluated convolutional network, succeeding in up to 83.6% of runs while they never succeed. On a real system, CoarseHammer steers heap-allocated tensors onto vulnerable frames despite address space layout randomization, without accessing the model file. With 16 templated frames, median accuracy reaches chance for all four language models and approximately chance for four convolutional networks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mahmoud Abumandour, Srinija Ramichetty, Guru Venkataramani, Alaa R. Alameldeen
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
