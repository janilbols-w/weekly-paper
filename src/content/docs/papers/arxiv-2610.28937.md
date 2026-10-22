---
title: "Auditing Conformal Prediction for Language Models Under Inference-Time Model Shift"
description: "Conformal prediction (CP) for language models is typically evaluated under a matched protocol, in which calibration and deployment use the same post-training inference configuration, such as quantization mode and inference temperature."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.28937) · [PDF](https://arxiv.org/pdf/2610.28937)

## 一句话摘要

Conformal prediction (CP) for language models is typically evaluated under a matched protocol, in which calibration and deployment use the same post-training inference configuration, such as quantization mode and inference temperature.

## 为什么值得关注

待编辑增强。

## 摘要原文

Conformal prediction (CP) for language models is typically evaluated under a matched protocol, in which calibration and deployment use the same post-training inference configuration, such as quantization mode and inference temperature. In deployment, these choices often differ from those used at calibration to meet memory or throughput constraints or serving policies. We argue that this exposes a limitation in current CP evaluation protocols for language models. We formalize the underlying phenomenon as inference-time model shift: a change in the conformal score distribution induced by inference configuration rather than by the input--label distribution, and theoretically characterize how it breaks split-conformal exchangeability even when the task distribution and trained model are unchanged. We then evaluate its consequences across 8 language models, 4 finite-label benchmarks, and 12 inference configurations. We find that matched evaluation can substantially overstate deployment-time coverage, and that the effect is heterogeneous across models and datasets. We argue that inference configuration should be reported as a first-class experimental axis in CP evaluations for language-model systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 15 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Achref Doula, Max M\"uhlh\"auser
- 发布：2026-10-22；更新：2026-10-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
