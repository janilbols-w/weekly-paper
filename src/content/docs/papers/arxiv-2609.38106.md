---
title: "Pruning for Efficiency, Paying in Fairness: Demographic Disparities in Pruned Speech-LLMs"
description: "Speech-LLMs are expensive to run, making compression important for real-world deployment."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.38106) · [PDF](https://arxiv.org/pdf/2609.38106)

## 一句话摘要

Speech-LLMs are expensive to run, making compression important for real-world deployment.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speech-LLMs are expensive to run, making compression important for real-world deployment. However, compressed models are usually selected using aggregate word error rate (WER), which can hide how pruning affects different demographic groups. In this work, we systematically study the effect of audio encoder pruning on SLAM-ASR for different demographic groups. Using the Fair-Speech and Common Voice datasets, we found that the pruning does not affect all demographic groups equally; the gap between best- and worst-performing groups increases in fold. These disparities appear across all three encoder scales, but only the largest model initially hides them behind aggregate WER. LoRA adaptation improves WER for every group, but benefits groups already performing well more strongly and widens for certain groups. On Common Voice English, Danish, and Dutch, accent gaps persist but do not clearly widen, showing that the fairness effects of pruning vary across datasets and must be measured directly. Our findings suggest that for pruned models, deployment decisions should include per-group WER, with the worst-performing group's error rate as an explicit criterion.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ganesh Pavan Kartikeya Bharadwaj Kolluri, Michael Kampouridis, Ravi Shekhar
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
