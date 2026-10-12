---
title: "COFFEQA: Counterfactual-Guided Few-Shot Distillation for LLM Question Answering"
description: "Knowledge distillation aims to train a smaller student model to mimic a larger teacher model for resource-constrained environments."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.12837) · [PDF](https://arxiv.org/pdf/2610.12837)

## 一句话摘要

Knowledge distillation aims to train a smaller student model to mimic a larger teacher model for resource-constrained environments.

## 为什么值得关注

待编辑增强。

## 摘要原文

Knowledge distillation aims to train a smaller student model to mimic a larger teacher model for resource-constrained environments. However, the process of distillation is typically data-intensive and computationally expensive, particularly for generative tasks. Few-shot distillation offers an alternative by transferring teacher knowledge using limited training samples. However, we observe that few-shot distillation performance is heavily dependent on the choice of these training samples. In fact, we demonstrate that using more uncertain samples near the teacher's decision boundary can significantly deteriorate distillation performance. Motivated by this observation, we propose Counterfactual-guided Few-shot Distillation in Open-book Question Answering (COFFEQA), a novel strategy that aptly uses counterfactuals to provide additional supervision around challenging factual samples. In the generative QA setting, we define a counterfactual as a minimally modified context that induces the teacher to change its response to an alternative answer. We provide geometric insights on how factual-counterfactual pairs can constrain the deviation between the teacher's and student's decision boundaries. We further introduce a new metric, Context Following Difficulty (CFD) that further validates counterfactuals prior to distillation based on agreement with the intended alternative answer and dependence on the modified context. COFFEQA uses CFD-validated factual-counterfactual pairs for few-shot distillation. Experiments across five in-domain and three out-of-domain QA benchmarks using T5 and Qwen2.5 families show that COFFEQA outperforms factual-only distillation baselines under the same few-shot budget. For instance, on TriviaQA, COFFEQA improves over the factual-only baseline by 8.77 average EM points and 9.98 average F1 points under the T5 setting with 32 few-shot pairs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kavinda Kehelella, Sanghamitra Dutta
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
