---
title: "Quantization Degradation in Large Language Models: A Signal-Noise Perspective"
description: "Post-training quantization reduces the deployment cost of large language models, yet how severely a quantized model degrades is not determined by bit-width alone."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.08188) · [PDF](https://arxiv.org/pdf/2608.08188)

## 一句话摘要

Post-training quantization reduces the deployment cost of large language models, yet how severely a quantized model degrades is not determined by bit-width alone.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training quantization reduces the deployment cost of large language models, yet how severely a quantized model degrades is not determined by bit-width alone. We systematically study weight-only post-training quantization across bit-widths, quantization methods, model scales and downstream tasks on multiple model families. We observe that such degradation varies substantially across these factors: 4-bit quantization usually preserves performance, 2-bit often causes broad degradation, and at 3-bit, degradation becomes apparent but varies markedly with task type, quantization method and model scale. To explain this variability, we use the signal-to-noise ratio (SNR) to measure how strongly quantization perturbs full-precision representations. We trace degradation back to two linked processes: how quantization errors arise within individual modules, and how they accumulate across layers. First, a source SNR decomposition shows that newly introduced errors depend on three factors: the magnitude of the weight error, the strength of the task-specific signal, and how strongly the quantization error aligns with task-specific activations. Different factors affect these components in distinct ways. Second, a cross-layer propagation analysis shows that these errors can be attenuated, preserved, or amplified as they pass across layers, and that larger models benefit from weaker error amplification. Together, these results establish that quantization degradation is governed by how errors are introduced at the source and how they accumulate across the network.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chenxi Zhou, Pengfei Cao, Jinyu Ye, Bohan Yu, Haida Yu, Jiang Li, Jun Zhao, Kang Liu
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
