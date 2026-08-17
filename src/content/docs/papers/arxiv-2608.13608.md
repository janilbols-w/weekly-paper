---
title: "Evaluating Agentic Learning Harness Capabilities Without Labels via the Scaling Hypothesis"
description: "Agentic \"Continual Learning Harnesses\", systems that pair an LLM with retrieval or memory to improve from feedback without retraining, have shown growing value in cybersecurity."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.13608) · [PDF](https://arxiv.org/pdf/2608.13608)

## 一句话摘要

Agentic "Continual Learning Harnesses", systems that pair an LLM with retrieval or memory to improve from feedback without retraining, have shown growing value in cybersecurity.

## 为什么值得关注

待编辑增强。

## 摘要原文

Agentic "Continual Learning Harnesses", systems that pair an LLM with retrieval or memory to improve from feedback without retraining, have shown growing value in cybersecurity. But their value is conventionally measured by gains against labeled benchmarks, an approach that often fails in operational security settings. Benchmark labels are scarce, stale, and unrepresentative, so a practitioner often cannot tell whether a given harness helps at all or which of two is better for their task. Traditional LLM-as-a-judge offers little signal because it is no stronger than the agent it evaluates, and distillation is unreliable on scarce, sporadic, and biased labels. We propose a framework for evaluating learning harnesses end-to-end without a labeled benchmark, grounded in the scaling hypothesis. A stronger teacher model provides sparsely sampled corrections to a smaller student with a continual learning harness. We score a harness by how much its student converges toward the teacher over time. Across security tasks, model families, and harness designs, we show that improvement relative to the teacher correlates with improvement relative to a held-out gold standard, validating teacher-relative lift as a proxy for true harness uplift when labels are absent. We further show that LLM-as-a-judge between similarly powered models yields no usable signal. These results suggest that a teacher-sized model can be improved through the same harness when humans provide the same kind of sparse, high-precision corrections.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Aryan Luthra, Kshitij Jain, Siddharth Arya, Bobby Filar, Anna Bertiger
- 发布：2026-08-17；更新：2026-08-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
