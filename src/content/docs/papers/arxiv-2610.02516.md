---
title: "Student-Guided Teacher Distillation for Efficient LLM Task Routing: Positioning Against Jev-Style System-1 Classifiers"
description: "Zero-shot classifiers are useful for routing user requests to specialized LLM tasks, but scoring every request against a large candidate set is expensive: a zero-shot NLI classifier must evaluate one premise-hypothesis pair per label, so cost scales linearly with taxonomy size."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.02516) · [PDF](https://arxiv.org/pdf/2610.02516)

## 一句话摘要

Zero-shot classifiers are useful for routing user requests to specialized LLM tasks, but scoring every request against a large candidate set is expensive: a zero-shot NLI classifier must evaluate one premise-hypothesis pair per label, so cost scales linearly with taxonomy size.

## 为什么值得关注

待编辑增强。

## 摘要原文

Zero-shot classifiers are useful for routing user requests to specialized LLM tasks, but scoring every request against a large candidate set is expensive: a zero-shot NLI classifier must evaluate one premise-hypothesis pair per label, so cost scales linearly with taxonomy size. We study a student-guided teacher distillation pipeline for a fixed taxonomy of 60 LLM task categories: a compact ModernBERT classifier predicts the full category distribution in one forward pass and retrieves a small top-k candidate set, and a larger DeBERTa-v3 zero-shot NLI classifier reranks only those candidates rather than all 60 labels; the resulting teacher labels iteratively improve the student, which produces sharper candidates for the next round. Unlike generic embedding retrieval or clustering-derived shortlists used in extreme multi-label classification, our candidate generator is trained end-to-end on the target taxonomy and is the same model serving production traffic, distinguishing it from LLM-routing work that routes between candidate models, and from concurrent System-1 encoder-classifier proposals (e.g. TypeSafe AI's Jev and the open-source Laya project) whose training methodology is undocumented or RL-based. Our best student checkpoint reaches 77.5% teacher agreement on a 200-example evaluation set, and preliminary coverage measurements show Coverage@16 of 91-100%, suggesting top-k sets retain most of the teacher's decision-relevant information. We further show truncated top-k teacher scores should not be treated as full 60-class soft targets for KL distillation: zeroing untruncated classes destroys the dark knowledge soft-label distillation depends on, introducing systematic bias rather than a harmless sparse approximation. A complete evaluation, including coverage at multiple k on a held-out set, an embedding-retrieval baseline, and a larger human-reviewed test set, remains in progress.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haifeng Wu, Srinivasan Manoharan, Jian Wan, Fangbo Tu, Junhua Zhao, Xin Chen
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
