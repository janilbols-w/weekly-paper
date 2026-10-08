---
title: "ResidualQuant: KV Cache Quantization for Looped Transformers with 2-Bit Residuals"
description: "Looped Transformers improve parameter efficiency by repeatedly applying shared Transformer blocks over multiple recurrent loops, increasing computational depth without increasing the parameter count."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.10381) · [PDF](https://arxiv.org/pdf/2610.10381)

## 一句话摘要

Looped Transformers improve parameter efficiency by repeatedly applying shared Transformer blocks over multiple recurrent loops, increasing computational depth without increasing the parameter count.

## 为什么值得关注

待编辑增强。

## 摘要原文

Looped Transformers improve parameter efficiency by repeatedly applying shared Transformer blocks over multiple recurrent loops, increasing computational depth without increasing the parameter count. However, KV cache memory still scales with the number of loops, becoming a key memory bottleneck that limits batch size and inference throughput. KV cache quantization can alleviate this bottleneck, but existing methods often suffer substantial accuracy degradation at aggressive low-precision regimes. We observe that looped Transformers offer a unique opportunity: KV states across loops are highly similar. Based on this observation, we propose ResidualQuant, which uses the final-loop KV states as a reference and represents the remaining loops with low-precision residuals. Our method further combines least-square scaling and rotations applied to the residuals, as well as loop-wise mixed precision, to enable accurate quantization down to INT2 while retaining efficient reconstruction. Across multiple looped Transformer models and mathematical reasoning and code generation benchmarks, ResidualQuant consistently improves the accuracy-memory tradeoff over state-of-the-art rotation-based KV quantization. In particular, our method retains accuracy close to BF16 under mixed-precision settings while reducing theoretical KV storage by 80.7%, achieving up to 13.0% higher accuracy than the rotation-based baseline at the same memory budget. On an RTX 5090, the reduced KV memory traffic improves fixed-batch decode throughput by up to 2.73x, while the smaller memory footprint enables up to 2x larger batches, improving peak throughput by up to 4.15x.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: mixed precision, quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Heejun Kim, Junyoung Lee, SangLyul Cho, Dongsu Han, Insu Han, Sehoon Kim
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
