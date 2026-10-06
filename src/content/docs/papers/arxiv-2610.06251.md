---
title: "Shared Stopping Decisions Change Answers in HQQ Cache Quantization"
description: "Language-model systems batch questions for throughput, but unrelated questions should not change a target's answer when its input and numerical execution are fixed."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.06251) · [PDF](https://arxiv.org/pdf/2610.06251)

## 一句话摘要

Language-model systems batch questions for throughput, but unrelated questions should not change a target's answer when its input and numerical execution are fixed.

## 为什么值得关注

待编辑增强。

## 摘要原文

Language-model systems batch questions for throughput, but unrelated questions should not change a target's answer when its input and numerical execution are fixed. We study compression of the key and value cache, which stores attention representations reused during generation. With request-local groups, Transformers' Half-Quadratic Quantization (HQQ) backend updates compression parameters separately but uses a shared average error to decide when all updates stop. Replacing only the question batched with the target changes four-bit HQQ answers in 170/384 test comparisons across two models. Replaying the other execution's update counts reproduces its complete answer and cache fingerprints in every changed pair, in both directions. Computing the stopping mean in FP32 reduces cache differences but leaves answer changes. Native HQQ also changes confirmed numerical correctness in eight arithmetic pairs. Fixed iterations and request-local stopping remove observed companion dependence under matched controls. Request-local stopping remains sensitive to synthetic padding changes at the tensor level. Fixing the original iteration budget removes this decision path without tuning. Neither repair has an established quality advantage, and natural rebatching still changes answers. Request-independence audits must cover stopping decisions as well as quantization groups.

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

- 作者：Seunghui Jwa, Minsu Oh, Chanjun Park, Yeo-Chan Yoon
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
