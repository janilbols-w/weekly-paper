---
title: "BitFair: A 12-nm Bit-Serial CNN Accelerator with Learnable Early Termination and Adaptive Bit Ordering for Ultra-Low-Power XR Vision"
description: "Extended Reality (XR) wearables require always-on perception within tight power envelopes of a few watts and motion-to-photon latency budgets below 20 ms, leaving only a few milliseconds for neural-network inference."
---

**评分：45/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2607.05445) · [PDF](https://arxiv.org/pdf/2607.05445)

## 一句话摘要

Extended Reality (XR) wearables require always-on perception within tight power envelopes of a few watts and motion-to-photon latency budgets below 20 ms, leaving only a few milliseconds for neural-network inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Extended Reality (XR) wearables require always-on perception within tight power envelopes of a few watts and motion-to-photon latency budgets below 20 ms, leaving only a few milliseconds for neural-network inference. Bit-serial computing is attractive for such energy-efficient neural network acceleration, but many existing architectures still process all bits even when ReLU sets the final output to zero. This paper presents BitFair, a software-hardware co-designed bit-serial CNN accelerator with learnable bit-level early termination and adaptive bit ordering, working under the ultra-low-power and strict latency requirements of XR applications. BitFair exploits dynamic bit-level sparsity by learning per-layer thresholds that trigger early termination when partial sums reliably predict that the final ReLU output will be zero. Furthermore, it searches for layer-wise bit orders that prioritize informative bits, maximizing early termination without sacrificing accuracy. A GlobalFoundries 12-nm FinFET implementation with a core area of 0.34 mm^2, 104 KB on-chip memory, and voltage scaling from 0.55 to 0.70 V achieves sub-millisecond latency, up to 117.0 BTOPS/W, and 0.07 pJ/SOP. On IBM DVS128 Gesture and N-MNIST, BitFair achieves 96.5% and 97.7% accuracy, respectively, while improving effective energy efficiency by 4.0-22.1x and accuracy by up to 9.2% over prior fabricated XR vision accelerators.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Ang Li, Chang Gao
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
