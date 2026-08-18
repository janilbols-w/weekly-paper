---
title: "Rethinking Reverse KL as Adaptive Entropy Distillation"
description: "Knowledge distillation (KD) is widely used to transfer the capabilities of large language models (LLMs) to smaller students, but existing objectives often struggle to balance faithful imitation and robust generation."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.14685) · [PDF](https://arxiv.org/pdf/2608.14685)

## 一句话摘要

Knowledge distillation (KD) is widely used to transfer the capabilities of large language models (LLMs) to smaller students, but existing objectives often struggle to balance faithful imitation and robust generation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Knowledge distillation (KD) is widely used to transfer the capabilities of large language models (LLMs) to smaller students, but existing objectives often struggle to balance faithful imitation and robust generation. In particular, existing methods mainly combine FKL and RKL, overlooking that RKL itself provides a mechanism for adjusting the student's imitation strength. Motivated by this, we revisit on-policy Reverse Kullback-Leibler (RKL) distillation and decompose its objective into a teacher-fitting term and a student-entropy term, without introducing an explicit FKL branch. We show theoretically that the token-level optimal student distribution corresponds to a tempered variant of the teacher distribution, where the adaptive weight controls the trade-off between mode-seeking and uncertainty preservation. Guided by this insight, we propose \textbf{Adaptive Entropy Distillation (AED)}, which uses the teacher's entropy to dynamically calibrate token-level imitation strength. Experiments on instruction-following and mathematical reasoning benchmarks demonstrate that AED achieves superior overall performance and generally improves teacher--student distributional and entropy alignment.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shizhen Li, Zhiyu Shen, Yuyin Lu, Yunhe Pang, Jielin Song, Yanghui Rao, Fu Lee Wang
- 发布：2026-08-18；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
