---
title: "Do Student LLMs Inherit OOD Robustness? Invariance-Weighted Distillation for Reliable Knowledge Transfer"
description: "Knowledge distillation (KD) aims to compress high-performance teacher LLMs into lightweight students."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.22566) · [PDF](https://arxiv.org/pdf/2609.22566)

## 一句话摘要

Knowledge distillation (KD) aims to compress high-performance teacher LLMs into lightweight students.

## 为什么值得关注

待编辑增强。

## 摘要原文

Knowledge distillation (KD) aims to compress high-performance teacher LLMs into lightweight students. However, distilled students often exhibit substantial performance degradation in out-of-distribution (OOD) settings, a critical gap that remains underexplored. We identify two compounding mechanisms causing OOD performance degradation: (1) data spuriousness: students can learn spurious correlations in the distillation dataset over genuine causal relationships; and (2) teacher capability: standard KD treats all samples uniformly, ignoring whether the teacher is guided by causal features or misled by spurious shortcuts on a given sample. To address these challenges, we propose Invariance-Weighted Distillation (IWD), a theoretically grounded framework that dynamically reweights training samples using an estimate of the teacher's causal reliance derived from prediction invariance across multiple synthetic environments. IWD perturbs spurious cues while preserving core semantics, assigning higher distillation weights to samples whose teacher predictions remain invariant, indicating greater reliance on causal rather than spurious features. We theoretically show that IWD reduces the student's Spurious-to-Causal (S2C) gradient ratio compared to standard uniformly weighted KD, driving the student toward more invariant representations. Experiments on four NLP benchmarks (MNLI, SQuAD-v2, CoNLL-2003 NER, and SST-2) across two model families (DeBERTa-v3 and Qwen-2.5) demonstrate that IWD consistently outperforms strong KD baselines on OOD evaluations while maintaining competitive in-distribution (ID) performance. Specifically, IWD achieves the highest accuracy in 15 out of 16 OOD benchmarks and improves average OOD performance over standard KD by 4.34 percentage points on NLI and 14.94 percentage points on QA.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 15 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dileesha Kannangara, Sanghamitra Dutta
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
