---
title: "AfriNLLB: Efficient Translation Models for African Languages"
description: "In this work, we present AfriNLLB, a series of lightweight models for efficient translation from and into African languages."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2602.09373) · [PDF](https://arxiv.org/pdf/2602.09373)

## 一句话摘要

In this work, we present AfriNLLB, a series of lightweight models for efficient translation from and into African languages.

## 为什么值得关注

待编辑增强。

## 摘要原文

In this work, we present AfriNLLB, a series of lightweight models for efficient translation from and into African languages. AfriNLLB supports 15 language pairs (30 translation directions), including Swahili, Hausa, Yoruba, Amharic, Somali, Zulu, Lingala, Afrikaans, Wolof, and Egyptian Arabic, as well as other African Union official languages such as Arabic (MSA), French, Portuguese, and Spanish. Our training data covers bidirectional translation between English and 13 languages, and between French and two languages (Lingala and Wolof). AfriNLLB models are based on NLLB-200 600M, which we compress using iterative layer pruning and quantization. We fine-tune the pruned models on parallel corpora we curated for African languages, employing knowledge distillation from a larger teacher model. Our work aims at enabling efficient deployment of translation models for African languages in resource-constrained settings. Our evaluation results demonstrate that AfriNLLB models achieve performance comparable to the baseline while being significantly faster. We release two versions of the AfriNLLB models, a Transformers version that allows further fine-tuning and a CTranslate2 version for efficient inference. Moreover, we release all the training data that we used for fine-tuning the baseline and pruned models to facilitate further research.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation, pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yasmin Moslem, Aman Kassahun Wassie, Amanuel Gizachew Abebe
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
