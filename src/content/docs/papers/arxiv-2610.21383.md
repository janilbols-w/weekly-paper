---
title: "Calibration Language Shapes Block-Influence Pruning in Multilingual Language Models"
description: "Block Influence (BI) ranks Transformer blocks for depth pruning from their input-output cosine change, but the ranking depends on the calibration distribution."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.21383) · [PDF](https://arxiv.org/pdf/2610.21383)

## 一句话摘要

Block Influence (BI) ranks Transformer blocks for depth pruning from their input-output cosine change, but the ranking depends on the calibration distribution.

## 为什么值得关注

待编辑增强。

## 摘要原文

Block Influence (BI) ranks Transformer blocks for depth pruning from their input-output cosine change, but the ranking depends on the calibration distribution. We study whether English calibration transfers to Indian languages in Qwen2.5-1.5B-Instruct, Llama-3.2-1B, and Gemma-2-2B. English, Hindi, Marathi, and Tamil use disjoint Wikipedia articles for calibration and evaluation; every selector receives the same 150-chunk budget, and Tamil is excluded from multilingual aggregation to test cross-script transfer. Across all three models, late-block BI is 20.7-55.5% higher for the three Indian languages than for English, and every predeclared late-minus-middle contrast has a 95% bootstrap interval above zero. This mismatch changes the low-BI blocks selected for removal despite high global rank correlations. Averaging BI over equal English, Hindi, and Marathi budgets mitigates the resulting perplexity damage for Qwen at six removed blocks and for Gemma at all tested depths, including held-out Tamil. The mitigation is not universal: on Llama, balancing improves Hindi and Marathi at two removed blocks but severely harms Tamil, while larger pruning budgets select the same blocks and collapse perplexity regardless of calibration. Rank-mean and minimax-rank aggregators do not dominate the raw mean. These results support a diagnostic claim rather than a universal pruning rule: English-only BI systematically misses late-layer activity for Indian-language text, but multilingual calibration must still be validated per architecture and pruning budget.

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

- 作者：Vedant Pandhare, Piyush Dhoka
- 发布：2026-10-16；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
