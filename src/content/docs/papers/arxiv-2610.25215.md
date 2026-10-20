---
title: "Hidden Cartographer: Hidden State Guided Data Selection for Dual Budgeted Instruction Tuning"
description: "Given the high cost of expert annotation and limited fine-tuning resources, effective data selection from large unlabeled pools under strict budgets has become a crucial step in adapting LLMs to specialized domains."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.25215) · [PDF](https://arxiv.org/pdf/2610.25215)

## 一句话摘要

Given the high cost of expert annotation and limited fine-tuning resources, effective data selection from large unlabeled pools under strict budgets has become a crucial step in adapting LLMs to specialized domains.

## 为什么值得关注

待编辑增强。

## 摘要原文

Given the high cost of expert annotation and limited fine-tuning resources, effective data selection from large unlabeled pools under strict budgets has become a crucial step in adapting LLMs to specialized domains. Existing label-dependent methods risk distorted selection when using pseudo-labels, while traditional active learning methods do not explicitly characterize instruction-tuning dynamics. To address these limitations, we propose Hidden Cartographer (HC), a two-stage framework that uses hidden states to guide annotation and exact training dynamics to select the final training subset. The first stage is Progressive Candidate Expansion, which utilizes the proxy to iteratively select top unlabeled candidates for expert annotation, merging them to recompute training dynamics and update the proxy until the annotation budget is exhausted; the second stage is Exact Cartography Pruning, which ranks these annotated candidates by their exact dynamics scores to isolate a compact subset under the final training budget. Experiments across the medical, legal, and financial domains demonstrate that HC achieves the highest average accuracy among all budgeted baselines, requiring annotation for only 20--30% of the original pool and fine-tuning on just 10--15%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zixuan Qin, Qi Qin, Erbo Li, Ting Wei, Yifan Sun, Zhaoxin Fan
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
