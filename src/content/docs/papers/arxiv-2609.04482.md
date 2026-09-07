---
title: "Safety for Whom? Boundary-Aware Self-Distillation for Controlled LLM Safety Refusal"
description: "Safety alignment is usually posed as a topic-level question: is this subject harmful?"
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.04482) · [PDF](https://arxiv.org/pdf/2609.04482)

## 一句话摘要

Safety alignment is usually posed as a topic-level question: is this subject harmful?

## 为什么值得关注

待编辑增强。

## 摘要原文

Safety alignment is usually posed as a topic-level question: is this subject harmful? Deployments ask a narrower one. A civics tutor and a public-sector assistant may share a base model yet need different boundaries inside the same topic, refusing targeted political manipulation while still answering factual questions about the same election. We formulate this as narrow-boundary safety and introduce an offline self-generated framework combining controlled topic generation, coverage repair, in-distribution compensation data, and harmful-benign pairs for training and evaluation. Single-shot generation leaves 19.88% of prompts without accepted refusal traces, whereas escalating retries leave 0.20%. On political persuasion with Qwen3-8B, training on refusal data completed through Escalate increases target-domain refusal from 9.47% to 84.75% and reduces the mean unsafe-response rate across three broader harmfulness benchmarks from 26.26% to 0.14%, but increases XSTest over-refusal from 2.00% to 74.00%. In a separate matched comparison, replacing external responses with verified target-model responses reduces over-refusal from 15.20% to 5.20%. Boundary-pair data reduces comply-side over-refusal on held-out pairs from 32.94% to 4.16%, while harmful-side refusal decreases only from 91.88% to 87.72%. These results show that data composition controls the safety and usability trade-off, and that safety alignment should be evaluated on both sides of the intended refusal boundary.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Alejo L\'opez-\'Avila, Iker Garc\'ia-Ferrero, Jezabel Garcia, Antonio Tiene, Rom\'an Or\'us
- 发布：2026-09-07；更新：2026-09-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
