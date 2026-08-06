---
title: "DIVE: Dynamic Iterative Visual Evidence Construction for Efficient Vision-Language Models"
description: "Visual inputs in vision-language models (VLMs) are often encoded into substantially longer token sequences than text, making visual tokens a major bottleneck for efficient inference."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.04496) · [PDF](https://arxiv.org/pdf/2608.04496)

## 一句话摘要

Visual inputs in vision-language models (VLMs) are often encoded into substantially longer token sequences than text, making visual tokens a major bottleneck for efficient inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Visual inputs in vision-language models (VLMs) are often encoded into substantially longer token sequences than text, making visual tokens a major bottleneck for efficient inference. Abundant recent methods address this bottleneck by scoring token importance and pruning low-scoring tokens in a single pass. However, one-shot scoring is insufficient because a token's prompt-relevant usefulness depends on the evidence already retained. Motivated by this insight, we introduce DIVE (Dynamic Iterative Visual Evidence Construction), a training-free framework that recasts visual-token pruning as dynamic evidence construction. DIVE repeatedly selects the remaining token with the highest residual-conditioned score, updates the visual and prompt residuals to discount the evidence already explained, and re-evaluates the remaining tokens. This select-update-re-evaluate process builds a retained set of complementary, prompt-relevant evidence. Experiments across eight image-understanding benchmarks show that DIVE consistently preserves performance across token budgets. With an 88.9% reduction in visual tokens, DIVE retains 98.2% of the uncompressed model's average performance. Code is available at https://github.com/Zhong-Chenchen/DIVE.git.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Chen Zhong, Xiao An, Zijie Wang, Jiepan Li, Guangyi Yang, Wei He
- 发布：2026-08-06；更新：2026-08-06
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Zhong-Chenchen/DIVE.git](https://github.com/Zhong-Chenchen/DIVE.git)
- 阅读深度：metadata
