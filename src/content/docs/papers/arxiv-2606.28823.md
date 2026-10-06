---
title: "Labeling Training Data for Entity Matching Using Large Language Models"
description: "Large language models (LLMs) achieve strong entity matching performance without task-specific training data, but applying them to large sets of candidate pairs is slow and costly."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.28823) · [PDF](https://arxiv.org/pdf/2606.28823)

## 一句话摘要

Large language models (LLMs) achieve strong entity matching performance without task-specific training data, but applying them to large sets of candidate pairs is slow and costly.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) achieve strong entity matching performance without task-specific training data, but applying them to large sets of candidate pairs is slow and costly. Matchers built on pretrained language models (PLMs), such as BERT, offer faster inference but require training data. We systematically study knowledge-distillation workflows in which an LLM teacher labels training pairs for a smaller student matcher. We vary pair selection, labeling budget, teacher model, correspondence post-processing, and student model across eight benchmarks, including unseen entities and non-English data. We compare students trained on machine-labeled data with matchers trained on the original benchmark training sets. In most cases, PLM-based matchers trained on LLM-labeled data perform similarly to those trained on benchmark sets. Pair selection matters most for small labeling budgets, where active learning is often most effective. An open-weight teacher trains competitive students, so distillation requires no closed-weight models. Compact PLM-based students compete with much larger LLM students on most tasks while requiring 34 to 459 times less inference time than direct LLM matching. On the two benchmarks with high shares of unseen products, PLM-based students substantially underperform their teachers, as do students trained on benchmark data. Under GPT-5.2 pricing, LLM labeling costs per training set average \$5.86 to \$8.11. These findings support knowledge distillation as a practical approach to reduce the effort of labeling task-specific training data while enabling efficient inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Aaron Steiner, Christian Bizer
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
