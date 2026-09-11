---
title: "Data-Centric Post-Training for Financial Reasoning: Mining, Distillation, and Verifiable Learning"
description: "Financial text, textbooks, and question-answer pairs are abundant, but only a small fraction is directly usable for reasoning-focused post-training."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.10113) · [PDF](https://arxiv.org/pdf/2609.10113)

## 一句话摘要

Financial text, textbooks, and question-answer pairs are abundant, but only a small fraction is directly usable for reasoning-focused post-training.

## 为什么值得关注

待编辑增强。

## 摘要原文

Financial text, textbooks, and question-answer pairs are abundant, but only a small fraction is directly usable for reasoning-focused post-training. Existing QA pairs often lack explicit reasoning, sufficient context, or reliably verifiable answers, while textbooks must first be transformed into synthetic training examples. We present a data-centric pipeline that constructs complementary corpora by mining open-source reasoning traces, distilling financial instruction data, and generating knowledge-graph-guided question-answer pairs from financial educational material. After semantic deduplication, three lightweight sequence classifiers select finance-relevant examples, reject under-specified questions, and identify tasks suitable for reinforcement learning with compact rule-based verifiers. For model adaptation, we study supervised fine-tuning and reinforcement learning, while self-distilled fine-tuning and post-training model merging are used to prevent the loss of financial capabilities already present in the starting model. We evaluate the adapted language models using FINESSE-Bench, reporting aggregate performance and changes relative to their starting checkpoints. Across the selected comparisons, ordinary SFT reduces FINESSE-Bench accuracy by 3.2-4.0 percentage points, whereas self-distilled SFT improves over the corresponding starting models by 1.0-2.8 points. Equal-weight merging recovers 3.0 points over its SFT parent and finishes 0.9 points above the original model; GRPO on hard tasks adds 0.4 points after self-distilled SFT or 3.0 points when applied directly to verifiable tasks. These results show that retention-aware adaptation can improve financial reasoning without the regressions observed after ordinary SFT.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhirayr Hayrapetyan, Andrei Kalmykov, Denis Kokosinskii, Dmitry Stanishevskii, Dmitry Zmitrovich
- 发布：2026-09-09；更新：2026-09-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
