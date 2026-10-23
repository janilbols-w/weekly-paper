---
title: "Repair Changes Which Layers to Remove: Exact Optima for Depth Pruning of Language Models"
description: "Depth pruning removes entire transformer layers to make large language models faster, and recent methods recover quality by replacing the removed layers with a training-free linear map."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.30552) · [PDF](https://arxiv.org/pdf/2610.30552)

## 一句话摘要

Depth pruning removes entire transformer layers to make large language models faster, and recent methods recover quality by replacing the removed layers with a training-free linear map.

## 为什么值得关注

待编辑增强。

## 摘要原文

Depth pruning removes entire transformer layers to make large language models faster, and recent methods recover quality by replacing the removed layers with a training-free linear map. Which layers to remove, however, is chosen with heuristic scores whose distance from the best choice is unknown. We evaluate every subset of layer groups exactly (about 53,000 pruned models across four families, with and without repair) and find that the best layers to remove depend on the repair: linear repair absorbs the interaction among nearby layers and turns the optimum from a split layout into a contiguous block, so methods that choose layers without the repair miss the repaired optimum by up to 189%. We therefore select layers under the repair that will be applied. A greedy search at the cost of SLEB lowers perplexity by 20% to 66% relative to ReplaceMe on five models up to 27B parameters, and with a task objective it is up to 25 points more accurate given the same data. A second-order expansion of the loss yields a score that selects the repaired block from one forward and one backward pass of the intact model.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jianchang Su, Dawei Xiang, Yifan Zhang, Wei Zhang
- 发布：2026-10-23；更新：2026-10-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
