---
title: "LoopZip: Visual Token Compression for Efficient Looped Vision-Language Models"
description: "Looped vision-language models (VLMs) deepen computation by reusing shared layers, approaching larger models' capabilities with fewer parameters and easing the storage and deployment burden of stacking independent layers."
---

**评分：49/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2611.22728) · [PDF](https://arxiv.org/pdf/2611.22728)

## 一句话摘要

Looped vision-language models (VLMs) deepen computation by reusing shared layers, approaching larger models' capabilities with fewer parameters and easing the storage and deployment burden of stacking independent layers.

## 为什么值得关注

待编辑增强。

## 摘要原文

Looped vision-language models (VLMs) deepen computation by reusing shared layers, approaching larger models' capabilities with fewer parameters and easing the storage and deployment burden of stacking independent layers. However, repeatedly processing long visual sequences still incurs substantial compute and GPU memory costs. Visual token compression reduces these costs by shortening sequences. Existing methods mainly select original tokens directly or combine selection with aggregation. In looped models, the former may overlook changing token importance across calls and discard information needed later; the latter lack joint consideration of output changes across calls, limiting information preservation. We propose LoopZip, a training-free visual token compression algorithm addressing both issues. Visual aggregation builds a compact candidate pool before the looped backbone, and cross-invocation selection averages instruction attention from the first two existing calls of the same shared attention layer to retain tokens needed by both states. Weight-tied value correction then jointly fits shared visual-value adjustments to both pre-selection layer outputs, reducing output deviations across states. To validate LoopZip's effectiveness, we conduct extensive experiments covering two open-source looped VLMs, eleven benchmarks, and three pruning ratios. On LoopVL-1B, LoopZip retains 97.16% of the original model's performance at 50% pruning ratio and exceeds the strongest baseline by 5.36% at 87.5% pruning ratio. Across Hugging Face Transformers, vLLM, and SGLang, LoopVL-1B with LoopZip reduces peak allocated GPU memory by 58.36%-58.98% and achieves 2.01-2.47x end-to-end speedups over the original model.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Weizhong Huang, Zhicheng Liu, Yan Zhang, Fei Chao, Xiawu Zheng, Liujuan Cao
- 发布：2026-11-18；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
