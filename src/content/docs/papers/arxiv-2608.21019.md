---
title: "Target-Aware Calibration Data Selection for Preserving Uncertainty in Quantized Language Models"
description: "Quantization is widely used to deploy large language models, but its effect on uncertainty behavior, such as confidence, margins, and abstention, is rarely treated as a primary objective."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.21019) · [PDF](https://arxiv.org/pdf/2608.21019)

## 一句话摘要

Quantization is widely used to deploy large language models, but its effect on uncertainty behavior, such as confidence, margins, and abstention, is rarely treated as a primary objective.

## 为什么值得关注

待编辑增强。

## 摘要原文

Quantization is widely used to deploy large language models, but its effect on uncertainty behavior, such as confidence, margins, and abstention, is rarely treated as a primary objective. We frame calibration-data selection for quantization as a target-dependent uncertainty-preservation problem. Different deployments emphasize different regions of the input distribution, yet prior work mainly optimizes accuracy-oriented compression metrics or adjusts scores after quantization. We formalize this goal with distributional and boundary preservation risks, and provide a simple mixture-mismatch argument explaining why no single calibration recipe should be expected to fit all targets. We introduce Doubt-Preserving Quantization (DPQ), a lightweight pre-quantization recipe family that uses full-precision predictions to construct target-aligned calibration mixtures of high-doubt examples and generic anchors. Across 8 language models, 9 NLP benchmarks, and 22 comparison methods, the leading fixed recipe changes with the preservation target: DPQ-r75 leads on SQuAD2 answerability-boundary preservation, while milder or single-signal variants, including DPQ-r50, confidence-only, and entropy-only, better preserve broad multiple-choice QA behavior. These results show that calibration data should be selected for the specific full-precision score behavior a deployment needs to preserve, rather than treated as a fixed quantization detail.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhen Yang, Sizai Hou, Kaiwen Zheng, Yaofang Liu, Liang He, Yixuan Chen, Kangning Cui
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
