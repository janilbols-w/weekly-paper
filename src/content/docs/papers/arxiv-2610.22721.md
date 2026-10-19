---
title: "CoLU: Confidence-Weighted Layerwise Unlearning for Large Language Models"
description: "Large language model (LLM) unlearning aims to forget certain information while preserving others, without retraining from scratch."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.22721) · [PDF](https://arxiv.org/pdf/2610.22721)

## 一句话摘要

Large language model (LLM) unlearning aims to forget certain information while preserving others, without retraining from scratch.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) unlearning aims to forget certain information while preserving others, without retraining from scratch. SoTA methods such as NPO, SimNPO, and SatImp balance forgetting and retain through whole model fine-tuning, while FOM-UL explores selective layer updates. Prior works show that suppressing target information can damage retained knowledge. This trade-off can vary across layers even under the same unlearning loss. In this work, we propose Confidence-Weighted Layerwise Unlearning (CoLU), which combines a novel confidence-weighted forgetting and retain regularization while updating a single selected transformer layer, rather than the whole model for unlearning. To reduce CoLU compute cost, we further propose Brief Layer Screening (BLS), which uses a newly defined normalized forgetting-retention (NFR) score to first rank layers through a brief unlearning trials using a subset of forgetting dataset and fewer epochs. BLS pre-selects top-k ranked layer candidates, which will then be fully profiled using full data analysis. BLS is proven to reduce the runtime of CoLU by 60.2-79.7% with almost the same performance. On TOFU dataset, CoLU improves both forgetting and retention over NPO, SatImp, and GA-based FOM-UL in all six TOFU settings, and over SimNPO in five of the six settings. On MUSE Books and News datasets, CoLU achieves the highest retained KnowMem and the PrivLeak closest to zero among the compared SOTA unlearning methods. CoLU presents a new record performance in both unlearning and retain in most settings up to date. Moreover, across the measured settings, average CoLU GPU memory usage is 77.4% to 79.5% lower than full-model unlearning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jingkai Guo, Ziyi Zhao, Chaitali Chakrabarti, Deliang Fan
- 发布：2026-10-19；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
