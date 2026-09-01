---
title: "Extracting Small Translation Specialists from LLMs by Aggressively Pruning Experts"
description: "Modern large language models (LLMs) achieve state-of-the-art machine translation performance, but they do so as broad generalists largely trained for many tasks and capabilities unrelated to translation."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.28042) · [PDF](https://arxiv.org/pdf/2605.28042)

## 一句话摘要

Modern large language models (LLMs) achieve state-of-the-art machine translation performance, but they do so as broad generalists largely trained for many tasks and capabilities unrelated to translation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern large language models (LLMs) achieve state-of-the-art machine translation performance, but they do so as broad generalists largely trained for many tasks and capabilities unrelated to translation. Thus, they are heavily overparameterized for this task, resulting in excessive memory and compute requirements. In this paper, we present a method for aggressively pruning experts from modern mixture-of-experts LLMs while incurring negligible degradation in translation quality. Our approach exploits expert specialization and the separability of multilingual capabilities in LLMs to identify experts irrelevant to translation. And because of the modular nature of MoEs, these can be easily pruned without any training. Without retraining, we are able to prune half of all experts with negligible degradation and 70% with only minor losses. With a very short SFT, we prune 75% of experts while recovering baseline performance, and in some settings remove nearly 90% while maintaining reasonable translation quality. Overall, our results show that translation requires only a fraction of the LLM, enabling substantial compression of the MoE blocks that contain over 90% of parameters.

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

- 作者：Liu O. Martin, Lucas Bandarkar, Nanyun Peng
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
