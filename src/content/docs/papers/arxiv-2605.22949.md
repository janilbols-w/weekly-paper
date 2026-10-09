---
title: "MARGIN: Runtime Confidence Calibration for Multi-Agent Foundation Model Coordination"
description: "When a coordinator compares answers from heterogeneous foundation models, self-reported confidence may have different meanings across responders and changing workloads."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2605.22949) · [PDF](https://arxiv.org/pdf/2605.22949)

## 一句话摘要

When a coordinator compares answers from heterogeneous foundation models, self-reported confidence may have different meanings across responders and changing workloads.

## 为什么值得关注

待编辑增强。

## 摘要原文

When a coordinator compares answers from heterogeneous foundation models, self-reported confidence may have different meanings across responders and changing workloads. This paper presents MARGIN (Multi-Agent Runtime Grading via Incremental Normalisation), a runtime calibration method that learns model-specific confidence corrections from observed answer outcomes without retraining the models or requiring a held-out calibration set. MARGIN tracks recent accuracy and stated confidence within confidence bands, uses their ratio to correct reported confidence, and blends sparse-band corrections toward a model-level estimate. The corrected scores weight candidate answers in a collective decision. Evaluation covers code generation, question answering, and mathematics, using an 18-model pool and a nine-model subset for distribution-shift experiments. On BigCodeBench, model-mean confidence is negatively related to accuracy; among correct/incorrect response pairs, choosing the more confident responder performs below chance. Against five online calibration baselines receiving identical feedback and retaining their learned state across each transition, MARGIN achieves lower post-shift expected calibration error than all five in two code-generation transitions and than four in a question-answering transition; the remaining question-answering comparison is inconclusive. In separate code-generation coordination experiments, calibration improves the ranking of correct responses and increases answer-selection accuracy by 4.3 and 14.0 percentage points on two of three benchmarks relative to uncalibrated confidence weighting. These results support model-specific runtime calibration for coordination under changing workloads when correctness feedback is available for the participating responders.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 15 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Joss Armstrong
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
