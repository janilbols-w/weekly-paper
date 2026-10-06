---
title: "Loopy: Low-Bit Quantization Framework for Looped Language Models"
description: "Looped language models provide a parameter-efficient way to scale iterative test-time computation by repeatedly executing a shared recurrent core."
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.05265) · [PDF](https://arxiv.org/pdf/2610.05265)

## 一句话摘要

Looped language models provide a parameter-efficient way to scale iterative test-time computation by repeatedly executing a shared recurrent core.

## 为什么值得关注

待编辑增强。

## 摘要原文

Looped language models provide a parameter-efficient way to scale iterative test-time computation by repeatedly executing a shared recurrent core. Post-training quantization (PTQ) can reduce the memory footprint and inference cost of looped language models, but errors introduced by a quantized shared core affect subsequent cores. Among PTQ methods, channel scaling and orthogonal rotations preserve the floating-point computation while producing representations with different quantization quality. We find that quantization configuration candidate rankings can change with recurrent depth, motivating configuration selection at the target deployment depth. However, evaluating every candidate over the full calibration set at this depth is costly. We therefore propose Loopy, a PTQ framework that formulates shared-core quantization through a recurrent-depth-aware objective, selecting shared low-bit representations by their final prediction loss at the target deployment depth. Channel scaling and orthogonal rotations parameterize the candidate representations. To approximately solve this selection problem efficiently, Loopy progressively allocates calibration windows to promising candidates while preserving complete target-depth execution, using only forward evaluations. Across eight settings, Loopy achieves the state-of-the-art results among different baselines. On Ouro-1.4B under W4A4, Loopy reduces LAMBADA perplexity by 36.5% relative to SpinQuant. Our code is available at https://github.com/Shameless0817/Loopy-review.git.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zeyu LI, Yipu ZHANG, Jintao Chen, Xin LI, Wei ZHANG
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Shameless0817/Loopy-review.git](https://github.com/Shameless0817/Loopy-review.git)
- 阅读深度：metadata
