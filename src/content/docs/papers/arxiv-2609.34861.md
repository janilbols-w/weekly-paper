---
title: "When Text Matters: Design Principles for Visual Token Pruning in Vision-Language Model"
description: "Visual token pruning has been widely studied as a practical approach to reducing the computational cost of large vision-language models."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.34861) · [PDF](https://arxiv.org/pdf/2609.34861)

## 一句话摘要

Visual token pruning has been widely studied as a practical approach to reducing the computational cost of large vision-language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Visual token pruning has been widely studied as a practical approach to reducing the computational cost of large vision-language models. However, it struggles to preserve essential visual information, which can lead to substantial performance degradation. In particular, image-based token selection can overlook task-relevant details, while text-guided token selection may fail to capture the text--visual relationships needed for complex reasoning. We find that applying textual guidance too early can limit its ability to identify answer-relevant visual regions, whereas text-to-visual attention becomes more informative at intermediate decoder depths. This finding motivates our training-free method, which separates early vision-guided pruning from deferred text-guided reselection. We first prune visual tokens using vision-encoder attention, retain additional candidates until the decoder midpoint, and then use text-to-visual attention to determine the final visual-token set. Across eight benchmarks and three models, our method outperforms the best-performing baselines by an average of 11.10 and 16.84 percentage points in performance recovery at 80% and 90% pruning, respectively, with comparable or lower LLM-prefill latency than most baselines. The source code is publicly available at https://github.com/kmc3661/DeFT

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Minchan Kang, Kyeonghye Park, Seoyoung Cho, Daeshik Kim, Yucheol Cho
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/kmc3661/DeFT](https://github.com/kmc3661/DeFT)
- 阅读深度：metadata
