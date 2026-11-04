---
title: "Online Label-Free Gradient Matching for Continual Language Model Training"
description: "Language models in customer-facing products must be continually updated, since the data they serve shifts over time."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.03496) · [PDF](https://arxiv.org/pdf/2611.03496)

## 一句话摘要

Language models in customer-facing products must be continually updated, since the data they serve shifts over time.

## 为什么值得关注

待编辑增强。

## 摘要原文

Language models in customer-facing products must be continually updated, since the data they serve shifts over time. As retraining on the full accumulated data is impractical, each update should instead run on a small set of examples carrying the training signal of all data seen so far. The strongest current methods build this set by gradient matching, which synthesizes examples whose training gradients match those of the full data. However, they require ground-truth labels, run once on a fixed snapshot rather than on a growing stream, and are slow on large data. We introduce \textbf{OLGA}, which lifts these limitations. It distills unlabeled data by drawing the gradient matching targets from the model's own next-token predictions. Across five text classification benchmarks with phi-1.5, it improves accuracy by 10 percentage points over the strongest selection baseline using as few as five examples. OLGA also distills online data streams by keeping a running rehearsal memory of synthetic examples, which is re-distilled together with each new batch as it arrives. In the online setting, it outperforms the strongest selection-based continual baseline by 6.6 stream-AUC percentage points. Finally, our method scales to large data by pairing distillation with selection in a hybrid pipeline, letting selection handle the mild stage of compression and distillation the extreme one. It cuts runtime by 30\% versus distillation alone at similar accuracy, and beats the best selection-only pipeline by up to 12.6 percentage points.

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

- 作者：Sajjad Pakdamansavoji, Mohammad Reza Rezaei, Ilija Subasic, Pedro Garzon, Radu Paradovschi, Zhao Chen
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
