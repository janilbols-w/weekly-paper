---
title: "SCRAMJet: An Ultra Low Latency JetClass-Scale Transformer for the HL-LHC Level-1 Trigger"
description: "Level-1 Triggers at the LHC classify collisions within a few microseconds on FPGAs, where a network is a fully unrolled circuit whose cost is area rather than time."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.00086) · [PDF](https://arxiv.org/pdf/2611.00086)

## 一句话摘要

Level-1 Triggers at the LHC classify collisions within a few microseconds on FPGAs, where a network is a fully unrolled circuit whose cost is area rather than time.

## 为什么值得关注

待编辑增强。

## 摘要原文

Level-1 Triggers at the LHC classify collisions within a few microseconds on FPGAs, where a network is a fully unrolled circuit whose cost is area rather than time. We present SCRAMJet, a transformer encoder that replaces multi-head attention with a low-rank projection, trains under per-parameter learned fixed-point quantization, and compiles to Verilog with distributed arithmetic optimization. On the ten-class JetClass dataset it reaches $71.4 \pm 0.6\%$ accuracy with 0.157M multiply-accumulates, 6.1 accuracy points above the strongest published resource-constrained model at an eighth of the operations, and meets timing on a Virtex UltraScale+ VU13P at 147 ns using 25.7% of the logic. We also show that resource-aware training silently removes attention channels: one whose learned bit-width reaches zero still carries signal during training but is absent from the compiled circuit, so the loss never sees it go. We call these virtual channels, and a floor on the attention datalane that prevents them is worth 3.1 accuracy points at matched budget. Code and trained checkpoints are available at https://github.com/Aaddy-1/hgq-jetformer.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Aadeesh Sharma, Chang Sun, Lauri Laatu, Arianna Cox, Benedikt Maier, Alexander Tapper, Maria Spiropulu, Wayne Luk, Zhiqiang Que
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Aaddy-1/hgq-jetformer](https://github.com/Aaddy-1/hgq-jetformer)
- 阅读深度：metadata
